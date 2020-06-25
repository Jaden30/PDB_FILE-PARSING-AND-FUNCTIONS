from Bio import PDB
from Bio.PDB import * # to be able to use the classes in Bio.PDB

pdbl = PDBList()
pdb_file = input("Select a pdb file of your choice?")
pdbl.retrieve_pdb_file(pdb_file, pdir = '.', file_format = 'pdb')
#opened_file = open(pdb_file)
