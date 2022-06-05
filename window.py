'''
現在有 n 門課、4個column
課程id有id1 ... idn
課程有x1 ... xn
內容有y1 ... yn
日期有z1 ... zn
時間有t1 ... tn

希望內容欄位的寬度可以隨內容長度變化
希望整個視窗的高度可以隨課程數(n)變化

'''
if __name__ == "__main__":
    # parameters(temporary)

    n = 4

    course = ['C/C++程式設計 C/C++ Programming',
            '作業研究 Operations Research',
            '應用線性代數 Applied Linear Algebra',
            '應用線性代數II Applied Linear AlgebraII']
    course_n_assignment = {'C/C++程式設計 C/C++ Programming':['Homework 1','Homework 2'],
            '作業研究 Operations Research':['Case Assignment 1'],
            '應用線性代數 Applied Linear Algebra':['Final Exam'],
            '應用線性代數II Applied Linear AlgebraII':['quiz1']}


# input
# n = int(input())
# course = []
# for i in range(n):
    # course.append(input("課程名稱："))
# assignment = []
# for i in range(n):
    # assignment.append(input("作業或考試：").split(','))
# course_n_assignment = dict()
# for i in range(n):
    # course_n_assignment[course[i]] = assignment[i]
# print(course_n_assignment)  # 到時id_n_classes可以被_get_course_id()取代掉

if __name__ == "__main__":
    dates = []
    for i in range(n):
        dates.append(input("截止日期："))
    times = []
    for i in range(n):
        times.append(input("截止時間："))
    



# settings
from tkinter import *
from  tkinter import ttk

class window(Tk):

    def __init__(self, course, course_n_assignment, dates, times):
        
        Tk.__init__(self)
        self.course = course
        self.course_n_assignment = course_n_assignment
        self.dates = dates
        self.times = times
        
        self.title('DeadLines')
        self.list()

    # root = Tk()
    # root.title('DeadLines')

    def list(self):    
        # add style
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="beige")
        style.map('Treeview', background=[('selected','darkseagreen')])


# root.geometry('500x300')

        set = ttk.Treeview(self)
        set.pack(fill='x')



        set['columns']= ('course','assignment','date', 'time')
        set.column("#0", width=0, stretch=NO)
        set.column("course",anchor=CENTER)
        set.column("assignment",anchor=CENTER)
        set.column("date",anchor=CENTER, width=60)
        set.column("time",anchor=CENTER, width=60)

        # header
        set.heading("#0",text="",anchor=CENTER)
        set.heading("course",text="Class",anchor=CENTER)
        set.heading("assignment",text="Content",anchor=CENTER)
        set.heading("date",text="Date",anchor=CENTER)
        set.heading("time",text="Time",anchor=CENTER)


        # output

        for i in range(n):
            set.insert(parent='',index='end',iid=i,text='',values=(course[i],course_n_assignment.get(course[i]),dates[i],times[i]))

if __name__ == "__main__":
    win = window(course, course_n_assignment, dates, times)
    win.mainloop()
