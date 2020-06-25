from Bio import PDB
from Bio.PDB import * 
from Bio.PDB import parse_pdb_header
from numpy import loadtxt
import numpy as np
from Bio.PDB import PDBList
from Bio.PDB.Entity import Entity
from Bio.PDB.Residue import Residue
import sys

parser = PDBParser()
pdb_file = input("Select a pdb file of your choice?").strip().lower()
if pdb_file.endswith(".pdb"):
	file = open(pdb_file)
	structure = parser.get_structure(file,file)
else:
	print("Wrong file has been parsed, Restart the program")
	sys.exit()

    

model = structure[0]

# list of atoms to get all atoms in the structure
atoms = [atom for atom in structure.get_atoms()]



        

# putting all the atoms and residue name in a dictionary 
"""
atom_dic = {}
for residue in residues:
    atom_dic[residue.resname] = atoms
#print(atom_dic)
"""
# getting the coordinates of all atoms and storing it incase user wants to calculate atomic distance of their choice
atom_coord = {}
for atom in atoms:
    atom_coord[atom.name] = atom.get_coord()
# to print out the residue in the chain so that user can select what residue distance, user wants to calculate 
chain = model["A"]
for residue in chain:
	print(residue)

def residue_distance(residue_one, residue_two):
    model = structure[0]
    chain = model["A"]
    for residue in chain:
    	#print(residue)
        res_one = chain[residue_one]
        res_two = chain[residue_two]
        for atom in residue:
        	# to get the coordinates of the selected
            one_res = res_one["CA"].get_coord()
            two_res =  res_two["CA"].get_coord()
            
        try:
        	#using mumpy for mathematical calculation
            residue_distance = np.linalg.norm(one_res - two_res)
            return residue_distance
        except KeyError:
            print("Residue does not have CA")



residue_one = int(input("Residue position on the chain(based on their resseq position)?"))
residue_two = int(input("Residue position on the chain (based on their resseq position)? "))
res_dist = residue_distance(residue_one, residue_two)
print("The residue distance is: ") 
print(res_dist)
   
def atomdistance(atom1, atom2):
    atom_1 = atom_coord[atom1]
    atom_2 =  atom_coord[atom2]
    try:
    	# the use of numpy to calculate the distance since the values are now in coordinates(array)
        atom_distance = np.sqrt(np.square(np.subtract(atom_1,atom_2)).sum())
        return atom_distance
    except KeyError:
        print("Atom does not exist")

question = input("Do you want to calculate the atom distance of your choice?  yes/no").lower().strip()

if question == "yes":
	atom1 = input("The first atom you want to calculate?").strip().upper()
	atom2 = input("The second atom you want to calculate?").strip().upper()
	atomic_distance = atomdistance(atom1, atom2)
	print("The atom distance between first atom and second atom is ")
	print(atomic_distance)
	print("finished")
else:
	("Thanks for using my program")
