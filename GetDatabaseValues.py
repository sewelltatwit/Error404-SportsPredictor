import pyodbc;
def getQuaterback(team):
    #get the quaterback's overall and return it
    overall = pullFromDatabase(team, 'QB', '1')
    print(overall)
    return overall
def getRunningBacks(team):
    overall = pullFromDatabase(team, 'HB', '2')
    print(overall)
    return overall;
def getOffensiveLine(team):
    overall = pullFromDatabase(team, 'WR')
    print(overall)
    return overall
def getWideRecievers(team):
    overall = pullFromDatabase(team, 'WR', 3) + pullFromDatabase(team, 'TE', 2)
    return overall/2
def getRunDefense(team):
    overallMLB = pullFromDatabase(team,'MLB')
    overallROLB = pullFromDatabase(team,'ROLB')
    overallLOLB = pullFromDatabase(team,'LOLB')
    overallRE = pullFromDatabase(team,'RE')
    overallLE = pullFromDatabase(team,'LE')
    overallDT = pullFromDatabase(team,'DT')
    overall = overallDT + overallLE + overallLOLB + overallMLB + overallRE + overallROLB
    print(overall/6)
    return overall/6
def getPassDefense(team):
    overallCB = pullFromDatabase(team, 'CB')
    overallFS = pullFromDatabase(team,'FS')
    overallSS = pullFromDatabase(team, 'SS')
    overall = (overallCB + overallFS + overallSS)/3
    print (overall)
def getStrengthOfTeam(list):
    overall = 0;
    return overall

def pullFromDatabase(team, pos, amount):
    if(amount == 0):
        sqlCommand = "SELECT overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "'"
    else:
        sqlCommand = "SELECT TOP " + amount + " overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "'"

    pyodbc.drivers()
    conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                          'Server=localhost;'
                          'Database=NFL_Players;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(sqlCommand)
    final = 0;
    for row in cursor:
        final = final + row[0]

    sqlCommandCount = "SELECT Count(*) from dbo.Players where Team = '" + team + "' and Position = '" + pos + "'"
    cursor.execute(sqlCommandCount)
    for row in cursor:
        total = row[0]
    if(amount == 0):
        final/total
    else:
        final/int(amount)
    return final
    
getRunningBacks("Cardinals")