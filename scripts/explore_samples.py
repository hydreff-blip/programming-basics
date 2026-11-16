import pandas as pd
df = pd.read_csv("data/samples.csv")

number_of_samples = df.shape[0]
print(f"There are {number_of_samples} samples in this dataset.")

print(f"The dataset contains next organisms: {df["organism"].unique()}")

mean = round(df["length"].mean(), 2)
print(f"=========\nThe mean length of all samples is {mean} b.p.")

print("=========\nEscherichia coli samples")
print(df[df["organism"] == "Escherichia coli"])

print("=========\nSamples with GC content > 42 and length > 1000")
print(df[(df["gc_content"] > 42) & (df["length"] > 1000)])

print("=========\nTOP-3 samples by GC content")
print(df.sort_values("gc_content", ascending=False).head(3))

df["length_kb"] = df["length"]/1000


