from tkinter import *

class Mine():
	def __init__(self):
		

window = Tk()
window.geometry("500x500")

mines = []
for i in range(10):
	mines.append(Button())

window.mainloop()