# -*- coding: utf-8 -*-
"""
Created on Thu May 26 12:09:24 2022

@author: User
"""

import tkinter as tk
from  tkinter import ttk
import tkinter.font as tkFont
import pygame
from PIL import Image, ImageTk

#要傳入的參數
set_day = 2

course = ['C/C++程式設計 C/C++ Programming',
          '作業研究 Operations Research',
          '應用線性代數 Applied Linear Algebra',
          '應用線性代數II Applied Linear AlgebraII']
assignment=[['Homework 1','Homework 2'],['Case Assignment 1'],['Final Exam'],['quiz1']]

def notification(day,course_name,due_assignment):

    #計算作業總數
    num_assignment = 0
    for i in range(len(course_name)):
        for j in range(len(due_assignment[i])):
            num_assignment+=1
    windowheight = max(num_assignment*45,150)
    
    window = tk.Tk()
    window.title('NTU COOLONG ALARM')
    window.geometry('650x%d+400+250' % (windowheight))
    window.resizable(width=0, height=0)
    #音效
    pygame.mixer.init()
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.load('bgm.mp3')
    pygame.mixer.music.play(-1)
    
    bg_color = 'beige'  #背景顏色
    
    #炸彈圖示
    
    image = Image.open("bomb.png")
    image = image.resize((100, 100), Image.ANTIALIAS)
    display = ImageTk.PhotoImage(image)
    labelbomb = tk.Label(window, image=display,bg=bg_color)
    labelbomb.place(relx=0.52,rely=0.48,anchor='center',x=230,y=0)
    #labelbomb.grid(row=0,column=6)
    
    #作業列表
    treeheight = len(course)+2
    columns=("Course","Assignment")
    tree=ttk.Treeview(window,height=treeheight,show="headings",columns=columns)
    tree.column("Course",width=200,anchor='center')   #表示列,不顯示
    tree.column("Assignment",width=250,anchor='center')
    tree.heading("Course",text="課程名稱")  #顯示表頭
    tree.heading("Assignment",text="作業")
    #tree.grid(row=0,column=0,columnspan=3)
    tree.place(relx=0.42,rely=0.48,anchor='center')
    style = ttk.Style()
    """表格顏色
    style.theme_use('clam')
    style.configure("Treeview", background=bg_color, 
                         foreground="black", fieldbackground=bg_color)
    """
    #表格內容
    style.map("Treeview",
              background=[('selected','darkcyan')])
    index = 0
    for i in range(len(course_name)):
        for j in range(len(due_assignment[i])):
            tree.insert('',index,values=(course_name[i],due_assignment[i][j]))
            index+=1
            
    # 提醒文字
    fontStyle = tkFont.Font(family="微軟正黑體", size=10, weight='bold')
    labelmsg = tk.Label(window,                 # 文字標示所在視窗
                     text = '再'+str(day)+'天就要交作業囉！加油！！',
                     font=fontStyle,fg='crimson',
                     bg=bg_color)  # 顯示文字
    labelmsg.place(relx=0.42,rely=0.90,anchor='center')
    
    
    window.configure(bg=bg_color)
    window.iconbitmap('icon.ico')
    window.mainloop()
    pygame.mixer.music.stop()   #停止音效


notification(set_day,course,assignment)