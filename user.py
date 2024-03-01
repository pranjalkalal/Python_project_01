import department
import intern
import job
class unitold:
    def __init__(self):
        print('''welcome to unitold company!
we are create softwares and also provides internships
where you want to join us
1.as a client
2.for internship
3.job''')
        user_i=int(input("enter your choice:"))
        if user_i==1:
            print('''
    cofounder:
    ''')
            department.cofounder()
            print('''
    manager:
    ''')
            department.manager1()
            print('''
    employees:
    ''')
            department.employee()
            print('''
    buget:
    ''')
            department.buget()
        elif user_i==2:
            intern.details()
        else:
            job.jb()

