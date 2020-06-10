from GetDatabaseValues import *
def prediction(team1, team2):
    percentage = [50, 50]
    team1Strength = [getQuaterback(team1),getRunningBacks(team1), getOffensiveLine(team1), getWideRecievers(team1), getRunDefense(team1), getPassDefense(team1)]
    
    f = getStrengthOfTeam(team1Strength)
    
    minorRun1 = team1Strength[1]
    majorRun1 = team1Strength[2]
    avgRun1 = (minorRun1 + majorRun1) /2
    
    minorPass1 = team1Strength[3]
    majorPass1 = team1Strength[0]
    avgPass1 = (minorPass1 + majorPass1) /2
    
    avgQBR1 = (minorPass1 + majorPass1 + majorRun1) /3
    
    runDefense1 = team1Strength[4]
    passDefense1 = team1Strength[5]
    avgDefense1 = (runDefense1 + passDefense1) /2
    print(f)
    team2Strength = [getQuaterback(team2), getRunningBacks(team2), getOffensiveLine(team2), getWideRecievers(team2), getRunDefense(team2), getPassDefense(team2)]
        
    g = getStrengthOfTeam(team2Strength)
    
    minorRun2 = team2Strength[1]
    majorRun2 = team2Strength[2]
    avgRun2 = (minorRun1 + majorRun2) /2
    
    minorPass2 = team2Strength[3]
    majorPass2 = team2Strength[0]
    avgPass2 = (minorPass2 + majorPass2) /2
    
    avgQBR2 = (minorPass2 + majorPass2 + majorRun2) /3
    
    runDefense2 = team2Strength[4]
    passDefense2 = team2Strength[5]
    avgDefense2 = (runDefense2 + passDefense2) /2
    print(g)
    percentage = CheckMatchup(f, g, percentage, abs(f-g))
    for row in percentage:
        print(row)


def CheckMatchup(match1, match2, percent, difference):
    if(match1 > match2):
        percent[1] = percent[1] - difference
        percent[0] = percent[0] + difference
    else:
        percent[1] = percent[1] + difference
        percent[0] = percent[0] - difference
    return percent


prediction("Patriots", "49s")