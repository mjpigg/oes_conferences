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


def make_times(sort=True):
    l=[]
    the_times = scheduler.create_empty_schedule()
    for x in range(5):
        for i in the_times:
            l.append(i)
    if sort:
        return sorted(l)

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

ids = get_ids()

# print(len(make_times()))
# print(create_dna(ids))



def fitness(dna):
    '''
    This function takes in a DNA and returns a normalized fitness score

    Things to consider for fitness:
        5 sessions per time block
        student got 1, 2, or 3 preference
        siblings are back to back
        advisor conflicts are minimized
        triple bookings are minimized

    :param DNA:
    :return:
    '''
    pass



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

