def find_pattren_positions(dna_sequence,pattren):

    poditions =[]
    seq_len = len(dna_sequence)
    pat_len = len(pattren)

    for i in range (seq_len - pat_len + 1):
        if dna_sequence[i:i + pat_len ] == pattren:
            poditions.append(i)
    return poditions

dna_seqence = "ACGTAGCTAGGCTA"
pattren = "GCTA"

positons = find_pattren_positions(dna_seqence,pattren)
print(f"Pattren'{pattren}' found at positions:{positons} ")