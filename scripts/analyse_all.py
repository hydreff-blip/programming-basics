sequences = ["ATGCGC", "GGCATTAGC", "TTA", "ATGGGCCCTA", "ATGNNNCGC"]
lengths = []
start_ATG = 0

# 1-3 together
for seq in sequences:
    print(seq, len(seq))    # print each sequence with its length
    lengths.append(len(seq))    # build a list of lengths
    if seq.startswith("ATG"):   # count how many sequences start with ATG
            start_ATG = start_ATG + 1
print (sum(lengths)/len(lengths))   # print the average length
print (start_ATG)   # print how many sequences start with ATG

# 4 separately
for seq in sequences:
      if len(seq) > 5:
            print (seq)

# 5
for seq in sequences:
    gc = 0
    for base in seq:
        if base == "G" or base == "C":  # or we could do it using "count" function
            gc = gc + 1
    gc_percent = gc/len(seq)*100
    print (gc_percent)

#bonus
for seq in sequences:
    if len(seq) == max(lengths):
        for i in range (0, len(seq), 3):
            print(seq[i:i+3])