from flask import Flask
from markupsafe import escape
from nba_api.stats.endpoints import teamdetails, commonteamroster, playercareerstats
import pandas as pd
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/team/<teamname>')
def show_team_profile(teamname):
    # show the team profile for that team
    return 'team %s' % escape(teamname)

@app.route('/teamDetails/<team_id>')
def show_team_details(team_id):
    teamDetails =teamdetails.TeamDetails(team_id=team_id).get_data_frames()
    jsonfrTeamDetails = pd.DataFrame(teamDetails).to_json(orient = 'records')
    # show the team profile for that team
    return jsonfrTeamDetails

@app.route('/teamRoster/<team_id>/<year>')
def show_team_roster(team_id, year):
    teamRoster = commonteamroster.CommonTeamRoster(team_id=team_id, season=year).get_data_frames()
    jsonfrTeamRoster = pd.DataFrame(teamRoster).to_json(orient = 'records')
    # show the team profile for that team
    
    return jsonfrTeamRoster

 
@app.route('/playerCareerStats/<player_id>')
def show_player_career_stats(player_id):
    playerCareerStats = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()   
    jsonfrPlayerCareerStats = pd.DataFrame(playerCareerStats).to_json(orient = 'records')
    # show the team profile for that team
    
    return jsonfrPlayerCareerStats
       

 



