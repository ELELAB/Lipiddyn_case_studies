#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 10:03:28 2020

@author: Matteo Lambrughi
"""

#asks user 1 pair spec-conc
def getPair():
    spec = input ('Enter spec: ')
    try:
        conc = float(input ('Enter concentration: '))
    except:
        print ('ERROR -------------- EXPECTED FLOAT -------------- ERROR')
        conc = float(input ('Reinsert concentration: '))
    return [spec, conc]

def findMax(n):
    nx = []
    for i in n:
        nx.append(sum(i))
    return nx.index(max(nx))

def findMin(n):
    return n.index(min(n))

def findMatch(j):
    found =''
    with open("matches.txt") as search:
        for line in search:
            line = line.rstrip()  # remove '\n' at end of line
            linesplit = line.rsplit('\t',1)
            
            if linesplit[0] == j:
                found = line
                break
    return found

import pandas as pd

excel_file = 'classes_ER.xlsx'
excel_sheet = 'Classes_median_no_CE_Lyso_FA'
xlsx = pd.read_excel(excel_file,  excel_sheet, header=0, usecols='A:B', index_col = 0, nrows=19, engine='openpyxl')

#print('Data selected:')
#print(xlsx)

print('Columns: ')


i=0
for col in xlsx.columns:
    print (str(i) + ' ' + col)
    i = i + 1

print()
colToUse = input ('Enter column index to use for calcs: ')
colIndex = int(colToUse)

print('Selected column @ index ',colIndex, xlsx.columns[colIndex])

colToUseData = xlsx[xlsx.columns[colIndex]]
print(colToUseData)

# SUMS
sumNames = ['Cer','Chol','CL','DAG','GM2','GM3','PA','PC','PE','PG','PI','PS','SM']
sumList =[[0,1,5,8,18],[2],[3],[4],[6],[7],[9],[10,11],[12,13],[14],[15],[16],[17]]
sums = []
sum_part = 0

for i in range(0,len(sumNames)):
    sum_part = 0
    sl = sumList[i]
    for j in sl:
        sum_part = sum_part + colToUseData[j]
    sums.append(sum_part)

#POP COUNT
print()
popCount = input ('Enter the number of lipids for each leaflet of the membrane: ')
print('Population set to: ',popCount)
popCount = int(popCount)
print()

#SPECIES-CONCENTRATION USER INSERT
SP_C = []
nInsert = []
for i in sumNames:
    SP_C_PART = []
    stri = 'Insert the number of lipid species and concentrations for ' + i + ': '
    try:
        c = int(input (stri))
    except:
        print ('ERROR -------------- EXPECTED INT -------------- ERROR')
        stri = 'Re' + stri
        c = int(input (stri))
    nInsert.append(c)
    if(c==0):
        print ('No lipid spec-conc pair for ', i)
    else:
        for j in range(0,c):
            pair = getPair()
            SP_C_PART.append(pair)
            j = j+1
            
    for x in SP_C_PART:
        print ('Inserting pair ', x, ' in ', i)
    print()
    SP_C.append(SP_C_PART)

#FINE INSERT
#list with sum of user inserts
sumInsert =[]
#list with increments
incremento =[]
     
#SUM INSERT
s = 0.0
for i in range(0,len(SP_C)):
    s = 0.0
    if nInsert[i] != 0:
        for j in SP_C[i]:
            s = s + j[1]    
    else:
        s = 0.0
    sumInsert.append(s)
print (sumInsert)

#CALC INCREMENT
for i in range(0,len(sumInsert)):
    if nInsert[i] != 0:
        inc = (sums[i] - sumInsert[i])/nInsert[i]
    else:
        inc = 0.0
    incremento.append(inc)
print (incremento)
#CORRECTION
#list of correct vals
corretto = SP_C
for i in range(0,len(corretto)):
    if nInsert[i] != 0:
        for j in SP_C[i]:
            j[1] = j[1] + incremento[i]  
print (corretto)
#INT ROUNDED + totNumLip
n_part = []
n = []
totNumLip = 0
for i in range(0,len(corretto)):
    n_part = []
    if(nInsert[i] != 0):
        for j in corretto[i]:
            calc = j[1]/100 * popCount
            totNumLip = totNumLip + round(calc)
            n_part.append(round(calc))
    else:
        n_part.append(0)
    n.append(n_part)

print(n)
print ('tot num lipids: ', totNumLip)

#under pop -> add to min of biggest class
if totNumLip != popCount:
    maxI = findMax(n)
    minI = findMin(n[maxI])
    diff = popCount - totNumLip
    n[maxI][minI] = n[maxI][minI] + diff 
    print('Added ', diff, ' to ', sumNames[maxI], ' ', corretto[maxI][minI][0] )

#CORRISP IN TXT FILE
with open('out.txt','w+') as out:
    for i in range(0,len(sumNames)):
        out.write(sumNames[i]+'\n')
        line = ''
        for j in range(0,len(corretto[i])):
            line = findMatch (corretto[i][j][0])
            line.replace('\t','\t\t')
            out.write(line + '\t' + str(n[i][j]) + '\n')

print ('----------DONE--------')
