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
#taking a pdb file of choice from the user 
# the strip() is to strip spaces in the input of the user so there is less error 
# the lower() is to take all the input of the user in small letter to reduce the error rate as most pdb files are saved in lower case letters 
pdb_file = input("Select a pdb file of your choice?").strip().lower()
if pdb_file.endswith(".pdb"):
    file = open(pdb_file)
    structure = parser.get_structure(file, file)
else:
    print("Wrong file.... restart the program")
    sys.exit()
#calling a class in biopython
ppb = PPBuilder()
# using the functions of the class to get the sequence of the protein (pdb file)
for pp in ppb.build_peptides(structure):
    seq1 = pp.get_sequence()
    print("The sequence of the structure is :  " + seq1)
    
# storing the model of the structure of the first pdb file
model = structure[0]
# asking the user for the second file 
# using strip() and lower()
second_file = input("What file do you wanna align").strip().lower()
second = open(second_file)
second_structure = parser.get_structure(second, second)


# doing the same thing as explained above to get the sequence of the protein
for pp in ppb.build_peptides(second_structure):
    seq2 = pp.get_sequence()
    print("The sequence of the structure is : " + seq2)

# rotating and translating atoms of important residues together 
# also obtaining their RMSD value(check user guide)
print("Superimposition uses the CA atoms of the choosen residues, the output file can be viewed in Pymol")
# taking the input of residue the user wants to superimpose

begin_id =int(input("What important residues do you want to superimpose, beginning position "))
end_id = int(input("What important residues do you want to superimpose, end position"))
aligned_atoms = range(begin_id, end_id + 1)

# storing the model of the second structure
second_model = second_structure[0]
first_atoms = []
second_atoms = []
for first_chain in model:
    for res in first_chain:
        if res.get_id()[1] in aligned_atoms:
            first_atoms.append(res['CA'])
# printing the atoms of the residue selected from the first_file
# printing it putside the first loop because I do not want it to keep looping

#print( first_atoms)

for second_chain in second_model:
    for res in second_chain:
        if res.get_id()[1] in aligned_atoms:
            second_atoms.append(res['CA'])
#print(second_atoms)

def superimpose(first, second):
    superimpose = PDB.Superimposer()
    superimpose.set_atoms(first, second)
    model = second_model
    superimpose.apply(model.get_atoms())
    print("The RMSD is: ")
    print(superimpose.rms)
    structure = second_structure
    io = PDB.PDBIO()
    io.set_structure(structure)
    saved_file = input("Name of output file (.pdb)?")
    io.save(saved_file)
    return saved_file 
    

stored_file = superimpose(first_atoms, second_atoms)
print("File saved as: " + stored_file)

# a function to align the sequence of the two files 
# global alignment
# returns the best score of the alignment 

def seq_alignment(structure, structure2):
    from Bio import pairwise2
    from Bio.pairwise2 import format_alignment
    align = pairwise2.align.globalxx(structure, structure2)
    format_align = format_alignment(*align[0])
    return format_align

question = input("Would you like to see the sequence alignment and the score of the best alignment? Yes/no").lower().strip()
if question == "yes":
	seq_align = seq_alignment(seq1, seq2)
	print(seq_align)
else:
	print("Thank you for using my program")
