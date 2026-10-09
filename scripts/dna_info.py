seq = "TGACGTTCGCATGCATCGATTA"
print (len(seq))
G = seq.count ("G")
C = seq.count ("C")
GC = round((G+C)/len(seq)*100, 2)
print("GC:", GC, "%")