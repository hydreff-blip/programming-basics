file0 = open("data/samples.csv")

import pandas as pd

df = pd.read_csv("data/samples.csv")
#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.describe())

#print(df[["sample", "gc_content"]])

#print(df[df["organism"] == "Escherichia coli"])

print(df.sort_values("gc_content"))

df["gc_rich"] = df["gc_content"] > 45

print(df[["gc_content", "gc_rich"]])
print (df[df["gc_rich" == True]])

