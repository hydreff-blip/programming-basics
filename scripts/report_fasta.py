# broken_report.py
# GC content report for sequences in a FASTA file.
# This script has 5 bugs. Run it, read the FIRST error, fix it, run again.


def read_fasta(path):
    sequences = {}
    name = None
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                name = line[1:]
                sequences[name] = ""
            else:
                sequences[name] += line
    return sequences


def gc_content(seq):
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return gc


def report(name, seq): # bug 1: SyntaxError: expected ':'
    gc = gc_content(seq)
    print(f"Sequence {name}: length  {len(seq)}") # bug 2: TypeError: can only concatenate str (not "int") to str
    print(f"  GC content: {gc:.1f}%") # silent bug: multiplying by 100 for the second time
    return gc


sequences = read_fasta("sequences.fasta")

results = {}
for name, seq in sequences.items():
    results[name] = report(name, seq) # bug 3: report function was not working

average = sum(results.values()) / len(results) # bug 4 - typo
print(f"Average GC: {average:.1f}%") 

# print("Reference sequence:", sequences["ref"]) # we don't have a reference sequence in the fasta file, but if we change it to name of an existing sequence, it works
