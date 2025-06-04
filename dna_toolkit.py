import random
from typing import Union

def nucleotides() -> list[str]:
    return ["A", "C", "G", "T"]

def generate_random_seq() -> str:
    return ''.join(random.choice(nucleotides()) for _ in range(50))

def load_dna_seq(file_path: str) -> Union[str, list[str]]:
    with open(file_path, 'r') as dna_seq:
        dna_seq_str = dna_seq.read()
        if '\n' in dna_seq_str:
            return dna_seq_str.split('\n')[:-1]
        return dna_seq_str.strip()

def load_dna_seq_fasta(file_path: str) -> dict[str: str]:
        fasta_seqs = {}
        with open(file_path, 'r') as fasta_file:
            lines = fasta_file.readlines()
            for line in lines:
                if line.startswith(">"):
                    key = line[1:].strip()
                    fasta_seqs[key] = ""
                else:
                    fasta_seqs[key] = fasta_seqs[key] + line.strip()
        return fasta_seqs

def verify_seq(dna_seq: str) -> Union[str, bool]:
    dna_seq_normalized = dna_seq.upper()
    for nucleotide in dna_seq_normalized:
        if nucleotide not in nucleotides():
            return False
    return dna_seq_normalized

def count_nucleotide_freq(dna_seq: str) -> dict:
    frequency_counter = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in dna_seq:
        frequency_counter[nucleotide] += 1
    return frequency_counter

def dna_to_rna(dna_seq: str) -> str:
    return dna_seq.replace("T", "U")

def dna_reverse_complement(dna_seq: str) -> str:
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[nuc] for nuc in reversed(dna_seq))

def gc_content(dna_seq: str) -> float:
    total = len(dna_seq)
    gc_nucleotides = sum(1 for nucleotide in dna_seq if nucleotide in ['G', 'C'])
    gc_percentage = (gc_nucleotides / total) * 100
    return gc_percentage

def count_point_mutation(dna_seq_1: str, dna_seq_2: str) -> int:
    return sum(1 for nuc_seq_1, nuc_seq_2 in zip(dna_seq_1, dna_seq_2) if nuc_seq_1 != nuc_seq_2)
