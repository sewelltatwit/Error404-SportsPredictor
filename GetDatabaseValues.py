import pyodbc;
def getQuaterback(team):
    #get the quaterback's overall and return it
    overall = pullFromDatabase(team, 'QB', '1')
    return overall
def getRunningBacks(team):
    overall = pullFromDatabase(team, 'HB', '2')
    return overall;
def getOffensiveLine(team):
    overallRG = pullFromDatabase(team, 'RG', '1')
    overallRT = pullFromDatabase(team, 'RT', '1')
    overallC = pullFromDatabase(team, 'C', '1')
    overallLT = pullFromDatabase(team, 'LT', '1')
    overallLG = pullFromDatabase(team, 'LG', '1')
    overall = overallRG + overallRT + overallC + overallLT + overallLG
    return overall/5
def getWideRecievers(team):
    overall = pullFromDatabase(team, 'WR', '3') + pullFromDatabase(team, 'TE', '2')
    return overall/2
def getRunDefense(team):
    overallMLB = pullFromDatabase(team,'MLB','1')
    overallROLB = pullFromDatabase(team,'ROLB','1')
    overallLOLB = pullFromDatabase(team,'LOLB', '1')
    overallRE = pullFromDatabase(team,'RE', '1')
    overallLE = pullFromDatabase(team,'LE', '1')
    overallDT = pullFromDatabase(team,'DT', '2')
    overall = overallDT + overallLE + overallLOLB + overallMLB + overallRE + overallROLB
    return overall/6
def getPassDefense(team):
    overallCB = pullFromDatabase(team, 'CB', '2')
    overallFS = pullFromDatabase(team,'FS', '1')
    overallSS = pullFromDatabase(team, 'SS', '1')
    overall = (overallCB + overallFS + overallSS)/3
    return overall
def getStrengthOfTeam(Entries):
    final = 0.0
    for entry in Entries:
        final += entry

    
    return final/(len(Entries))

def pullFromDatabase(team, pos, amount):
    if(amount == 0):
        sqlCommand = "SELECT overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "'"
    else:
        sqlCommand = "SELECT TOP " + amount + " overall from dbo.Players where Team = '" + team + "' and Position = '" + pos + "' order by overall desc"

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

    for row in cursor:
        total = row[0]

    return final/float(amount)
    
getRunningBacks("Cardinals")