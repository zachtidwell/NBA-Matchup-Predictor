import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats, leaguestandings, commonteamroster
import time


# This python script will create 3 .csv files in the current working directory
# It will create 'nba-stats.csv', 'nba-standings.csv', and 'nba_rosters.csv'
# Built using 'nba_api' created by Swar Patel
# https://github.com/swar/nba_api


# Get all the teams
nba_teams = teams.get_teams()

# initialize a list for all the rosters dataframes
rosters = []

# Loop through each team and get their season stats, and rosters
for team in nba_teams:
    team_id = team['id']
    team_name = team['full_name']

    # Sleeping as to not overload the api
    time.sleep(.600)
    # Retrieve team season stats
    team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id, season='2022-23')
    team_stats_df = team_stats.get_data_frames()[0]

    # Sleeping as to not overload the api
    time.sleep(.600)
    # Retrieve team rosters
    team_rosters = commonteamroster.CommonTeamRoster(team_id, season='2022-23')
    team_rosters_df = team_rosters.get_data_frames()[0]
    # Add a column 'TEAM' and fill with team_name
    team_rosters_df['TEAM'] = team_name
    # Add each roster to the roster list
    rosters.append(team_rosters_df)

# Concatenate each roster to the final dataframe
team_rosters_df = pd.concat(rosters)

# Retrieve the league standings of each team
team_standings = leaguestandings.LeagueStandings(season='2022-23')
team_standings_df = team_standings.get_data_frames()[0]

# Converting each dataframe into a .csv file and sending to current directory
team_stats_df.to_json('nba-stats.json', orient='records')
team_standings_df.to_json('nba-standings.json', orient='records')
team_rosters_df.to_json('nba-rosters.json', orient='records')
