from tkinter import *
from  tkinter import ttk

# if __name__ == "__main__":


   
    



# settings
class window(Tk):
    category = 2
    
    def __init__(self, assignments, quizzes):
        
        Tk.__init__(self)
        self.assignments = assignments
        self.quizzes = quizzes
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
        set.column("category",anchor=CENTER, width=60)
        set.column("course",anchor=W)
        set.column("name",anchor=W)
        set.column("deadline",anchor=CENTER, width=100)
        

        # header
        set.heading("#0",text="",anchor=CENTER)
        set.heading("category",text="Category",anchor=CENTER)
        set.heading("course",text="Course",anchor=CENTER)
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
        if self.assignments == []:
            set.insert(parent='',index='end',text='',values=("","沒有未繳交的作業"))
        else:
            for i in range(len(self.assignments)):
                set.insert(parent='',index='end',iid=i,text='',values=(" ",self.assignments[i].course,self.assignments[i].name,self.assignments[i].deadline))
        set.insert(parent='',index='end',text='',values=("考試"))
        if self.quizzes == []:
            set.insert(parent='',index='end',text='',values=(" ","沒有即將來臨的考試"))
        else:
            for j in range(len(self.quizzes)):
                set.insert(parent='',index='end',text='',values=(" ",self.quizzes[j].course,self.quizzes[j].name,self.quizzes[j].deadline))
    
       

if __name__ == "__main__":
    win = window(category, course, name, deadline)
    win.mainloop()
