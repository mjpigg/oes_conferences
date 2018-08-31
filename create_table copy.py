import csv, sqlite3
#from scheduler import get_prefs

con = sqlite3.connect("conf.db")
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS pcr;")
cur.execute("CREATE TABLE pcr "
            "(grade,advisor,lastname,firstname,dept,course,teacherlast,"
            "parentemail1,parentemail2,studentID INT, period,parent1first,"
            "parent1last,parent2first,parent2last);")


# csv_layout=['grade','lastname','firstname','dept','course','teacherlast','parentemail1','parentemail2','studentID', 'period']

# take the data from the PCR dump file and loast it into a list of tuples for loading to database
with open('pcr.csv','rU') as fin:  # `with` statement available in 2.5+
    data = csv.reader(fin)  # comma is default delimiter
    next(data, None)  # skip first line

    to_db = [(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14]) for i in data]

# load data from cvs into conf.pcr
#print(to_db)
cur.executemany("INSERT INTO pcr "
                "(grade, advisor, lastname, firstname, dept, course, teacherlast, parentemail1, parentemail2, "
                "studentID, period, parent1first, parent1last, parent2first, parent2last) "
                "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)

# create conferences db table

cur.execute("DROP TABLE IF EXISTS confs;")
sql = "CREATE TABLE confs (studentID INT PRIMARY KEY,grade,the_date,room,lastname,firstname,advisor,english,hum_hist," \
      "language,math,act_art,music,pe,science,parents);"

cur.execute(sql)
cur.execute("SELECT studentID,grade,firstname,lastname,advisor FROM pcr GROUP BY studentID")
rows = cur.fetchall()

# Create preferences table
cur.execute("DROP TABLE IF EXISTS prefs;")
sql = "CREATE TABLE prefs (studentID INT,pref1,pref2,pref3);"
cur.execute(sql)

# Create best schedules table
cur.execute("DROP TABLE IF EXISTS schedules;")
sql = "CREATE TABLE schedules (scheduleID INTEGER PRIMARY KEY AUTOINCREMENT, score, mutation_rate, population_size, random_seed, date_produced datetime, schedule);"
cur.execute(sql)


# First pass, just add all the studentIDs to confs
to_db = [(i[0], i[1], i[2], i[3], i[4]) for i in rows]

cur.executemany("INSERT INTO confs (studentID, grade, firstname, lastname, advisor)"
                " VALUES (?, ?, ?, ?, ?);", to_db)


# Second pass, UPDATE confs to add English, Hum_Hist,Language,Math,PE, Science
sql = "SELECT studentID,dept,course,teacherlast,period FROM pcr WHERE dept NOT LIKE 'Perform%' " \
    "AND dept NOT LIKE 'Acti%' GROUP BY studentID,course;"
cur.execute(sql)
rows = cur.fetchall()

col_map = {
    'Languages': 'language',
    'Science': 'science',
    'PhysicalEducation': 'pe',
    'Performing & Fine Art': 'act_art',
    'Mathematics': 'math',
    'Humanities': 'hum_hist',
    'History': 'hum_hist',
    'English': 'english'
         }


for i in rows:
    sql = "UPDATE confs SET {}='{}' WHERE studentID={};".format(col_map[i[1]],i[3].replace("'","''"),i[0])
    cur.execute(sql)

# Third pass, UPDATE Act/Art
sql = "SELECT studentID, teacherlast from pcr where dept LIKE 'perf%' AND (course LIKE 'Act%' OR course like 'Art%') " \
    "GROUP BY course,studentID;"
cur.execute(sql)
rows = cur.fetchall()
for i in rows:
    sql = "UPDATE confs SET act_art='{}' WHERE studentID={};".format(i[1].replace("'","''"),i[0])
    cur.execute(sql)

# fourth, UPDATE Music
sql = "SELECT studentID, teacherlast from pcr where dept LIKE 'perf%' AND (course LIKE 'Band%' OR course like 'Choir%') " \
    "GROUP BY course,studentID;"
cur.execute(sql)
rows = cur.fetchall()
for i in rows:
    sql = "UPDATE confs SET music='{}' WHERE studentID={};".format(i[1].replace("'","''"),i[0])
    cur.execute(sql)


# Fifth pass, ADD all e-mails
'''
Format parents in a list like this:
"John Smith" <johnsemail@hisserver.com>; "Jane Smith" <janesmail@hisserver.com>
'''
def email_format(firstname,lastname,email):
    e = "\"{} {}\" <{}>".format(firstname.replace("'","''"),lastname.replace("'","''"),email)
    return e


sql = "SELECT studentID,parent1first,parent1last,parentemail1 FROM pcr GROUP BY studentID,parentemail1;"
cur.execute(sql)
rows = cur.fetchall()
# create a dictionary of parent emails
parents = {}
for i in rows:
    parents[i[0]]=[] #create empty list and then append to it

for i in rows:
    if i[1] != '': parents[i[0]].append(email_format(i[1],i[2],i[3]))

sql = "SELECT studentID,parent2first,parent2last,parentemail2 FROM pcr GROUP BY studentID,parentemail2;"
cur.execute(sql)
rows = cur.fetchall()
for i in rows:
    if i[1]!='': parents[i[0]].append(email_format(i[1],i[2],i[3]))

for key,value in parents.items():
    sql = "UPDATE confs SET parents='{}' WHERE studentID={};".format(' '.join(value),key)
    cur.execute(sql)

cols = ['studentID','grade','the_date','room','lastname','firstname','advisor','english','hum_hist',
      'language','math','act_art','music','pe','science','parents']

sql = "SELECT * FROM confs ORDER BY the_date,room,grade,lastname,firstname;"
# print(sql)
cur.execute(sql)
rows = cur.fetchall()
con.commit()

# Add prefs from Survey Monkey export
# with open('prefs.csv','rU') as fin:
with open('prefs.csv', encoding = "ISO-8859-1") as fin:
    data = csv.reader(fin)  # comma is default delimiter
    next(data, None)  # skip first line
    to_db = [(i[0], i[2], i[3], i[4]) for i in data if i[2]!='']

# print(to_db)
# load data from cvs into conf.pcr
cur.executemany("INSERT INTO prefs "
                "(studentID, pref1, pref2, pref3) "
                "VALUES (?, ?, ?, ?);", to_db)

con.commit()
cur.close()
con.close()

