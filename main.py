from tkinter import *
from random import randint as rnd

class Cell():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.is_mine = False
		self.environment_mines = []
		self.environment_empties = []
		self.button = Button(window, text = "", bg='grey', command = lambda: player_move(self))
		self.button.place(x = x * 50, y = y * 50 + 50, width = 50, height = 50)

def generate():
	global mines
	# Генерация поля
	for y in range(10):
		mines.append([])
		for x in range(10):
			mines[y].append(Cell(x, y))

	# Генерация мин
	i = 0
	while i != 10:
		mine_x = rnd(0, 9)
		mine_y = rnd(0, 9)
		if mines[mine_y][mine_x].is_mine:
			i -= 1
		else:
			mines[mine_y][mine_x].is_mine = True
		i += 1

	# Обозначение номера
	for y2 in range(len(mines)):
		for x2 in range(len(mines[y2])):
			if not mines[y2][x2].is_mine:
				environment_check(mines[y2][x2])

def environment_check(button):
	global mines
	# Верхняя левая
	if button.x != 0 and button.y != 0:
		if mines[button.y - 1][button.x - 1].is_mine:
			button.environment_mines.append(mines[button.y - 1][button.x - 1])
		else:
			button.environment_empties.append(mines[button.y - 1][button.x - 1])

	# Верхняя
	if button.y != 0:
		if mines[button.y - 1][button.x].is_mine:
			button.environment_mines.append(mines[button.y - 1][button.x])
		else:
			button.environment_empties.append(mines[button.y - 1][button.x])

	# Верхняя правая
	try:
		if button.y != 0 and button.x != len(mines[0]):
			if mines[button.y - 1][button.x + 1].is_mine:
				button.environment_mines.append(mines[button.y - 1][button.x + 1])
			else:
				button.environment_empties.append(mines[button.y - 1][button.x + 1])
	except:
		pass

	# Левая
	if button.x != 0:
		if mines[button.y][button.x - 1].is_mine:
			button.environment_mines.append(mines[button.y][button.x - 1])
		else:
			button.environment_empties.append(mines[button.y][button.x - 1])

	# Правая
	try:
		if button.x != len(mines[0]):
			if mines[button.y][button.x + 1].is_mine:
				button.environment_mines.append(mines[button.y][button.x + 1])
			else:
				button.environment_empties.append(mines[button.y][button.x + 1])
	except:
		pass

	# Нижняя левая
	try:
		if button.x != 0 and button.y != len(mines):
			if mines[button.y + 1][button.x - 1].is_mine:
				button.environment_mines.append(mines[button.y + 1][button.x - 1])
			else:
				button.environment_empties.append(mines[button.y + 1][button.x - 1])
	except:
		pass

	# Нижняя
	try:
		if button.y != len(mines):
			if mines[button.y + 1][button.x].is_mine:
				button.environment_mines.append(mines[button.y + 1][button.x])
			else:
				button.environment_empties.append(mines[button.y + 1][button.x])
	except:
		pass

	# Нижняя правая
	try:
		if button.y != len(mines) and button.x != len(mines[0]):
			if mines[button.y + 1][button.x + 1].is_mine:
				button.environment_mines.append(mines[button.y + 1][button.x + 1])
			else:
				button.environment_empties.append(mines[button.y + 1][button.x + 1])
	except:
		pass

def player_move(button):
	global mines, game, opened_cells, label
	if game:
		if button.is_mine:
			game = False
			label['text'] = 'GAME OVER'
			all_mines_find()
		else:
			if len(button.environment_mines) == 0:
				zero_test(button)
			else:
				button.button['text'] = str(len(button.environment_mines))
			button.button['bg'] = 'white'
			if not button in opened_cells:
				opened_cells.append(button)
	if len(opened_cells) >= 90:
		game = False
		label['text'] = 'YOU WIN'
	print(len(opened_cells))

def zero_test(first_cell):
	global opened_cells
	checking_cells = [first_cell]
	checked_cells = []

	while len(checking_cells) != 0:
		for i in range(len(checking_cells)):
			try:
				if not checking_cells[i] in checked_cells:
					checked_cells.append(checking_cells[i])
				for q in checking_cells[i].environment_empties:
					if len(q.environment_mines) == 0 and not q.is_mine and not q in checked_cells:
						checking_cells.append(q)
				del checking_cells[i]
			except:
				pass

	for z in range(len(checked_cells)):
		checked_cells[z].button['bg'] = 'white'
		opened_cells.append(checked_cells[z])

def all_mines_find():
	for y in range(len(mines)):
		for x in range(len(mines[y])):
			if mines[y][x].is_mine:
				mines[y][x].button['bg'] = 'red'

window = Tk()
window.geometry("500x550")
window.resizable(False, False)

label = Label(window, text = "")
label.place(x = 0, y = 0, width = 500, height = 50)

mines = []
game = True
opened_cells = []
generate()

window.mainloop()