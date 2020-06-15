import pyodbc;
from Prediction import  *

def pullTeamsFromDatabase(databaseName):
    
    sqlCommand = "SELECT Team from " + databaseName

    pyodbc.drivers()
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=localhost;'
                          'Database=NFL_Players;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    teamNames = []
    for row in cursor:
        teamNames.append(row[0])


    return teamNames


def pullScheduleFromDatabase(databaseName, teamName):
    sqlCommand = "SELECT * from " + databaseName + " where Team = '" + teamName + "'"
    pyodbc.drivers()
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=localhost;'
                          'Database=NFL_Players;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    teamNames = []
    for row in cursor:
        for opp in row:
            #if(opp != teamName):
                #teamNames.append(opp)
            teamNames.append(opp)
        print(teamNames)

    return teamNames
