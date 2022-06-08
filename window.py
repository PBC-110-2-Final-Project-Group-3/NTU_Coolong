import datetime
from tkinter import *
from  tkinter import ttk

# if __name__ == "__main__":


   
category = 2    



# settings
class window(Tk):

    def __init__(self, category, course, name, deadline):
        
        Tk.__init__(self)
        self.category = category
        self.course = course
        self.name = name
        self.deadline = deadline
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


        set = ttk.Treeview(self)
        set.pack(fill='x')



        set['columns']= ('category','course','name','deadline')
        set.column("#0", width=0, stretch=NO)
        set.column("category",anchor=CENTER, width=70)
        set.column("course",anchor=CENTER)
        set.column("name",anchor=CENTER)
        set.column("deadline",anchor=CENTER, width=100)
        

        # header
        set.heading("#0",text="",anchor=CENTER)
        set.heading("category",text="Category",anchor=CENTER)
        set.heading("course",text="Class",anchor=CENTER)
        set.heading("name",text="Content",anchor=CENTER)
        set.heading("deadline",text="DeadLine",anchor=CENTER)
        


        # output
        '''
        get_assignments_or_quizzes("assignments")、get_assignments_or_quizzes("quizzes") are lists
        get_assignments_or_quizzes("assignments") = [assignment_1, assignment_2, ...]
        get_assignments_or_quizzes("quizzes") = [quiz_1, quiz_2, ...]
        
        course of assignment_1 --> assignment_1.course
        name of assignment_1 --> assignment_1.name
        deadline of assignment_1 --> assignment_1.deadline
        
        '''

        
        set.insert(parent='',index='end',text='',values=("作業"))
        for i in range(len(get_assignments_or_quizzes("assignments"))):
            set.insert(parent='',index='end',iid=i,text='',values=(" ",get_assignments_or_quizzes("assignments")[i].course,get_assignments_or_quizzes("assignments")[i].name, get_assignments_or_quizzes("assignments")[i].deadline))
        set.insert(parent='',index='end',text='',values=("考試"))
        for j in range(len(get_assignments_or_quizzes("quizzes"))):
            set.insert(parent='',index='end',text='',values=(" ",get_assignments_or_quizzes("quizzes")[j].course,get_assignments_or_quizzes("quizzes")[j].name,get_assignments_or_quizzes("quizzes")[j].deadline))

if __name__ == "__main__":
    win = window(category, course, name, deadline)
    win.mainloop()
