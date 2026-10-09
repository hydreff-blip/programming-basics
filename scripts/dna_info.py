# seq = "TGACGTTCGCATGCATCGATTA"
# print (len(seq))
# G = seq.count ("G")
# C = seq.count ("C")
# GC = round((G+C)/len(seq)*100, 2)
# print("GC:", GC, "%")


#seq = "ATGGCCATTGTAATGGGCCGC"
#print (seq[:3])
#print (seq[-6:])
#print (seq[::-1])
#print (seq.replace("T", "U"))
#first = seq.find ("ATG")
#print (first)
#print(seq.find ("ATG", first+1))


seq = "ATGC"
complement = seq.replace("A", "t").replace("T", "a")
complement = complement.replace("G", "c").replace("C", "g")
rev_comp = complement.upper()[::-1]
print(rev_comp)