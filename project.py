import xmlsoccer
import pandas as pd
import time


## http://www.xmlsoccer.com/FootballDataDemo.asmx


#%% Call API
xmls = xmlsoccer.XmlSoccer(api_key = "CJLWGIFMFFDGRIXTRUFZHLFXPNDQAKSONGUOPRIZCKVAHDIERJ" , use_demo=True)

#%% Check Spam or API_key
#xmls.call_api(method='CheckApiKey')
xmls.call_api(method='IsMyApiKeyPutOnSpammersList')

    
#%% Load Teams and players

#Teams = xmls.call_api(method='GetAllTeams')

#df_team = pd.DataFrame(Teams)

df_team = pd.read_pickle('team.pickle')

df_players = pd.DataFrame()

for i in df_team.Team_Id:
    time.sleep(20)
    temp = pd.DataFrame(xmls.call_api(method='GetAllTeams', teamId = i))
    df_players = pd.concat([df_players, temp])
    
print(df_players)



#%% 
df_players.to_pickle('players.pickle')

#%% List of seasons

season_list = []
for i in range(17):
    temp = format(i, '02d') + format(i+1, '02d')
    season_list.append(temp)
    
print(season_list)

#%% Load list of past games
season_list = ['1516', '1415']

df_Hist_Matches = pd.DataFrame()

for season in season_list:
    time.sleep(16)
    
    temp = pd.DataFrame(xmls.call_api(method='GetHistoricMatchesByLeagueAndSeason',
                                             seasonDateString = season,
                                             league='Scottish Premier League'))
    df_Hist_Matches = pd.concat([df_Hist_Matches, temp])
    
print(df_Hist_Matches)
    
#%% Load list of fixtures games
season_list = ['1516', '1415']

df_Fixtures = pd.DataFrame()

for season in season_list:
    time.sleep(16)
    
    temp = pd.DataFrame(xmls.call_api(method='GetFixturesByLeagueAndSeason',
                                             seasonDateString = season,
                                             league='Scottish Premier League'))
    df_Fixtures = pd.concat([df_Fixtures, temp])
    
print(df_Fixtures)

#%% Export to csv
df_Fixtures.to_csv('Fixtures.csv')

df_Hist_Matches.to_csv('Hist_Matches.csv')

df_players = pd.read_pickle('players.pickle')
df_players.to_csv('Players.csv')

df_team = pd.read_pickle('team.pickle')
df_team.to_csv('Teams.csv')