from tkinter import *

window = Tk()
window.geometry("500x550")

mines = []
for x in range(10):
	for y in range(10):
		mine = Button(window, text = "", bg='grey')
		mine.place(x = x * 50, y = y * 50 + 50, width = 50, height = 50)

window.mainloop()