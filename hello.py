from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!!!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/conf/<teacher>')
def show_schedule(teacher):
    if teacher!='':
        return get_csv(teacher)
    else:
        return "Please select a Teacher from the List Below"

def get_csv(teacher):
    data = "Teacher Conference Schedule for {}".format(teacher.title())
    data+='<br><BR>'
    conflicts=get_advisee_times(teacher)

    conferences=get_conferences()
    day=''
    time=''
    the_total=0

    bookings=get_bookings(teacher)

    for row in conferences:
        advisor=False
        if row[6].split(',')[0].split(' ')[0].lower()==teacher.lower():
            advisor=True
        #check match
        match=False
        for check in row[6:15]:
            if teacher.lower()==check.split(',')[0].split(' ')[0].lower():
                match=True
                continue

        if match:
            id=row[1]+row[2]

            if day != row[1]: data += '<br>' #new day, so add an extra break

            #if time==row[2] and day==row[1]: data+='** '
            if bookings.get(id,0)>1: data += '*'*bookings[id]+' '
            data+="{} {} {} {} {}".format(row[1],row[2],row[3],row[5],row[4])
            if id in conflicts and not advisor:
                data+=' << CANNOT ATTEND, DUE TO ADVISEE CONFLICT >>'
            if advisor: data += '<< ADVISEE >> '
            data+='<br>'
            the_total+=1
            day=row[1]
            time=row[2]

    data+="<BR>{} Conferences".format(the_total)
    data+='<BR><BR>** Double Booked Conference<BR><BR>'
    #return "i'm in "+teacher
    return data


@app.route('/conf/')
def test_print():
    data= "Please Select a teacher from the list below<br>"
    data+=get_teachers()
    return data

@app.route('/test/<teacher>')
def test_page(teacher):
    data='test'
    for x in get_advisee_times(teacher):
        data+=x
    return data



def get_bookings(teacher):
    bookings={}
    for row in get_conferences():
        match=False
        for check in row[6:15]:
            if teacher.lower()==check.split(',')[0].split(' ')[0].lower():
                match=True
                continue
        if match: #matches the teacher
            book_id=row[1]+row[2] #unique ID time
            bookings[book_id]=bookings.get(book_id,0)+1
    return bookings


def get_conferences():
    import csv
    with open('conferences.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data, None)
        conferences = []
        for row in data:
            conferences.append(row)
    return conferences

def get_advisee_times(teacher):
    conferences=get_conferences()
    times=[]
    for row in conferences:
        if row[6].split(',')[0].split(' ')[0].lower()==teacher.lower(): #this teacher is the advisor
            times.append(row[1]+row[2])
    return times


def get_teachers():
    import csv
    text=''
    with open('conferences.csv') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        next(data, None)
        conferences = []
        for row in data:
            conferences.append(row)
    teacher_set=set()
    for row in conferences:
        for i in range(6,15):
            if row[i] != '' and row[0] in ['6','7','8']:
                teacher_set.add(row[i].split(',')[0].split(' ')[0].title())


    for teacher in sorted(teacher_set):
         text+="<a href='./"+teacher.split(',')[0]+"'>"+teacher+"<br>"
    return text

