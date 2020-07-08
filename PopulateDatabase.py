from flask import Flask, request, render_template, jsonify
from SQLQueries import *
app = Flask(__name__, template_folder='/Users/daobr/Documents/VSCodePy/Error404-SportsPredictor')
app.debug = True
app.config['SESSION_COOKIE_SECURE'] = False
@app.route('/')
def populateTeamOne():
    allTeams = pullTeamsFromDatabase('dbo.Schedule')
    return render_template("SportsPredictorUI.html",
                           Team1=allTeams)

@app.route('/getSchedule/<TeamOneValue>')
def getSchedule(TeamOneValue):
    return jsonify(pullScheduleFromDatabase(TeamOneValue))

        
        
if __name__ == "__main__":
    app.run()