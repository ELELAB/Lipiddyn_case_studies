#comparative modeling with multiple templates
from modeller import *              # Load standard Modeller classes
from modeller.automodel import *    # Load the automodel class

class MyModel(automodel):
      def user_after_single_model(self):
        # each model:
        self.rename_segments(segment_ids=('A'), renumber_residues=[163])
      def select_atoms(self):
          return selection(self.residue_range('1:A', '6:A'),self.residue_range('28:A', '31:A')) 
#      def special_restraints(self, aln):
#        rsr = self.restraints
#        at = self.atoms  
#        rsr.add(secondary_structure.alpha(self.residue_range('4', '9')))
env = environ()
# directories for input atom files
env.io.atom_files_directory = ['.', '../atom_files']
env.io.hydrogen = True
env.io.hetatm = True

a = MyModel(env,
            alnfile  = 'xxx.ali', # alignment filename
            knowns   = ('p24_last_A'),     # codes of the templates
            sequence = ('p24_163-193'))               # code of the target
a.starting_model= 1                 # index of the first model
a.ending_model  = 100               # index of the last model
                                    # (determines how many models to calculate)
a.make()                            # do the actual comparative modeling
