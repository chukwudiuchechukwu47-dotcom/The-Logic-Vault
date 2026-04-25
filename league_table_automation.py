import pandas as pd

path = "epl-2025-GMTStandardTime.csv" 
df = pd.read_csv(path)
print(df)

df_played = df.dropna(subset=['Result'])
df_played[['Home_Goals', 'Away_Goals']] = df_played['Result'].str.split(' - ', expand=True).astype(int)

print("\n"+"=" * 70)
print(df_played[['Home Team', 'Away Team', 'Result', 'Home_Goals', 'Away_Goals']])
print("=" * 70)

def get_Pts(row):
    if row['Home_Goals'] > row['Away_Goals']:
       return 3, 0
    elif row['Away_Goals'] > row['Home_Goals']:
       return 0, 3
    else:
       return 1, 1
    
    
df_played[['Home_Pts', 'Away_Pts']] = df_played.apply(get_Pts, axis=1, result_type='expand')
print(df_played[['Home Team', 'Away Team', 'Result', 'Home_Pts', 'Away_Pts']])
print("=" * 70)

home_stats = pd.DataFrame({
   'Team': df_played['Home Team'],
   'GF': df_played['Home_Goals'],
   'GA': df_played['Away_Goals'],
   'Pts': df_played['Home_Pts']
})

Away_stats = pd.DataFrame({
   'Team': df_played['Away Team'],
   'GF': df_played['Away_Goals'],
   'GA': df_played['Home_Goals'],
   'Pts': df_played['Away_Pts']
})

all_stats = pd.concat([home_stats, Away_stats], ignore_index=True)
print(all_stats)

league_table = all_stats.groupby('Team').agg({
    'GF': 'sum',  
    'GA': 'sum', 
    'Pts': 'sum'   
}).reset_index()

league_table['GD'] = league_table['GF'] - league_table['GA']

league_table = league_table.sort_values(by=['Pts', 'GD'], ascending=False).reset_index(drop=True)
league_table.index = league_table.index + 1

print("\n" + " FINAL EPL 2025 LEAGUE TABLE ".center(70, "="))
print(league_table)
print("=" * 70)

