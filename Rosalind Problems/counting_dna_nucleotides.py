from dna_toolkit import *


path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_dna_1_dataset.txt'
sequence = load_dna_seq(path_to_dna)

print(count_nucleotide_freq(verify_seq(sequence)))
