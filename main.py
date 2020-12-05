from tkinter import *
from random import randint as rnd

class Cell():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.status = None
		self.button = Button(window, text = "", bg='grey', command = lambda: mine_check(self))
		self.button.place(x = x * 50, y = y * 50 + 50, width = 50, height = 50)

def generate():
	global mines
	# Генерация поля
	for y in range(10):
		mines.append([])
		for x in range(10):
			mines[y].append(Cell(x, y))
			print(x, y)

	# Генерация мин
	i = 0
	while i != 10:
		mine_x = rnd(0, 9)
		mine_y = rnd(0, 9)
		if mines[mine_y][mine_x].status == 'mine':
			i -= 1
		else:
			mines[mine_y][mine_x].status = 'mine'
		i += 1

	# Обозначение номера
	for y2 in range(len(mines)):
		for x2 in range(mines[y2]):
			if mines[y2][x2].status == None:
				

def environment_check(button):
	global mines
	i = 0
	try:
		# Верхняя левая
		if button.x != 0 and button.y != 0:
			if mines[button.y - 1][button.x - 1].is_mine:
				i += 1
		# Верхняя
		if button.y != 0:
			if mines[button.y - 1][button.x].is_mine:
				i += 1
		# Верхняя правая
		if button.y != 0:
			if mines[button.y - 1][button.x + 1].is_mine:
				i += 1
		# Левая
		if button.x != 0:
			if mines[button.y][button.x - 1].is_mine:
				i += 1
		# Правая
		if mines[button.y][button.x + 1].is_mine:
			i += 1
		# Нижняя левая
		if button.x != 0:
			if mines[button.y + 1][button.x - 1].is_mine:
				i += 1
		# Нижняя
		if mines[button.y + 1][button.x].is_mine:
			i += 1
		# Нижняя правая
		if mines[button.y + 1][button.x + 1].is_mine:
			i += 1
	except:
		pass
	return i

def cells_check(button):
	global mines
	i = []
	try:
		# Верхняя левая
		if button.x != 0 and button.y != 0:
			if not mines[button.y - 1][button.x - 1].is_mine:
				i.append(mines[button.y - 1][button.x - 1])
		# Верхняя
		if button.y != 0:
			if not mines[button.y - 1][button.x].is_mine:
				i.append(mines[button.y - 1][button.x])
		# Верхняя правая
		if button.y != 0:
			if not mines[button.y - 1][button.x + 1].is_mine:
				i.append(mines[button.y - 1][button.x + 1])
		# Левая
		if button.x != 0:
			if not mines[button.y][button.x - 1].is_mine:
				i.append(mines[button.y][button.x - 1])
		# Правая
		if not mines[button.y][button.x + 1].is_mine:
			i.append(mines[button.y][button.x + 1])
		# Нижняя левая
		if not button.x != 0:
			if mines[button.y + 1][button.x - 1].is_mine:
				i.append(mines[button.y + 1][button.x - 1])
		# Нижняя
		if not mines[button.y + 1][button.x].is_mine:
			i.append(mines[button.y + 1][button.x])
		# Нижняя правая
		if not mines[button.y + 1][button.x + 1].is_mine:
			i.append(mines[button.y + 1][button.x + 1])
	except:
		pass
	return i

def zero_test(first_cell):
	cells = [first_cell]
	checked_cells = [first_cell]
	while cells != []:
		i = 0
		print(0)
		while i <= len(cells):
			print(len(cells_check(cells[i])))
			if len(cells_check(cells[i])) == 8:
				print(2)
				for q in range(len(cells_check(cells[i]))):
					if not cells_check(cells[i])[q] in checked_cells:
						cells.append(cells_check(cells[i])[q])
						checked_cells.append(cells_check(cells[i])[q])
			cells.remove(cells[i])
			print(3)
			i += 1
			print('i '+str(i))

	for z in range(len(checked_cells)):
		checked_cells[z].button['text'] = environment_check(checked_cells[z])
		checked_cells[z].button['bg'] = 'white'

def mine_check(button):
	global mines
	if button.is_mine:
		button.button['bg'] = 'red'
	else:
		i = environment_check(button)
		if i == 0:
			zero_test(button)
		else:
			button.button['text'] = str(i)

def game_over():
	exit()

window = Tk()
window.geometry("500x550")

mines = []
generate()

window.mainloop()