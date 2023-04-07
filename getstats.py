import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguedashteamstats, commonteamroster, leaguestandings
import time
import json


# This python script will create 1 .json file in the current working directory
# It will create 'nba-data.json'
# Built using 'nba_api' created by Swar Patel
# https://github.com/swar/nba_api

def get_data():
    sleep_timer = 0.600

    # Get all the teams
    nba_teams = teams.get_teams()

    # initialize a dictionary for the data
    data = {}

    # Loop through each team and get their season stats, roster, and standings
    for team in nba_teams:
        team_id = team['id']
        team_name = team['full_name']

        # Sleeping as to not overload the api
        time.sleep(sleep_timer)

        # Retrieve team season stats
        team_stats = leaguedashteamstats.LeagueDashTeamStats(team_id, season='2022-23')
        team_stats_df = team_stats.get_data_frames()[0]
        team_stats_df = team_stats_df[['PTS', 'REB', 'AST', 'STL', 'BLK', 'GP']]
        team_stats_dict = team_stats_df.to_dict('records')[0]

        # Sleeping as to not overload the api
        time.sleep(sleep_timer)

        # Retrieve team roster
        team_roster = commonteamroster.CommonTeamRoster(team_id, season='2022-23')
        team_roster_df = team_roster.get_data_frames()[0]
        team_roster_df = team_roster_df[['PLAYER', 'POSITION', 'NUM', 'HEIGHT', 'WEIGHT', 'AGE', 'BIRTH_DATE', 'SCHOOL']]
        team_roster_dict = team_roster_df.to_dict('records')

        # Sleeping as to not overload the api
        time.sleep(sleep_timer)

        # Retrieve team standings
        team_standings = leaguestandings.LeagueStandings(season='2022-23')
        team_standings_df = team_standings.get_data_frames()[0]
        team_standings_df = team_standings_df.loc[team_standings_df['TeamID'] == team_id]
        team_standings_df = team_standings_df[['Conference', 'PlayoffRank', 'ConferenceRecord', 'ConferenceGamesBack', 'L10', 'strCurrentStreak']]
        team_standings_dict = team_standings_df.to_dict('records')[0]

        team_dict = {
            'stats': team_stats_dict,
            'roster': team_roster_dict,
            'standings': team_standings_dict
        }
        data[team_name] = team_dict


    # Write data to json file
    with open('nba-data.json', 'w') as f:
        json.dump(data, f)


def main():
    get_data()


if __name__ == "__main__":
    main()
