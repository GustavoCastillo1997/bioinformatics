from dna_toolkit import *


path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_2.txt'
sequence = load_dna_seq(path_to_dna)

print(dna_to_rna(verify_seq(sequence)))
