from GetDatabaseValues import *
def prediction(team1, team2):
    #Inital score and percentage of matchup
    percentage = [50, 50]
    score = [0, 0]
    winner = []
    #If the second team is the bye week, then team one does not play anyone
    #Will return message
    if(team2 == "BYE"):
        return ["Can not display result for bye week",""]
    
    #Gains home field advantage in percentage to win
    if('@' in team2):
        percentage[0] = percentage[0] - 2
        percentage[1] = percentage[1] + 2
        isHome = False
        team2 = team2.replace('@', '')
    else:
        isHome = True
        percentage[1] = percentage[1] - 2
        percentage[0] = percentage[0] + 2
        
    #Check to see if the results have been stored
    #If stored, then pulls results instead of running prediction
    if(isHome):
        storedWinner = CheckResults(team1, team2, "PredictedWinner")
        storedScore = CheckResults(team1, team2, "PredictedScore")
        storedMessage = CheckBaseMessage(team1, team2)
        if(storedWinner != None):
            winner = [storedWinner + "\t Score: " + storedScore, storedMessage]
            return winner
    else:
        storedWinner = CheckResults(team2, team1, "PredictedWinner")
        storedScore = CheckResults(team2, team1, "PredictedScore")
        storedMessage = CheckBaseMessage(team2, team1)
        if(storedWinner != None):
            winner = [storedWinner + "\t Score: "+ storedScore, storedMessage]
            return winner
    
    #Overalls of each major part for team one
    team1Strength = [getQuaterback(team1),getRunningBacks(team1), getOffensiveLine(team1), getWideRecievers(team1), getRunDefense(team1), getPassDefense(team1)]
    strength1 = getStrengthOfTeam(team1Strength)
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

    #Overalls of each major part for team two
    team2Strength = [getQuaterback(team2), getRunningBacks(team2), getOffensiveLine(team2), getWideRecievers(team2), getRunDefense(team2), getPassDefense(team2)]     
    strength2 = getStrengthOfTeam(team2Strength)
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
   
    #Checks overall team strength to each other
    percentage = CheckMatchup(strength1, strength2, percentage, abs(strength1-strength2))
    score = UpdateScore(strength1, strength2, score)
    
    #RunningBacks vs Run Defense
    percentage = CheckMatchup(minorRun1, runDefense2, percentage, 1)
    percentage = CheckMatchup(runDefense1, minorRun2, percentage, 1)
    
    #Offensive Line vs Run Defense
    percentage = CheckMatchup(majorRun1, runDefense2, percentage, 2)
    percentage = CheckMatchup(runDefense1, majorRun2, percentage, 2)
    
    #RunningBacks and Offensive Line vs Run Defense
    percentage = CheckMatchup(avgRun1, runDefense2, percentage, 1.5)
    percentage = CheckMatchup(runDefense1, avgRun2, percentage, 1.5)
    score = UpdateScore(avgRun1, runDefense2, score)
    score = UpdateScore(runDefense1, avgRun2, score)
    
    #Wide Recievers vs Pass Defense
    percentage = CheckMatchup(minorPass1, passDefense2, percentage, 1)
    percentage = CheckMatchup(passDefense1, minorPass2, percentage, 1)
    
    #Quaterbacks vs Pass Defense
    percentage = CheckMatchup(majorPass1, passDefense2, percentage, 1.6)
    percentage = CheckMatchup(passDefense1, majorPass2, percentage, 1.6)
    
    #Quaterbacks and Wide Recievers vs Pass Defense
    percentage = CheckMatchup(avgPass1, passDefense2, percentage, 1.3)
    percentage = CheckMatchup(passDefense1, avgPass2, percentage, 1.3)
    
    #Quaterbacks, Wider Recievers, Offensive Line vs Run and Pass Defense
    percentage = CheckMatchup(avgQBR1, avgDefense2, percentage, 2)
    percentage = CheckMatchup(avgDefense1, avgQBR2, percentage, 2)
    score = UpdateScore(avgQBR1, avgDefense2, score)
    score = UpdateScore(avgDefense1, avgQBR2, score)

    #Organizes the score to show hometeam first
    if(isHome):
        finalResult = str(score[0]) + "-" + str(score[1])
    else:
        finalResult = str(score[1]) + "-" + str(score[0])
        
    #Stores and displays the results
    if percentage[0] > percentage[1]:
        if(isHome):
            StoreResults(team1, team2, team1 +" has a " + str(round(percentage[0], 2)) + "% chance to win.", "PredictedWinner")
            StoreResults(team1, team2, finalResult, "PredictedScore")
            baselineMessage = CheckBaseLine(team1, team2, team1)
        else:
            StoreResults(team2, team1, team1 +" has a " + str(round(percentage[0], 2)) + "% chance to win.", "PredictedWinner")
            StoreResults(team2, team1, finalResult, "PredictedScore")
            baselineMessage = CheckBaseLine(team2, team1, team1)

        return [team1 + " has a " + str(round(percentage[0], 2)) + "% chance to win. \t Score: "+ finalResult, baselineMessage]
    else:
        if(isHome):
            StoreResults(team1, team2, team2 +" has a " + str(round(percentage[1], 2)) + "% chance to win.", "PredictedWinner")
            StoreResults(team1, team2, finalResult, "PredictedScore")
            baselineMessage = CheckBaseLine(team1, team2, team2)
        else:
            StoreResults(team2, team1, team2 +" has a " + str(round(percentage[1], 2)) + "% chance to win.", "PredictedWinner")
            StoreResults(team2, team1, finalResult, "PredictedScore")
            baselineMessage = CheckBaseLine(team2, team1, team2)
        
        return [team2 +" has a "+ str(round(percentage[1], 2)) + "% chance to win. \t Score: "+ finalResult, baselineMessage]

#Will update the score based on who has higher overall
def UpdateScore(team1, team2, score):
    if(team1 > team2 and (team1-team2) < 5):
        score[0] += 3
    elif(team1 < team2 and (team2-team1) < 5):
        score[1] += 3
    elif(team1 > team2 and (team1-team2) >= 5):
        score[0] += 7
    elif(team2 > team1 and (team2-team1) >= 5):
        score[1] += 7
    return score

#Will update the percentage based on who has higher overall
def CheckMatchup(team1, team2, percent, difference):
    if(team1 > team2):
        percent[1] = percent[1] - difference
        percent[0] = percent[0] + difference
    else:
        percent[1] = percent[1] + difference
        percent[0] = percent[0] - difference
    return percent