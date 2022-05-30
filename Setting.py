import tkinter as tk
from tkinter import messagebox
import yaml
#import crawler?

'''這個檔案是「首次登入」介面，按登入button之後會把使用者輸入的帳號密碼存在一個叫Config.yaml的檔案裡'''
class Setting(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('NTU COOLONG')
		self.geometry('380x110+550+300')
		self.resizable(width=0, height=0)
		self.grid()
		self.createWidgets()
		self.arrange()

	def createWidgets(self):
		self.userLabel = tk.Label(self, text="請輸入帳號：")
		self.passwordLabel = tk.Label(self, text="請輸入密碼：")
		self.userEntry = tk.Entry(self)
		self.passwordEntry = tk.Entry(self, show='*')
		self.remindDaysLabel = tk.Label(self, text="在作業截止前")
		self.Days = tk.Entry(self, width=3)
		self.Days.insert(0,'3') # 預設3天前提醒
		self.remindDaysLabel2 = tk.Label(self, text="天提醒我")
		self.loginBtn = tk.Button(self, text="登入", width=10, command=lambda:[self.save()]) # 按下button後要crawl?
	

	def arrange(self):
		self.userLabel.grid(row=1, column=1, sticky='E')
		self.passwordLabel.grid(row=2, column=1, sticky='E')
		self.userEntry.grid(row=1, column=2, sticky='W', columnspan=4)
		self.passwordEntry.grid(row=2, column=2, sticky='W', columnspan=4)
		self.remindDaysLabel.grid(row=3, column=1,sticky='E')
		self.Days.grid(row=3, column=2, sticky='W'+'E')
		self.remindDaysLabel2.grid(row=3, column=3, sticky='W')
		self.loginBtn.grid(row=5, column=6,sticky="S")

	def save(self): # 儲存帳號密碼、倒數幾天
		d = {}
		d['account'] = self.userEntry.get()
		d['password'] = self.passwordEntry.get()
		d['remindDay'] = self.Days.get()
		with open('Config.yaml', 'w') as f:
			yaml.dump(d, f)
		remindDays = self.Days.get()
		#print(remindDays)

	'''def crawl(self):
		crawler1 = crawler.NTUCoolCrawler()
		adict = crawler1.get_assignments_or_quizzes("quizzes", self.userEntry.get(), self.passwordEntry.get())  # It crawls quizzes
		for key in adict.keys():
		    print(key + ":")
		    print(adict[key], "\n===========")
		print("=======================\nFinish!\n=======================")'''


Set = Setting()
Set.mainloop()
