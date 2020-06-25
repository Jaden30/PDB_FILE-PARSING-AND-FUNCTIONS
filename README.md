#PARSING AND ANALYSIS OF A PDB FILE

AUTHOR: AUSTINE-ORIMOLOYE OLA
#FEATURES AND OVERVIEW
Set of programs written in python that analyses a pdb_file and outputs some of the analysis in a pdb_file,pymol or on the command line
1. Parses pdb_file functions include residue_distance, atomdistance.
2. Series of scripts to analyse the pdb_file
3. Result output

#DEPENDENCIES AND REQUIREMENTS
Run on a linux command line
Numpy needs to be installed, #pip install numpy
Biopython installation is needed 
Download Biopython - pip install Biopython
Pymol, a visualization tool needs to be installed 
Python3.7 

#SCRIPTS AND FUNCTIONS
distance.py - Calculates the residue distance and atom distance in a pdb file, the residue to be calculated has to be inputted based on the chain position which would be printed on the screen, any residue can be choosen based on the chain position. 
The atom distance is calculated by inputting atom of your choice. The instructions on the screen should be strictly followed.

impose.py - Superimposition and pairwise sequence alignment, superimposition is to rotate and translate one set of atoms on top of another to minimize RMSD is the root mean square deviation of atomic positions, it is the measure of average distance between the atoms(usually CA atoms) of superimposed proteins, the script also calculates the RMSD of the residues superimposed, the pairwise sequence alignment is the global alignment of the two sequences of pdb_file that is been analysed, showing the best score and their alignment. The output file of the superimposition can be loaded in pymol.

color_by_prop.py - This is a script that colors the residues in a pdb file based on their properties(charges and behaviour). It is majorly run on the command line and pymol.

#WORKING DIRECTORY
Working directory should be your home directory 
username :~$
Majorly because of loading pymol from the command line.
Working directory should also contain pdb files you want to parse and analyse

#USAGE
The distance.py and impose.py is run pn the command line in the right workinhg directory, the instructions on input should be strictly followed, in order to get the right output. 
On the command line in your working directory
username :~$ python3 distance.py 
username :~$ python3 impose.py 
The color_by_prop.py uses the command line and the pymol command line, in your working directory 
username :~$ pymol name of pdb_file
This would load the pdb_file to be analysed into pymol
On pymol command line write :
run color_by_prop.py
Then:
color_by_prop all
Then type "ray" on the command line and save the image.
The color_by_prop all calls the function name in the color_by_prop.py script.

### PUBLICATION 
Chang, J., Chapman, B., Friedberg, I., Hamelryck, T., De Hoon, M., Cock, P., Antao, T. and Talevich, E., 2010. Biopython Tutorial and Cookbook. Update, pp.15-19.

DeLano, W.L. and Bromberg, S., 2004. PyMOL user’s guide. DeLano Scientific LLC, pp.1-66.

GitHub Repository Pymol-Scripts/Pymol-script-repo






