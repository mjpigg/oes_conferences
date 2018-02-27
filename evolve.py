'''
Functions for Evolving the Population toward best fitting schedule
DNA will be a dictionary of this structure:

DNA = {
        studentID: 'conf datetime'
        studentID: 'conf datetime'
        }

1 DNA strand represents a schedule which is on element of the population
'''
import scheduler
import random
import sqlite3
import datetime

def make_times(sort = True):
    conf_times = []
    the_times = scheduler.create_empty_schedule()
    for x in range(5):
        for i in the_times:
            conf_times.append(i)
    if sort:
        return sorted(conf_times)

def get_ids():
    con = sqlite3.connect("conf.db")
    cur = con.cursor()
    cur.execute("SELECT studentID FROM confs;")
    rows = cur.fetchall()
    con.commit()
    con.close()
    ids = []
    for id in rows:
        ids.append(id[0])
    return ids

def create_dna(ids):
    sessions = make_times()
    dna = {}
    for id in ids:
        dna[id] = sessions.pop(random.randrange(len(sessions)))
    return dna

def conftime_to_preftime(conf_time):
    days = {2: 'Wed ', 3: 'Thu ', 4: 'Fri '}
    c = datetime.datetime.strptime(conf_time, "%Y-%m-%d %H:%M:%S")
    pref_time = days[c.weekday()]
    if c.hour < 11:
        pref_time += 'AM'
    elif c.hour < 14:
        pref_time += 'Mid'
    else:
        pref_time += 'PM'
    return pref_time


#c = datetime.datetime.strptime('2018-02-28 07:30:00',"%Y-%m-%d %H:%M:%S")
#print(c.weekday(),c.hour)
# print(len(make_times()))
sample = create_dna(get_ids())
print(conftime_to_preftime(sample[20483]))

def get_prefs():
    '''
    This function will return a dictionary of the preferences for each student ID
    for now it's generating random
    :rtype: object
    :return:
    '''
    prefs={}
    con = sqlite3.connect("conf.db")
    cur = con.cursor()
    cur.execute("SELECT * from prefs;")
    rows = cur.fetchall()
    con.commit()
    con.close()
    for ID in rows:
        prefs[ID[0]]=(ID[1].encode('ascii'), ID[2].encode('ascii'), ID[3].encode('ascii'))
    return(prefs)



def fitness(dna):
    '''
    This function takes in a DNA and returns a normalized fitness score
    Things to consider for fitness:
        student got pref1 +5
        student got pref2 +3
        student got pref3 +2
        4 or 5 sessions +1
        empty last conf +2
        all three grades per slot +5
        siblings are back to back + 10
        advisor conflict -1 for each one
        triple bookings -1 for each one
    :param dna :
    :return:
    '''
    score=0

    # check prefs
    prefs = get_prefs()
    for key, value in dna.items():
        pass


    return random.randint(0,50)

def create_population(n):
    pop = []
    ids = get_ids()
    for i in range(n):
        dna = create_dna(ids)
        pop.append([0,dna])
    return pop


def crossover(dna1,dna2):
    '''
    Takes in two "parent DNAs" and randomly crosses them
    by swapping
    :param DNA_1:
    :param DNA_2:
    :return:
    '''
    pass

def mutate(dna):
    '''
    mutates the DNA
    move ID 1,2 or 3 slots earlier or later
    if session full, then swap with one ID already there, otherwise just move and now swap
    :param DNA:
    :return:
    '''
    pass

