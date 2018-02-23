import csv, sqlite3

con = sqlite3.connect("conf.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS pcr;")
cur.execute("CREATE TABLE pcr (grade,lastname,firstname,dept,course,teacherlast,parentemail1,parentemail2,studentID INT, period);") # use your column names here


#csv_layout=['grade','lastname','firstname','dept','course','teacherlast','parentemail1','parentemail2','studentID', 'period']


with open('pcr.csv','rU') as fin: # `with` statement available in 2.5+
    data = csv.reader(fin) # comma is default delimiter
    next(data, None) #skip first line

    to_db = [(i[0], i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9]) for i in data]

#print(to_db)
cur.executemany("INSERT INTO pcr (grade,lastname,firstname,dept,course,teacherlast,parentemail1,parentemail2,studentID, period) VALUES (?, ?,?,?,?,?,?,?,?,?);", to_db)
con.commit()
con.close()

