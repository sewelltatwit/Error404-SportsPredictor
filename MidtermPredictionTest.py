from Prediction import *
from SQLQueries import *
def main():
    allTeams = pullTeamsFromDatabase("dbo.Schedule")
    print(allTeams)
    team1Chosen = input("Enter the first team: ")
    team1Chosen = (team1Chosen.lower()).capitalize()
    teamOneSchedule = pullScheduleFromDatabase("dbo.Schedule", team1Chosen)
    print(teamOneSchedule)
    teamTwoChosen = input("Select the second team: ")
    teamTwoChosen = (teamTwoChosen.lower()).capitalize()
    percent = prediction(team1Chosen, teamTwoChosen)
    index = teamOneSchedule.index(teamTwoChosen) + 1
    CheckBaseLine(percent, team1Chosen, "Week_" + str(index))
    
main()