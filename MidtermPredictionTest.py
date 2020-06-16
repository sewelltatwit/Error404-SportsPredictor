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
    if ('@' in teamTwoChosen):
        teamTwoChosen = '@' + ((teamTwoChosen.replace('@', '').lower()).capitalize())
    else:
        teamTwoChosen = (teamTwoChosen.lower()).capitalize()
    percent = prediction(team1Chosen, teamTwoChosen)
    index = teamOneSchedule.index(teamTwoChosen) + 1
    if('@' in teamTwoChosen):
        #if Percent[0] > [1] then team one won else team two won
        StoreResults( teamTwoChosen.replace('@', ''),team1Chosen, str(index), percent[1] > percent[0])
    else:
        StoreResults(team1Chosen, teamTwoChosen, str(index), percent[0] > percent[1])
    CheckBaseLine(percent, team1Chosen, "Week_" + str(index))
    
main()