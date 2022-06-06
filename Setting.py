import tkinter as tk
from tkinter import messagebox
import yaml
import os

'''這個檔案是「首次登入」介面，按登入button之後會把使用者輸入的帳號密碼存在一個叫Config.yaml的檔案裡'''
class Setting(tk.Tk):

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('NTU COOLONG LOGIN')
		self.geometry('380x110+550+300')
		self.resizable(width=0, height=0)
		self.grid()
		self.createWidgets()
		self.arrange()
		self.configure(bg='beige')

	def createWidgets(self):
		self.userLabel = tk.Label(self, text="請輸入帳號：", bg='beige')
		self.passwordLabel = tk.Label(self, text="請輸入密碼：", bg='beige')
		self.userEntry = tk.Entry(self,highlightbackground='beige',bg='beige')
		self.passwordEntry = tk.Entry(self, show='*',highlightbackground='beige',bg='beige')
		self.remindDaysLabel = tk.Label(self, text="在作業截止前", bg='beige')
		self.Days = tk.Entry(self, width=3,highlightbackground='beige',bg='beige')
		self.Days.insert(0,'3') # 預設3天前提醒
		self.remindDaysLabel2 = tk.Label(self, text="天提醒我", bg='beige')
		self.loginBtn = tk.Button(self, text="登入", width=10, highlightbackground='beige',fg='darkseagreen', command=lambda:[self.save()])
		self.leaveBtn = tk.Button(self, text='離開',width=10, highlightbackground='beige', fg='darkseagreen',command=lambda:[self.destroy()])

	def arrange(self):
		self.userLabel.grid(row=1, column=1, sticky='E')
		self.passwordLabel.grid(row=2, column=1, sticky='E')
		self.userEntry.grid(row=1, column=2, sticky='W', columnspan=4)
		self.passwordEntry.grid(row=2, column=2, sticky='W', columnspan=4)
		self.remindDaysLabel.grid(row=3, column=1,sticky='E')
		self.Days.grid(row=3, column=2, sticky='W'+'E')
		self.remindDaysLabel2.grid(row=3, column=3, sticky='W')
		self.loginBtn.grid(row=5, column=6,sticky="S")
		self.leaveBtn.grid(row=5, column=5)

	def save(self): # 儲存帳號密碼、倒數幾天
		d = {}
		d['account'] = self.userEntry.get()
		d['password'] = self.passwordEntry.get()
		d['remindDay'] = self.Days.get()
		path = os.path.join('Users', 'pengchihyi', 'Desktop','PBC', 'NTU_Coolong')
		with open('Config.yaml', 'w') as f:
			yaml.dump(d, f)
		remindDays = self.Days.get()
		#print(remindDays)
		self.destroy()

if __name__ == "__main__":
	Set = Setting()
	Set.mainloop()
