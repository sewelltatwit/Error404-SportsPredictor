from flask import Flask, request, render_template
from SQLQueries import *
app = Flask(__name__, template_folder='/Users/daobr/Documents/VSCodePy/Error404-SportsPredictor')
app.debug = True

@app.route('/', methods=["GET", "POST"])
#@app.route('/populateTeamOne', methods=["GET"])
def populateTeamOne():
    allTeams = pullTeamsFromDatabase('dbo.Schedule')
    return render_template("SportsPredictorUI.html",
                           server_list=allTeams)
if __name__ == "__main__":
    app.run()