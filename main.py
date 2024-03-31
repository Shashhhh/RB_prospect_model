import pandas as pd
from IPython.display import display
df_2014 = pd.read_csv('2014.csv')
df_2015 = pd.read_csv('2015.csv')
df_2016  = pd.read_csv('2016.csv')
df_2017  = pd.read_csv('2017.csv')
df_2018  = pd.read_csv('2018.csv')
df_2019  = pd.read_csv('2019.csv')
df_2020  = pd.read_csv('2020.csv')
df_2021 = pd.read_csv('2021.csv')
df_2022 = pd.read_csv('2022.csv')
df_2023 = pd.read_csv('2023.csv')

df_2014['Year'] = 2014
df_2015['Year'] = 2015
df_2016['Year']  = 2016
df_2017['Year']  = 2017
df_2018['Year']  = 2018
df_2019['Year']  = 2019
df_2020['Year']  = 2020
df_2021['Year'] = 2021
df_2022['Year'] = 2022
df_2023['Year'] = 2023
#Concat csv into one
fantasy_df = pd.concat([df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022, df_2023], ignore_index=True)
#Drops unnamed col
fantasy_df.drop(fantasy_df.columns[0], axis=1, inplace=True)
fantasy_df = fantasy_df.rename(columns={'Player': 'Name'})
#Gets all RB data
fantasy_df = fantasy_df[fantasy_df['Pos']== 'RB']
#Gets rid of * in RB names
fantasy_df['Name'] = fantasy_df['Name'].str.replace('*', '')
display(fantasy_df)
#Captures RB fantasy points
RB_fantasy = fantasy_df[['Name','FantasyPoints', 'Year', 'G']]
RB_names = RB_fantasy['Name'].unique()







RAS_df = pd.read_csv('RAS_scores_2.csv')
RAS_df.drop(RAS_df.columns[0], axis = 1, inplace=True)
RAS_df.drop(RAS_df.columns[-1], axis = 1, inplace=True)

display(RAS_df)

main_df = pd.merge(RAS_df, RB_fantasy, on=['Name','Year'])
main_df['PPG'] = main_df['FantasyPoints'] / main_df['G']
main_df = main_df[main_df['G'] >= 6]
main_df = main_df.round(decimals=2)

display(main_df)






draft_2014 = pd.read_csv('2014_draft.csv')
draft_2015 = pd.read_csv('2015_draft.csv')
draft_2016  = pd.read_csv('2016_draft.csv')
draft_2017  = pd.read_csv('2017_draft.csv')
draft_2018  = pd.read_csv('2018_draft.csv')
draft_2019  = pd.read_csv('2019_draft.csv')
draft_2020  = pd.read_csv('2020_draft.csv')
draft_2021 = pd.read_csv('2021_draft.csv')
draft_2022 = pd.read_csv('2022_draft.csv')
draft_2023 = pd.read_csv('2023_draft.csv')

draft_2014['Year'] = 2014
draft_2015['Year'] = 2015
draft_2016['Year'] = 2016
draft_2017['Year'] = 2017
draft_2018['Year'] = 2018
draft_2019['Year'] = 2019
draft_2020['Year'] = 2020
draft_2021['Year'] = 2021
draft_2022['Year'] = 2022
draft_2023['Year'] = 2023

draft_df = pd.concat([draft_2014, draft_2015, draft_2016, draft_2017, draft_2018,
                             draft_2019, draft_2020, draft_2021, draft_2022, draft_2023])

draft_df.reset_index(drop=True, inplace=True)
draft_df = draft_df[['Name', 'Year', 'Overall', 'PreDraftGrade']]
display(draft_df)