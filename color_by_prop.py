
import colorsys,sys
from pymol import cmd
# a dictionary of the residue(amino acid(proteins), the single letter as the key  and their three word representation as the value 
amino_3 = {
  'A': 'ALA', 
  'C': 'CYS', 
  'D': 'ASP', 
  'E': 'GLU', 
  'F': 'PHE', 
  'G': 'GLY', 
  'H': 'HIS', 
  'I': 'ILE', 
  'K': 'LYS', 
  'L': 'LEU', 
  'M': 'MET', 
  'N': 'ASN', 
  'P': 'PRO', 
  'Q': 'GLN', 
  'R': 'ARG', 
  'S': 'SER', 
  'T': 'THR', 
  'V': 'VAL', 
  'W': 'TRP', 
  'Y': 'TYR', 
}
# a dictionary of amino acid and their properties(.i.e positvely charged etc)
amino_prop = {
  'A': 'hydrophobic',
  'C': 'cysteine',
  'D': 'negative',
  'E': 'negative',
  'F': 'aromatic',
  'G': 'glycine',
  'H': 'polar',
  'I': 'hydrophobic',
  'K': 'positive',
  'L': 'hydrophobic',
  'M': 'hydrophobic',
  'N': 'polar',
  'P': 'proline',
  'Q': 'polar',
  'R': 'positive',
  'S': 'polar',
  'T': 'polar',
  'V': 'hydrophobic',
  'W': 'aromatic',
  'Y': 'aromatic',
}
# the function and the parameters
def color_by_prop(selection = "all",  hydrophobic='grey90',
        aromatic='lightpink',
        polar='palecyan',
        positive='blue',
        negative='red',
        cysteine='paleyellow',
        proline='palegreen',
        glycine='green'):
# a dictionary to show the color and type of the colors based on the parameters passed in the function 
	color_type = {
    'hydrophobic': hydrophobic,
    'aromatic': aromatic,
    'polar': polar,
    'positive': positive,
    'negative': negative,
    'cysteine': cysteine,
    'proline': proline,
    'glycine': glycine,
 	 }

 	for amino in amino_prop:
 		select = selection + " and r. %s" % amino_3[amino]
 	 	cmd.color(color_type[amino_prop[amino]], select)
    
cmd.extend("color_by_prop",color_by_prop)
