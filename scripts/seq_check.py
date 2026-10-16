seq = "ATCGATGCGNNCGCGCGCGATATACNNGATAGCGATCGATATCGATTACGTANNNCGC"

if len(seq) < 30:
    print("Too short")
if "N" in seq:
    print("Contains unknown bases")
GC = ((seq.count ("G") + seq.count ("C"))/ len(seq))
if GC > 0.6:
    print ("GC rich")
elif GC < 0.4:
    print ("AT rich")
else:
    print ("Balanced")
if seq.startswith("ATG") and len(seq) % 3 == 0:
    print ("Possible ORF")
else:
    print ("Not ORF :(")