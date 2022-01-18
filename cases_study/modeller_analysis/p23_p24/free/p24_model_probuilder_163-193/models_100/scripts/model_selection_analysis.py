
import argparse
import MDAnalysis as mda
from MDAnalysis.analysis import distances
from MDAnalysis.analysis import contacts
import sys 
import os 
import pandas as pd




# normalization for ranking 
def normalize_dist(df):
	dist_list=df.to_list()
	#print(dist_list.mtx)
	minimum=min(dist_list)

	maximum=max(dist_list)

	rank_d=[]
	for i in dist_list:
		r=(i-minimum)/(maximum-minimum)
		r=round(r,4)
		rank_d.append(r)
	return(rank_d)

def normalize_contact(df):
	contact_list=df.to_list()
	minimum=min(contact_list)
	maximum=max(contact_list)

	rank_c=[]
	for i in contact_list:
		r=(maximum-i)/(maximum-minimum)
		r=round(r,4)
		rank_c.append(r)
	return(rank_c)

# fun to get the N-C terms distances of each structure
def get_dist_terms(u):
	res=u.select_atoms('protein').residues.resids

	c_term=u.select_atoms(f'name CA and resid {res[len(res)-1]}') #revise
	n_term=u.select_atoms(f'name CA and resid {res[0]}') #revise 
	# compute the distances between N-C terms
	dist_arr= distances.distance_array(c_term.positions, n_term.positions)
	
	return(dist_arr)



def contact_sum_C(a, SEG1_l,SEG1_u,SEG2_l,SEG2_u,HELIX_l,HELIX_u, count,i, c_seg):

	

	single=c_seg.select_atoms(f'resid {a}')
	rest=c_seg.select_atoms(f'resid {a+1}-{SEG2_u}')
	dist3=contacts.distance_array(single.positions,rest.positions)
	#print(dist3)
	contact3=contacts.contact_matrix(dist3,4).sum()
	#print(contact3)
		
	return contact3

def contact_sum_N(a, SEG1_l,SEG1_u,SEG2_l,SEG2_u,HELIX_l,HELIX_u, count,i, n_seg):
	
	single=n_seg.select_atoms(f'resid {a}')
	#print('SING', single)
	rest=n_seg.select_atoms(f'resid {a+1}-{SEG1_u}')
	#print('REST', rest)
	dist4=contacts.distance_array(single.positions,rest.positions)
	#print(dist4)
	contact4=contacts.contact_matrix(dist4,4).sum()
	#print(contact4)
	return(contact4)


def contact_score(u,SEG1_l, SEG1_u, SEG2_l,SEG2_u,HELIX_l,HELIX_u):   #FIND A WAY TO COMPUTE CONTACT ONLY AMONG SIDE CHAINS 

	final_sum=[]
	# distance n term seg vs only tm helix
	n_seg=u.select_atoms(f'resid {SEG1_l}-{SEG1_u}')
	sele1=u.select_atoms(f'resid {HELIX_l}-{HELIX_u}') 
	dist1=contacts.distance_array(n_seg.positions,sele1.positions)
	#print(dist1)
	contact1=contacts.contact_matrix(dist1,4).sum()

	final_sum.append(contact1)
	
	
	# distance c term seg vs tm helix
	c_seg=u.select_atoms(f'resid {SEG2_l}-{SEG2_u}')
	sele2=u.select_atoms(f' resid {HELIX_l}-{HELIX_u}')
	dist2=contacts.distance_array(c_seg.positions,sele2.positions)	
	contact2=contacts.contact_matrix(dist2,4).sum()	
	final_sum.append(contact2)

	# distance among C term residues
	count=0
	for a in c_seg.residues.resids:
		count+=1  #review
		i=a+1
		if count < len(c_seg.residues.resids):
			
			final_sum.append(contact_sum_C(a, SEG1_l,SEG1_u,SEG2_l,SEG2_u,HELIX_l,HELIX_u, count,i, c_seg))
			
	# distance among N term residues
	count=0
	for a in n_seg.residues.resids:
		
		count+=1  #review
		i=a+1
		if count < len(n_seg.residues.resids):
			final_sum.append(contact_sum_N(a, SEG1_l,SEG1_u,SEG2_l,SEG2_u,HELIX_l,HELIX_u, count,i, n_seg))	
				
	return (sum(final_sum))





parser=argparse.ArgumentParser()

parser.add_argument('-p',
					'--path',
					dest='path',
					type=str,
					required=True)
parser.add_argument('-C',
					'--c-term-first-last',
					dest='cterm',
					nargs='+',
					type=int,
					required=True)
parser.add_argument('-N',
					'--n-term-fist-last',
					dest='nterm',
					nargs='+',
					type=int,
					required=True)
parser.add_argument('-H',
					'--helix-c-n-term',
					dest='helix',
					type=int,
					nargs='+',
					required=True)


args=parser.parse_args()

path=args.path
c_region=args.cterm
n_region=args.nterm 
helix=args.helix


# make a list of all the .pdb model files
path=args.path
pdb_l=sorted(os.listdir(os.path.abspath(path)))


SEG1_l=n_region[0]
SEG1_u=n_region[1]
SEG2_l=c_region[0]
SEG2_u=c_region[1]
HELIX_l=helix[0]
HELIX_u=helix[1]

data_dist={}
data_contact={}
data={}
for pdb in pdb_l:
	
	path_file=os.path.relpath(path+pdb)
	#print(path_file)
	u=mda.Universe(path_file)
	# get the N/C-term distance 
	distance_score=get_dist_terms(u)
	# convert model path and distance into a dict
	data_dist[path_file]=round(float(distance_score),4)
	
	# get residues contacts 
	contact_scores=contact_score(u, SEG1_l, SEG1_u, SEG2_l,SEG2_u,HELIX_l,HELIX_u)
	# convert model path and contacts into a dict
	data_contact[path_file]=contact_scores
	# convert model paths, distance and contact into a dict
	data[path_file]=float(distance_score), contact_scores    #remove this, use the merge for df 



# convert all dicts into dataframe 

df_distance=pd.DataFrame.from_dict(data_dist, orient='index', columns=['distance N/C-term'])
df_distance.index.name='model'

df_distance['norm_d']=normalize_dist(df_distance['distance N/C-term'])
df_distance=df_distance.sort_values(by=['norm_d'], ascending=False)

csv_data=df_distance.to_csv('distance.tsv', sep='\t')

df_contact=pd.DataFrame.from_dict(data_contact,orient='index', columns=['#contacts'])
df_contact.index.name='model'
df_contact['norm_c']=normalize_contact(df_contact['#contacts'])
df_contact=df_contact.sort_values(by=['norm_c'], ascending=True)
csv_data1=df_contact.to_csv('contact.tsv', sep='\t')




# merge data frame and compute the final rank 

df_c=pd.concat([df_distance, df_contact], axis=1, join='inner')
df_c['rank']=round(((df_c[['norm_c','norm_d']].sum(axis=1))/2),4)
df_c=df_c.sort_values(by=['rank'], ascending=False)
csv_data2=df_c.to_csv('merged.tsv', sep='\t')

































