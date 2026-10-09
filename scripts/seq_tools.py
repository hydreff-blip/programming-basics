seq = "AATTCTGTAGCTGGTACCTATATATGCCCGTA"
print(len(seq))
C = seq.count("C")
G = seq.count ("G")
GC = C+G
percent = GC/len(seq)*100
print(percent)
print(seq[:3])
print(seq[-3:])
RNA = seq.replace("T","U")
print (RNA)
comp = seq.replace("A","t").replace("T", "a").replace("G","c").replace("C", "g")
rev_comp = comp.upper()[::-1]
print(seq.startswith("ATG"))
print(seq[0:])
print(seq[1:])
print(seq[2:])