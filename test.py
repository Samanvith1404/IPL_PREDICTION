import pandas as pd

df=pd.read_csv("Probs.csv")
df["BOOL_DATA"]=(df["Win"]==df["Actual_Win"])
df.to_csv("prob2.csv")