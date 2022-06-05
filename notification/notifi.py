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

#要傳入的參數
if __name__ == "__main__":
    set_day = 2

    course = ['C/C++程式設計 C/C++ Programming',
            '作業研究 Operations Research',
            '應用線性代數 Applied Linear Algebra',
            '應用線性代數II Applied Linear AlgebraII']
    assignment=[['Homework 1','Homework 2'],['Case Assignment 1'],['Final Exam'],['quiz1']]

class notification(tk.Tk):
    
    def __init__(self,day,course,assignment):

        tk.Tk.__init__(self)
        self.day = day
        self.course = course
        self.assignment = assignment
        
        num_assignment = 0
        for i in range(len(self.course)):
            for j in range(len(self.assignment[i])):
                num_assignment+=1
        windowheight = max(num_assignment*45,150)
        
        self.title('NTU Coolong ALARM')
        self.geometry('600x%d+400+250' % (windowheight))
        self.resizable(width=0, height=0)
        self.createWindow()
        self.music()
        self.iconbitmap('./notification/icon.ico')
    
    def music(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.load('./notification/bgm.mp3')
        pygame.mixer.music.play(-1)
        
    def table(self):
        bg_color = 'beige'
        treeheight = len(course)+2
        columns=("Course","Assignment")
        tree=ttk.Treeview(self,height=treeheight,show="headings",columns=columns)
        tree.column("Course",width=200,anchor='center')   #表示列,不顯示
        tree.column("Assignment",width=250,anchor='center')
        tree.heading("Course",text="課程名稱")  #顯示表頭
        tree.heading("Assignment",text="作業")
        tree.place(relx=0.42,rely=0.48,anchor='center')
        style = ttk.Style()
        """
        #表格顏色
        style.theme_use('clam')
        style.configure("Treeview", background=bg_color, 
                             foreground="black", fieldbackground=bg_color)
        """
        #表格內容
        style.map("Treeview",
                  background=[('selected','darkseagreen')])
        index = 0
        for i in range(len(self.course)):
            for j in range(len(self.assignment[i])):
                tree.insert('',index,values=(self.course[i],self.assignment[i][j]))
                index+=1
                
    def msg(self):
        bg_color = 'beige'
        fontStyle = tkFont.Font(family="微軟正黑體", size=10, weight='bold')
        labelmsg = tk.Label(self,                 # 文字標示所在視窗
                         text = '再'+str(self.day)+'天就要交作業囉！加油！！',
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
        labelbomb.place(relx=0.52,rely=0.48,anchor='center',x=230,y=0)

    def createWindow(self):
        self.msg()
        self.table()
        self.image()
        
    def __del__(self):
        pygame.mixer.music.stop()   #停止音效

if __name__ == "__main__":            
    noti = notification(set_day,course,assignment)
    noti.mainloop()
