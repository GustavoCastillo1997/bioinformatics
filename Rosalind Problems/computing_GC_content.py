from dna_toolkit import *

path_to_dna = 'C:\\Users\\Gustavo\\OneDrive - APCBRH\\Documentos\\Rosalind Problems\\rosalind_5.txt'
sequences = load_dna_seq_fasta(path_to_dna)

max_gc_key = None
max_gc_value = 0

for seq in sequences:
    if gc_content(verify_seq(sequences[seq])) > max_gc_value:
        max_gc_key = seq
        max_gc_value = gc_content(sequences[seq])
print(f'Sequência com o maior GC Content: {max_gc_key}: {max_gc_value:.5f} %')
