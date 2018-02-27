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




#print(get_prefs())

