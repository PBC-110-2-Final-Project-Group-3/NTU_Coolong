import datetime
from tkinter import *
from  tkinter import ttk

if __name__ == "__main__":
    # parameters(temporary)

    '''
    course = ['C/C++程式設計 C/C++ Programming',
            '作業研究 Operations Research',
            '應用線性代數 Applied Linear Algebra',
            '應用線性代數II Applied Linear AlgebraII']
    course_n_assignment = {'C/C++程式設計 C/C++ Programming':'Homework 1','C/C++程式設計 C/C++ Programming':'Homework 2',
            '作業研究 Operations Research':'Case Assignment 1',
            }
    course_n_quizz = {'應用線性代數 Applied Linear Algebra':['Final Exam'],
            '應用線性代數II Applied Linear AlgebraII':['quiz1']}
    assignment = ['C/C++程式設計 C/C++ Programming,Homework 1,2021-10-13 17:30:00','C/C++程式設計 C/C++ Programming,Homework 2,2021-11-10 17:30:00',
    '作業研究 Operations Research,Case Assignment 1,2021-12-08 17:30:00']
    quiz = ['應用線性代數 Applied Linear Algebra,Final Exam, 2022-01-01 22:00:00',
            '應用線性代數II Applied Linear AlgebraII,quiz1,2022-02-21 23:59:59']
    '''
    
    # temporary deadline
    deadline = datetime.datetime(2022, 6, 19, 23, 59, 59)
    dates = deadline.date()
    times = deadline.time()
    category = 0

    



# settings
class window(Tk):

    def __init__(self, category, course, course_n_assignment, dates, times):
        
        Tk.__init__(self)
        self.category = category
        self.course = course
        self.course_n_assignment = course_n_assignment
        self.dates = dates
        self.times = times
        
        self.title('DeadLines')
        self.list()

        
    # root.title('DeadLines')

    def list(self):    
        # add style
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="beige")
        style.map('Treeview', background=[('selected','darkseagreen')])
        # root = tk.Tk()

# root.geometry('500x300')

        set = ttk.Treeview(self)
        set.pack(fill='x')



        set['columns']= ('category','course','assignment','date', 'time')
        set.column("#0", width=0, stretch=NO)
        set.column("category",anchor=CENTER, width=70)
        set.column("course",anchor=CENTER)
        set.column("assignment",anchor=CENTER)
        set.column("date",anchor=CENTER, width=60)
        set.column("time",anchor=CENTER, width=60)

        # header
        set.heading("#0",text="",anchor=CENTER)
        set.heading("category",text="Category",anchor=CENTER)
        set.heading("course",text="Class",anchor=CENTER)
        set.heading("assignment",text="Content",anchor=CENTER)
        set.heading("date",text="Date",anchor=CENTER)
        set.heading("time",text="Time",anchor=CENTER)


        # output
        assignments = []
        for i in range(len(assignment)):
            assignments.append(assignment[i].split(','))
        quizzes = []
        for i in range(len(quiz)):
            quizzes.append(quiz[i].split(','))

        # Label(self, text="作業", bg="#3300CC", fg="white").place(x=90, y=28)
        # Label(self, text="Position 1 : x=0, y=0", bg="#FFFF00", fg="white")
        set.insert(parent='',index='end',text='',values=("作業"))
        for i in range(len(assignment)):
            set.insert(parent='',index='end',iid=i,text='',values=(" ",assignments[i][0],assignments[i][1],dates,times))
        set.insert(parent='',index='end',text='',values=("考試"))
        for j in range(len(quiz)):
            set.insert(parent='',index='end',text='',values=(" ",quizzes[j][0],quizzes[j][1],dates,times))

if __name__ == "__main__":
    win = window(category, course, course_n_assignment, dates, times)
    win.mainloop()
