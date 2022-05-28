import tkinter as tk
from tkinter import messagebox
import yaml

class Setting(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.master.title("NTU COOLONG")
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
		self.remindDaysLabel2 = tk.Label(self, text="天提醒我")
		self.loginBtn = tk.Button(self, text="登入", width=10, command=self.save)
	

	def arrange(self):
		self.userLabel.grid(row=1, column=1,)
		self.passwordLabel.grid(row=2, column=1)
		self.userEntry.grid(row=1, column=2, sticky='W', columnspan=4)
		self.passwordEntry.grid(row=2, column=2, sticky='W', columnspan=4)
		self.remindDaysLabel.grid(row=3, column=1)
		self.Days.grid(row=3, column=2, sticky='W'+'E')
		self.remindDaysLabel2.grid(row=3, column=3, sticky='W')
		self.loginBtn.grid(row=5, column=6,sticky="S")

	def save(self):
		d = {}
		d['account'] = self.userEntry.get()
		d['password'] = self.passwordEntry.get()
		with open('Config.yaml', 'w') as f:
			yaml.dump(d, f)


	'''def get(key):
		with open("config.yaml", "r") as f:
			data = yaml.load(f, Loader=yaml.FullLoader)
    try:
        return data[key]
    except Exception:
        raise'''

Set = Setting()
Set.mainloop()
