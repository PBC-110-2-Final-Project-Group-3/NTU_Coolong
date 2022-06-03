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
# imput
n = int(input())
# ids = []
# for i in range(n):
    # ids.append(input("課程id："))
classes = []
for i in range(n):
    classes.append(input("課程名稱："))
contents = []
for i in range(n):
    contents.append(input("作業或考試：").split(','))
classes_n_contents = dict()
for i in range(n):
    classes_n_contents[classes[i]] = contents[i]
print(classes_n_contents)  # 到時id_n_classes可以被_get_course_id()取代掉


dates = []
for i in range(n):
    dates.append(input("截止日期："))
times = []
for i in range(n):
    times.append(input("截止時間："))

# settings
from tkinter import *
from  tkinter import ttk

root = Tk()
root.title('DeadLines')

# add style => looks more like ntucool
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview.Heading", background="beige")
style.map('Treeview', background=[('selected','darkseagreen')])


# root.geometry('500x300')

set = ttk.Treeview(root)
set.pack(fill='x')



set['columns']= ('class','content','date', 'time')
set.column("#0", width=0, stretch=NO)
set.column("class",anchor=CENTER)
set.column("content",anchor=CENTER)
set.column("date",anchor=CENTER, width=60)
set.column("time",anchor=CENTER, width=60)

# header
set.heading("#0",text="",anchor=CENTER)
set.heading("class",text="Class",anchor=CENTER)
set.heading("content",text="Content",anchor=CENTER)
set.heading("date",text="Date",anchor=CENTER)
set.heading("time",text="Time",anchor=CENTER)


# output

for i in range(n):
    set.insert(parent='',index='end',iid=i,text='',values=(classes[i],classes_n_contents.get(classes[i]),dates[i],times[i]))


root.mainloop()
