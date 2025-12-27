import pandas as pd

df=pd.read_csv("set1.csv")
print(df)
s1=df["season"].unique()
mp={}
df["season"]=df["season"].astype(str)

df["season"]=df["season"].astype(int)
df=df[df["season"]>2017]

df["team1"]=df["team1"].str.replace("Royal Challengers Bengaluru","RCB",regex=False)
df["team1"]=df["team1"].str.replace("Royal Challengers Bangalore","RCB",regex=False)
df["team1"]=df["team1"].str.replace("Chennai Super Kings","CSK",regex=False)
df["team1"]=df["team1"].str.replace("Gujarat Titans","GT",regex=False)
df["team1"]=df["team1"].str.replace("Mumbai Indians","MI",regex=False)
df["team1"]=df["team1"].str.replace("Kolkata Knight Riders","KKR",regex=False)
df["team1"]=df["team1"].str.replace("Delhi Capitals","DC",regex=False)
df["team1"]=df["team1"].str.replace("Delhi Daredevils","DC",regex=False)
df["team1"]=df["team1"].str.replace("Rajasthan Royals","RR",regex=False)
df["team1"]=df["team1"].str.replace("Sunrisers Hyderabad","SRH",regex=False)
df["team1"]=df["team1"].str.replace("Kings XI Punjab","KXIP",regex=False)
df["team1"]=df["team1"].str.replace("Lucknow Super Giants","LSG",regex=False)
df["team1"]=df["team1"].str.replace("Punjab Kings","KXIP",regex=False)

df["team2"]=df["team2"].str.replace("Royal Challengers Bengaluru","RCB",regex=False)
df["team2"]=df["team2"].str.replace("Royal Challengers Bangalore","RCB",regex=False)
df["team2"]=df["team2"].str.replace("Chennai Super Kings","CSK",regex=False)
df["team2"]=df["team2"].str.replace("Gujarat Titans","GT",regex=False)
df["team2"]=df["team2"].str.replace("Mumbai Indians","MI",regex=False)
df["team2"]=df["team2"].str.replace("Kolkata Knight Riders","KKR",regex=False)
df["team2"]=df["team2"].str.replace("Delhi Capitals","DC",regex=False)
df["team2"]=df["team2"].str.replace("Delhi Daredevils","DC",regex=False)
df["team2"]=df["team2"].str.replace("Rajasthan Royals","RR",regex=False)
df["team2"]=df["team2"].str.replace("Sunrisers Hyderabad","SRH",regex=False)
df["team2"]=df["team2"].str.replace("Kings XI Punjab","KXIP",regex=False)
df["team2"]=df["team2"].str.replace("Lucknow Super Giants","LSG",regex=False)
df["team2"]=df["team2"].str.replace("Punjab Kings","KXIP",regex=False)

df["winner"] = df["winner"].str.replace("Royal Challengers Bengaluru","RCB",regex=False)
df["winner"] = df["winner"].str.replace("Royal Challengers Bangalore","RCB",regex=False)
df["winner"] = df["winner"].str.replace("Chennai Super Kings","CSK",regex=False)
df["winner"] = df["winner"].str.replace("Gujarat Titans","GT",regex=False)
df["winner"] = df["winner"].str.replace("Mumbai Indians","MI",regex=False) # Ensure this matches your data
df["winner"] = df["winner"].str.replace("Kolkata Knight Riders","KKR",regex=False)
df["winner"] = df["winner"].str.replace("Delhi Capitals","DC",regex=False)
df["winner"] = df["winner"].str.replace("Delhi Daredevils","DC",regex=False)
df["winner"] = df["winner"].str.replace("Rajasthan Royals","RR",regex=False)
df["winner"] = df["winner"].str.replace("Sunrisers Hyderabad","SRH",regex=False)
df["winner"] = df["winner"].str.replace("Kings XI Punjab","KXIP",regex=False)
df["winner"] = df["winner"].str.replace("Lucknow Super Giants","LSG",regex=False)
df["winner"] = df["winner"].str.replace("Punjab Kings","KXIP",regex=False)

df.to_csv("set2.csv")