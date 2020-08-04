import pyodbc;

#Query to select the teams in the league from the database
def pullTeamsFromDatabase(databaseName):
    sqlCommand = "SELECT Team from " + databaseName
    cursor = ExecuteQuery(sqlCommand)
    teamNames = []
    for row in cursor:
        teamNames.append(row[0])
    return teamNames

#Query to return a list of teams that the "teamName" plays in 2019 season
def pullScheduleFromDatabase(teamName):
    sqlCommand = "SELECT * from dbo.Schedule where Team = '" + teamName + "'"
    cursor = ExecuteQuery(sqlCommand)
    teamNames = []
    for row in cursor:
        for opp in row:
            if(opp != teamName):
                teamNames.append(opp)
    return teamNames

#Query to return average players at a certain position and team
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

#Query to check the final results of actual game vs predicted game
def CheckBaseLine(home, away, results):
    sqlCommand = "SELECT Winner, Score from dbo.BaselineCheck where Home = '" + home + "' and Away = '" + away + "'"
    cursor = ExecuteQuery(sqlCommand)
    actualResult = ''
    for row in cursor:
        if(results == row[0]):
            actualResult = "Predicted Winner Correctly! Actual Score: " + row[1]
        else:
            actualResult = "Predicted Winner Incorrectly! Actual Score: " + row[1]
    StoreBaseline(home, away, actualResult)
    return actualResult

#Query to return message stored in BaselineCheck
def CheckBaseMessage(home, away):
    sqlCommand = "SELECT Message from dbo.BaselineCheck where Home = '" + home + "' and Away = '" + away + "'"
    cursor = ExecuteQuery(sqlCommand)
    message = ''
    for row in cursor:
        message = row[0]
    return message

#Query to store information in the Baseline for reference later
def StoreBaseline(home, away, results):
    sqlCommand = "UPDATE dbo.BaselineCheck SET Message = '" + results + "' WHERE Home = '" + home + "' And Away = '" + away + "'"
    SetValues(sqlCommand)

#Query to store results of matchup
def StoreResults(teamHome, teamAway, winner, prediction):
    sqlCommand = "UPDATE dbo.Game SET " + prediction + " = '" + winner + "' WHERE HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "'"
    SetValues(sqlCommand)

#Query to check the stored results of matchup
def CheckResults(teamHome, teamAway, predicted):
    sqlCommand = "Select " + predicted + " FROM dbo.Game where HomeTeam = '" + teamHome + "' AND AwayTeam = '" + teamAway + "'"
    cursor = ExecuteQuery(sqlCommand)
    result = ''
    for row in cursor:
        result = row[0]
    return result

#Command to connect to the database and run a query
def ExecuteQuery(sqlCommand):
    pyodbc.drivers()
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=sports-predictor.database.windows.net;'
                        'Database=SportsPredictor;'
                        'UID=server;'
                        'PWD=SeniorProject2020;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    return cursor

#Command to connect to the database and set a value
def SetValues(sqlCommand):
    pyodbc.drivers()
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=sports-predictor.database.windows.net;'
                        'Database=SportsPredictor;'
                        'UID=server;'
                        'PWD=SeniorProject2020;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    conn.commit()
    