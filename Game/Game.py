import pygame

#initialize pygame moduke
pygame.init()

#default parameters and design scheme
CO_1 = (225, 225, 0)
CO_2 = (0, 225, 225)
BLACK = (42, 42, 42)
BG = (22, 22, 22)
WHITE = (255, 255, 255)
BOLD_FONT = ("Arial", 20, "bold")
FONT = ("Arial", 15, "bold")
DIMS = (800, 800) #dimenssions

#window config
window = pygame.display.set_mode(DIMS)
pygame.display.set_caption("Binary Sudoku")

#classes

#blocks
class block():
	def __init__(self, x_pos, y_pos, width, height, val):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.width = width
		self.height = height
		self.val = val #value

#empty block
class empty_block(block):
	def __init__(self, x_pos, y_pos, width, height,  val):
		super().__init__(x_pos, y_pos, width, height, val)
		self.color = BLACK
		self.trans = (self.x_pos, self.y_pos, self.width, self.height) #transform

	def draw(self):
		pygame.draw.rect(window, self.color, self.trans)

#yellow block
class yellow_block(block):
	def __init__(self, x_pos, y_pos, width, height,  val):
		super().__init__(x_pos, y_pos, width, height, val)
		self.color = CO_1
		self.trans = (self.x_pos, self.y_pos, self.width, self.height)

	def draw(self):
		pygame.draw.rect(window, self.color, self.trans)

#green block
class blue_block(block):
	def __init__(self, x_pos, y_pos, width, height,  val):
		super().__init__(x_pos, y_pos, width, height, val)
		self.color = CO_2
		self.trans = (self.x_pos, self.y_pos, self.width, self.height) 

	def draw(self):
		pygame.draw.rect(window, self.color, self.trans)

#gameloop
play = True

while play:
	window.fill((BG))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			play = False

	#tests
	test_block_1 = empty_block(20, 20, 20, 20, 0)
	test_block_1.draw()
	test_block_2 = yellow_block(80, 80, 20, 20, 1)
	test_block_2.draw()
	test_block_3 = blue_block(140, 140, 20, 20, 2)
	test_block_3.draw()

	pygame.display.update()
pygame.quit()

