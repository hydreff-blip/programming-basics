sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA"]
gene = ("BRCA1", "chr17", 43044295, 43125483)
print(len(sequences))
print(sequences[0],"\n"+sequences[-1])
sequences.append("TATGCTA")
print(sequences)
lengths = [len(sequences[0]), len(sequences[1]), len(sequences[2]), len(sequences[3]), len(sequences[4])]
print(lengths)
average = sum(lengths)/len(lengths)
print(min(lengths), max(lengths),average)
name, chrom, start, stop = gene
print(f"{name} is on {chrom}, and is {stop-start} bases long")
# gene[0] = "HBA1" # TypeError: 'tuple' object does not support item assignment
genes = [("BRCA",81188),("TP53", 25759)]
print(genes[1][1])