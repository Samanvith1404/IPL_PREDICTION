import pandas as pd
import numpy as np

import numpy as np

df=pd.read_csv("set2.csv")
s1=df["season"].unique()


def ALGO(df_curr,df_overall,teamA,teamB):
  A1=df_overall[teamA]
  B1=df_overall[teamB]
  A2=df_curr[teamA]
  B2=df_curr[teamB]
  prob_overall=A1-B1
  prob_curr=A2-B2
  prob_tot=(prob_overall+prob_curr)/2
  if len(prob_tot[prob_tot>0])>len(prob_tot[prob_tot<0]):
    return (teamA,len(prob_tot[prob_tot>0])/len(prob_tot))
  else:
    return (teamB,len(prob_tot[prob_tot<0])/len(prob_tot))


def ALGO_MAIN(i,dp,total_table,df_curr):
  df1=dp
  df2=pd.DataFrame(np.zeros((len(df1),5)),columns=["Year","team1","team2","Win_Prob","Win"],index=df1.index)
  for index, row in df1.iterrows():
    team_A=row["team1"]
    team_B=row["team2"]
    df2.loc[index,"Year"]=i
    df2.loc[index,"team1"]=team_A
    df2.loc[index,"team2"]=team_B
    win_team, win_prob = ALGO(df_curr,total_table,team_A,team_B)
    df2.loc[index,"Win_Prob"]= win_prob
    df2.loc[index,"Win"]= win_team
    df_curr.loc[team_A,team_B]=win_prob*100
    df_curr.loc[team_B,team_A]=(1-win_prob)*100
  df2.to_csv("Probs.csv",mode='a',header=False,index=False)

def table_form(df):
    t_union = sorted(list(pd.concat([df["team1"], df["team2"]]).unique()))
    dp = pd.DataFrame(np.zeros((len(t_union), len(t_union))), index=t_union, columns=t_union)

    for team_A in t_union:
        for team_B in t_union:
            if team_A == team_B:
                dp.loc[team_A, team_B] = 100.0
            else:
                matches_A_vs_B = df[(df["team1"] == team_A) & (df["team2"] == team_B)]
                matches_B_vs_A = df[(df["team1"] == team_B) & (df["team2"] == team_A)]

                all_common_match_indices = matches_A_vs_B.index.union(matches_B_vs_A.index)
                common_matches_df = df.loc[all_common_match_indices]

                total_matches_played = len(common_matches_df)

                if total_matches_played > 0:
                    wins_team_A = len(common_matches_df[common_matches_df["winner"].str.lower() == team_A.lower()])
                    win_percent_A = (wins_team_A / total_matches_played) * 100

                    wins_team_B = len(common_matches_df[common_matches_df["winner"].str.lower() == team_B.lower()])
                    win_percent_B = (wins_team_B / total_matches_played) * 100

                    dp.loc[team_A, team_B] = win_percent_A
                    dp.loc[team_B, team_A] = win_percent_B
                else:
                    dp.loc[team_A, team_B] = 0.0
                    dp.loc[team_B, team_A] = 0.0
    return dp



mp={}
print(df)
for i in s1:
    mp[i]=df[df["season"]==i]

total_table1=[table_form(mp[2018])]

all_teams = sorted(list(pd.concat([df["team1"], df["team2"]]).unique()))


for i in mp:
     if i != 2018: total_table1.append(table_form(mp[i]))
     total_table=sum(total_table1)/len(total_table1)
     array=np.full((len(all_teams), len(all_teams)),50.00)
     arrau=np.fill_diagonal(array,100.00)
     df_curr = pd.DataFrame(array, index=all_teams, columns=all_teams)
     ALGO_MAIN(i,mp[i],total_table,df_curr)


total_table=total_table.dropna(how='all')
total_table=total_table.dropna(how='all',axis=1)
for i in total_table1:
   print(i)
   print()
print("Total_Table1:")
print(total_table)
print("DF_CURR:")
print(df_curr)