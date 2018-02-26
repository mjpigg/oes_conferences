import datetime,sqlite3,random

def create_empty_schedule():
    delta=datetime.timedelta(minutes=30)
    start=datetime.datetime(2018,2,28,7,30)
    n=1
    c=start
    a=1
    sch={}
    breaks=['9:30','12:0','12:30','14:30']
    while 1:
        the_time = "{}:{}".format(c.hour, c.minute)
        #print(the_time)
        if c>datetime.datetime(2018,3,2,15):
            break
        if the_time in breaks and (c.weekday!=4 and the_time!='14:30'):
           # print('BREAK')
            c=c+delta
            continue
        if c>datetime.datetime(c.year,c.month,c.day,16,30):
            c=start+datetime.timedelta(hours=24*n)
            n+=1
            continue
        #print("{}: {}".format(a,c))
        #print(str(c))
        sch[str(c)]=[]
        a+=1
        c = c + delta
    return(sch)

def get_prefs():
    '''
    This function will return a dictionary of the preferences for each student ID
    for now it's generating random
    :return:
    '''
    options=['Wed AM','Wed AM','Wed AM','Wed AM','Wed Mid','Wed Mid','Wed Mid','Wed PM','Thu AM','Thu Mid','Thu PM','Fri AM','Fri Mid','Fri PM']
    prefs={}
    con = sqlite3.connect("conf.db")
    cur = con.cursor()
    cur.execute("SELECT studentID FROM confs;")
    rows = cur.fetchall()
    con.commit()
    con.close()
    for ID in rows:
        p1=random.choice(options)
        p2 = random.choice(options)
        p3 = random.choice(options)
        prefs[ID[0]]=(p1,p2,p3)
    return(prefs)



prefs=get_prefs()
con = sqlite3.connect("conf.db")
cur = con.cursor()

for key,val in prefs.items():
    sql="INSERT INTO prefs (studentID,pref1,pref2,pref3) VALUES (?,?,?,?)"
    #print(sql)
    cur.execute(sql,(key,val[0],val[1],val[2]))

con.commit()
con.close()