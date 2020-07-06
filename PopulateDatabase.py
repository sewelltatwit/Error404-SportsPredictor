from flask import Flask, request, render_template
from SQLQueries import *
app = Flask(__name__, template_folder='/Users/daobr/Documents/VSCodePy/Error404-SportsPredictor')
app.debug = True

@app.route('/', methods=["GET", "POST"])
@app.route('/Team1', methods=["GET"])
def populateTeamOne():
    allTeams = pullTeamsFromDatabase('dbo.Schedule')
    return render_template("SportsPredictorUI.html",
                           Team1=allTeams)

@app.route('/', methods=["GET", "POST"])
@app.route("/Team2", methods=["POST"])
def populateTeamTwo():
    TeamOneValue = request.form("Team1")
    if request.method == "POST":
        if TeamOneValue != None:
            TeamOneSchedule = pullScheduleFromDatabase(TeamOneValue)
            print(TeamOneSchedule)
            return render_template("SportsPredictorUI.html", Team2= TeamOneSchedule)
    return render_template("SportsPredictorUI.html")
        
        
        
        
if __name__ == "__main__":
    app.run()