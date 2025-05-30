import random


def nucleotides() -> list[str]:
    return ["A", "C", "G", "T"]

def generate_random_seq():
    return ''.join(random.choice(nucleotides()) for _ in range(50))

def load_dna_seq(file_path: str) -> str:
    with open(file_path, 'r') as dna_seq:
        return dna_seq.read().strip()

def verify_seq(dna_seq: str):
    dna_seq_normalized = dna_seq.upper()
    for nucleotide in dna_seq_normalized:
        if nucleotide not in nucleotides():
            print("Não é uma sequência válida")
            return False
    print("Sequência válida!")
    return dna_seq_normalized

def count_nucleotide_freq(dna_seq: str) -> dict:
    frequency_counter = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in dna_seq:
        frequency_counter[nucleotide] += 1
    return frequency_counter

def dna_to_rna(dna_seq: str) -> str:
    return dna_seq.replace("T", "U")
