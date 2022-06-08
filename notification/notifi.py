# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:09:24 2022

@author: wenjie
"""

import tkinter as tk
from  tkinter import ttk
import tkinter.font as tkFont
import pygame
from PIL import Image, ImageTk


class notification(tk.Tk):
    
    def __init__(self,day,lis):

        tk.Tk.__init__(self)
        self.day = day
        self.lis = lis
        
        num_assignment = len(lis)
        windowheight = max(num_assignment*65,165)
        
        self.title('NTU COOLONG ALARM')
        self.geometry('700x%d+400+250' % (windowheight))
        self.resizable(width=0, height=0)
        self.music()
        self.iconbitmap('./notification/icon.ico')
        self.createWindow()
        
    def music(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load('./notification/bgm.mp3')
        pygame.mixer.music.play(0)
        
    def table(self):
        bg_color = 'beige'
        treeheight = len(self.lis)+2
        columns=("Course","Assignment","Deadline")
        tree=ttk.Treeview(self,height=treeheight,show="headings",columns=columns)
        tree.column("Course",width=150,anchor='center')   #表示列,不顯示
        tree.column("Assignment",width=200,anchor='center')
        tree.column("Deadline",width=150,anchor='center')
        tree.heading("Course",text="Class")  #顯示表頭
        tree.heading("Assignment",text="Content")
        tree.heading("Deadline",text="Deadline")
        tree.place(relx=0.42,rely=0.42,anchor='center')
        style = ttk.Style()

        #表格顏色
        style.theme_use('clam')
        style.configure("Treeview", background=bg_color, 
                             foreground="black", fieldbackground=bg_color)
        #表格內容
        style.map("Treeview",
                  background=[('selected','darkseagreen')])
        index = 0
        for i in range(len(self.lis)):
            tree.insert('',index,values=(self.lis[i].course,self.lis[i].name,self.lis[i].deadline))
            index+=1
                
    def msg(self):
        bg_color = 'beige'
        fontStyle = tkFont.Font(family="微軟正黑體", size=10, weight='bold')
        labelmsg = tk.Label(self,                 # 文字標示所在視窗
                         text = '快要考試/交作業囉！加油！！',
                         font=fontStyle,fg='crimson',
                         bg=bg_color)  # 顯示文字
        labelmsg.place(relx=0.42,rely=0.90,anchor='center')
        self.configure(bg=bg_color)
        
    def image(self):
        bg_color = 'beige'  #背景顏色
        image = Image.open("./notification/bomb.png")
        image = image.resize((100, 100), Image.ANTIALIAS)
        self.display = ImageTk.PhotoImage(image)
        labelbomb = tk.Label(self, image=self.display,bg=bg_color)
        labelbomb.place(relx=0.9,rely=0.42,anchor='center')

    def button(self):
        leaveBtn = tk.Button(self, text='離開',width=10, highlightbackground='beige', fg='darkseagreen',command=lambda:[self.destroy(),self.leave()])
        leaveBtn.place(relx=0.9,rely=0.88,anchor='center')
        
    def createWindow(self):
        self.msg()
        self.table()
        self.image()
        self.button()
        
    def __del__(self):
        pygame.mixer.music.stop()   #停止音效
            
if __name__ == "__main__":
    class assign:
        
        def __init__(self,course,name,deadline):
            self.course = course
            self.name = name
            self.deadline = deadline
        
    a1 = assign('作業研究 Operations Research','Homework 1','2022-06-05')
    a2 = assign('作業研究 Operations Research','Homework 2','2022-06-05')
    a3 = assign('C/C++程式設計 C/C++ Programming','Case Assignment 1','2022-06-05')

    set_day = 2
    lis = [a1,a2,a3]
    noti = notification(set_day,lis)
    #noti.after(30000, lambda: noti.destroy())
    noti.mainloop()
