import pyodbc;

def pullTeamsFromDatabase(databaseName):
    
    sqlCommand = "SELECT Team from " + databaseName

    cursor = ExecuteQuery(sqlCommand)
    teamNames = []
    for row in cursor:
        teamNames.append(row[0])

    return teamNames

def pullScheduleFromDatabase(teamName):
    sqlCommand = "SELECT * from dbo.Schedule where Team = '" + teamName + "'"
    cursor = ExecuteQuery(sqlCommand)
    teamNames = []
    for row in cursor:
        for opp in row:
            if(opp != teamName):
                teamNames.append(opp)
    return teamNames

def pullFromDatabase(team, pos, amount):
    if(amount == 0):
        sqlCommand = "SELECT overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "'"
    else:
        sqlCommand = "SELECT TOP " + amount + " overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "' order by overall desc"

    cursor = ExecuteQuery(sqlCommand)
    final = 0;
    for row in cursor:
        final = final + row[0]

    for row in cursor:
        total = row[0]

    return final/float(amount)

def CheckBaseLine(percentage, team, weekNum):
    sqlCommand = "SELECT " + weekNum + " from dbo.BaseLine where Team = '" + team + "'"
    cursor = ExecuteQuery(sqlCommand)
    for row in cursor:
        if(percentage[0] < percentage[1] and (row[0] == 'L')):
            print("Predicted Loss Correct!")
        elif (percentage[0] > percentage[1] and (row[0] == 'W')):
            print("Predicted Win Correct!")
        else:
            print("Prediction Incorrect!")
            
def StoreResults(teamHome, teamAway, weekNum, winner):
    if(winner):
        sqlCommand = "UPDATE dbo.Game SET PredictedWinner = '" + teamHome + "' WHERE HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "' AND Week = '" + weekNum + "'"  
    else:
        sqlCommand = "UPDATE dbo.Game SET PredictedWinner = '" + teamAway + "' WHERE HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "' AND Week = '" + weekNum + "'"  

    SetValues(sqlCommand)
    print('Stored results!')
    cursor = ExecuteQuery("SELECT * from dbo.Game WHERE HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "' AND Week = '" + weekNum + "'")
    for row in cursor:
        print(row)

#StoreResults('Cardinals', 'Lions', '1')
def ExecuteQuery(sqlCommand):
    pyodbc.drivers()
    #conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
    #                      'Server=localhost;'
    #                      'Database=NFL_Players;'
    #                      'Trusted_Connection=yes;')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=sports-predictor.database.windows.net;'
                        'Database=SportsPredictor;'
                        'UID=server;'
                        'PWD=SeniorProject2020;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    return cursor

def SetValues(sqlCommand):
    pyodbc.drivers()
    #conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
    #                      'Server=localhost;'
    #                      'Database=NFL_Players;'
    #                      'Trusted_Connection=yes;')
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=sports-predictor.database.windows.net;'
                        'Database=SportsPredictor;'
                        'UID=server;'
                        'PWD=SeniorProject2020;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    conn.commit()