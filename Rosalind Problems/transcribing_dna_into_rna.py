from dna_toolkit import *


path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_dna_2_dataset.txt'
sequence = load_dna_seq(path_to_dna)

print(dna_to_rna(verify_seq(sequence)))
