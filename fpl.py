import time
import datetime
import pandas as pd

#location from where data are scrapped 
#thanks to Fantasy Premier league
dfs = pd.read_html("https://fantasy.premierleague.com/player-list/", header =0)

#goalkeeper
gk1 = dfs[0]
gk2 = dfs[1]
gk = [gk1,gk2]
f_gk = pd.concat(gk)
f_gk["Position"] = "Goalkeepers"
f_gk = f_gk.sort_values(by=["Points", "Cost"], ascending = [False,True])
f_gk = f_gk.reset_index(drop=True)

#defender
df1 = dfs[2]
df2 = dfs[3]
df = [df1,df2]
f_df = pd.concat(df)
f_df["Position"] = "Defenders"
f_df = f_df.sort_values(by=["Points", "Cost"], ascending = [False,True])
f_df = f_df.reset_index(drop=True)

#midfielder
mf1 = dfs[4]
mf2 = dfs[5]
mf = [mf1,mf2]
f_mf = pd.concat(mf)
f_mf["Position"] = "Midfielders"
f_mf = f_mf.sort_values(by=["Points", "Cost"], ascending = [False,True])
f_mf = f_mf.reset_index(drop=True)

#forward
fw1 = dfs[6]
fw2 = dfs[7]
fw = [fw1,fw2]
f_fw = pd.concat(fw)
f_fw["Position"] = "Forwards"
f_fw = f_fw.sort_values(by=["Points", "Cost"], ascending = [False,True])
f_fw = f_fw.reset_index(drop=True)

#combining everyone
pattern = [f_fw,f_mf,f_df,f_gk]
fpl = pd.concat(pattern)
fpl_data = fpl.reset_index(drop=True)

now = datetime.datetime.now()
fname = now.strftime("%d_%B%Y")
fpl_data.to_csv(fname + '.csv')
print("A file named '"+ fname +"' is created where you saved the code.")
print("enjoy")

