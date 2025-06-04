from dna_toolkit import *


path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_3.txt'
sequence = load_dna_seq(path_to_dna)

print(dna_reverse_complement(verify_seq(sequence)))
