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
            
def StoreResults(teamHome, teamAway, winner, prediction):
    sqlCommand = "UPDATE dbo.Game SET " + prediction + " = '" + winner + "' WHERE HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "'"
    SetValues(sqlCommand)
    
def CheckResults(teamHome, teamAway, predicted):
    sqlCommand = "Select " + predicted + " FROM dbo.Game where HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "'"
    cursor = ExecuteQuery(sqlCommand)
    result = ''
    for row in cursor:
        result = row[0]
    #print(result) 
    return result



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
    
#CheckResults("Bears", "Packers")