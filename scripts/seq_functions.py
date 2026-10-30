def gc_content(seq):
    g_amount = seq.count("G")
    c_amount = seq.count("C")
    return round((g_amount + c_amount)/len(seq), 2)

print(gc_content("ATCGATAGCTA"))

def reverse_complement(seq):
    complement = seq.replace("A","t").replace("T","a").replace("G", "c").replace("C","g")
    reverse = complement.upper()[::-1]
    return reverse

print (reverse_complement("ATCG"))


def is_usable(seq):
    if "N" in seq == True:
        print("Not usable")
    else:
        print ("Usable")

is_usable("ATCNGACT")