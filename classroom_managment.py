classroom = [
    {
        'name': 'Alice',
        'email': 'alice@example.com',
        'grades': [
            ('math', 91),
            ('english', 78),
            ('math', 90),
            ('history', 34),
            ('math', 95),
        ],
    },
    {
        'name': 'Bob',
        'email': 'bob@example.com',
        'grades': [
            ('math', 85),
            ('english', 92),
            ('history', 75),
        ],
    },
    {
        'name': 'Charlie',
        'email': 'charlie@example.com',
        'grades': [
            ('physics', 78),
            ('english', 81),
            ('english', 89),
            ('history', 68),
            ('english', 82),
            ('physics', 91),
        ],
    },
]

def index(name):
    for i,student in enumerate(classroom) :
        if name==student['name']:
           return i
    return -1   
        
def add_student(name, email=None):
    """Add a new student to the classroom
    with the following keys:
    'name': the given name
    'email': if email is given use it otherwise use <name>@example.com
             in lowercase, you can use the `s.lower()` method
    'grade': initialize with empty list
    """
    if email==None:
        email=f'{name.lower()}@example.com'
    classroom.append({'name':name,'email':email,'grades':[]})
    pass

def delete_student(name):
    """Delete a student from the classroom"""
    del classroom[index(name)]
    pass
def set_email(name, email):
    """Sets the email of the student"""
    classroom[index(name)]['email']=email
    pass

def add_grade(name, profession, grade):
    """Adds a new grade to the student grades"""
    tpl=(profession,grade)
    classroom[index(name)]['grades'].append(tpl)
    pass
add_grade("Bob","math",100)
add_grade("Bob","math",45)


def avg_grade(name, profession):
    """Returns the average of grades of the student
    in the specified profession
    """
    sum=0
    count=0
    for t in classroom[index(name)]['grades']:
        if(t[0]==profession):
            count+=1
            sum+=t[1]
    return sum/count
    pass

def get_professions(name):
    """Returns a list of unique professions that student has grades in"""
    lst=[]
    for i in classroom[index(name)]['grades']:
        lst.append(i[0])
    lst=set(lst)    
    return lst    
    pass

# def get_professions2(name):
#     profession = set()
#     for item in classroom[index(name)]['grades']:
#         profession.add(item[0])
#     return profession
# print(get_professions2("Charlie"))