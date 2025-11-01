import pandas as pd

def summarize_add(df3,i):
    df1=pd.read_csv("summarize.csv")
    fail=len(df3[df3["Win"]!=df3["Actual_Win"]])/len(df3)
    success=len(df3[df3["Win"]==df3["Actual_Win"]])/len(df3)
    print("Year",i,"Suceess:",success*len(df3),"Fail:",fail*len(df),"LEngth:",len(df3))
    data={
        "Year": [i],
        "Success(%)": [success*100],
        "Failure(%)": [fail*100],
    }
    df2=pd.DataFrame(data)
    df2.to_csv("Summarize.csv",mode='a',header=False,index=False)

df_main=pd.read_csv("Probs.csv")
df_main2=pd.read_csv("set2.csv")

df_main["team1_O"]=df_main2["team1"]
df_main["team2_O"]=df_main2["team2"]
df_main["Actual_Win"]=df_main2["winner"]
df_main["Win_Prob"]=df_main["Win_Prob"]*100
df_main.to_csv("Probs.csv",mode='w')

df=pd.read_csv("Probs.csv")
print(df["Year"].unique())
for i in df["Year"].unique():
    df1=df[df["Year"]==i]
    summarize_add(df1,i)
