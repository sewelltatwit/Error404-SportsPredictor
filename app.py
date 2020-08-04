from flask import Flask, request, render_template, jsonify
from SQLQueries import *
from Prediction import *
app = Flask(__name__)

app.config['SESSION_COOKIE_SECURE'] = False
#Will initally populate the website with the teams in the first dropdown
@app.route('/')
def populateTeamOne():
    allTeams = pullTeamsFromDatabase('dbo.Schedule')
    return render_template("SportsPredictorUI.html",
                           Team1=allTeams)

#Schedule for each team is stored in the html page
@app.route('/getSchedule/<TeamOneValue>')
def getSchedule(TeamOneValue):
    return jsonify(pullScheduleFromDatabase(TeamOneValue))

#Final result for each team matchup is stored in the html page
@app.route('/finalResult/<TeamOne>/<TeamTwo>')       
def storeResult(TeamOne, TeamTwo):
    return jsonify(prediction(TeamOne, TeamTwo))

#Runs flask to get main website
if __name__ == "__main__":
    app.run()