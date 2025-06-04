from dna_toolkit import *

path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_6.txt'
sequences = load_dna_seq(path_to_dna)

seq_1 = sequences[0]
seq_2 = sequences[1]

print(count_point_mutation(seq_1, seq_2))
