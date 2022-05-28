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
n = int(input())
ids = []
for i in range(n):
    ids.append(input("課程id："))
classes = []
for i in range(n):
    classes.append(input("課程名稱："))
id_n_classes = dict()
for i in range(n):
    id_n_classes[ids[i]] = classes[i]
print(id_n_classes)  # 到時id_n_classes可以被_get_course_id()取代掉

contents = []
# dates = []
# times = []
for i in range(n):
    contents.append(input("作業或考試：").split(','))
print(contents)
# for i in range(n):
    # dates.append(input("截止日期)

from tkinter import *
from  tkinter import ttk


ws  = Tk()
ws.title('DeadLines')
ws.geometry('500x300')

set = ttk.Treeview(ws)
set.pack(fill='x')

set['columns']= ('class_id','class','content','date', 'time')
set.column("#0", width=0, stretch=NO)
set.column("class_id",anchor=CENTER,width=60)
set.column("class",anchor=CENTER, width=80)
set.column("content",anchor=CENTER, width=100)
set.column("date",anchor=CENTER, width=60)
set.column("time",anchor=CENTER, width=60)

# 標題
set.heading("#0",text="",anchor=CENTER)
set.heading("class_id",text="Class ID",anchor=CENTER)
set.heading("class",text="Class",anchor=CENTER)
set.heading("content",text="Content",anchor=CENTER)
set.heading("date",text="Date",anchor=CENTER)
set.heading("time",text="Time",anchor=CENTER)


# 清單
set.insert(parent='',index='end',iid=0,text='',
values=(ids[0],id_n_classes.get(ids[0]),contents[0],'05/12','02:20'))
set.insert(parent='',index='end',iid=1,text='',
values=(ids[1],id_n_classes.get(ids[1]),contents[1],'06/09',))
set.insert(parent='',index='end',iid=2,text='',
values=(ids[2],id_n_classes.get(ids[2]),contents[2],'06/15','18:00'))

ws.mainloop()