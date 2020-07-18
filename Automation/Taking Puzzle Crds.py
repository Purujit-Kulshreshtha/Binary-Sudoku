#importing required modules
import tkinter as tk
import os
import time

#color scheme
BLACK = "#2A2A2A"
BLUE = "#35B8D5"
RED = "#D55336"
BG = "#222222"
WHITE = "#FFFFFF"
BOLD_FONT = ("Arial", 20, "bold")
FONT = ("Arial", 15, "bold")

#default variables
CURRENT_DIR = os.getcwd()
DATA_DIR = CURRENT_DIR + "\\Ohh1_Automation_Data"
WIDTH = "500"
HEIGHT = "500"
DIMS = f"{WIDTH}x{HEIGHT}"

#window creation
window = tk.Tk()
window.title("Oh h1 Automation")
window.geometry(DIMS)
window.configure(bg = BG)

#title
top_label = tk.Label(window, text = "Oh h1 Automation", bg = RED, fg = WHITE, font = BOLD_FONT, width = WIDTH)
top_label.pack()


#input fields

#radio buttons, puzzle type
puzzle_type_info = tk.IntVar()


type_header = tk.Label(window, text = "Puzzle Types", font = BOLD_FONT, bg = BLACK, fg = WHITE, width = WIDTH)
type_header.pack()

empty_label = tk.Label(window, bg = BG).pack()

free_play = tk.Radiobutton(
		window,
		bg = BG,
		text = "Free Play",
		value = 1,
		font = FONT,
		fg = WHITE,
		variable = puzzle_type_info)
free_play.pack()

today_play = tk.Radiobutton(
		window,
		bg = BG,
		text = "Today's Puzzle",
		value = 2,
		font = FONT,
		fg = WHITE,
		variable = puzzle_type_info)
today_play.pack()

empty_label = tk.Label(window, bg = BG).pack()

#input, puzzle size
size_header = tk.Label(window, text = "Puzzle Size", font = BOLD_FONT, bg = BLACK, fg = WHITE, width = WIDTH)
size_header.pack()

empty_label = tk.Label(window, bg = BG).pack()

puzzle_size_label = tk.Label(window, text = "Enter puzzle size:", font = FONT, bg = BG, fg = WHITE)
puzzle_size_label.pack()

empty_label = tk.Label(window, bg = BG).pack()

puzzle_size_entry = tk.Entry(window, font  = FONT, bg = BLACK, fg = WHITE)
puzzle_size_entry.pack()

#write data
def invalid_entry():
	#checks if entry is valid and changes window as needed

	save_button_valid.destroy()

	invalid_label = tk.Label(window, text = "Invalid Entry!", fg = RED, font  = FONT, bg = BG)
	invalid_label.pack()

	empty_label = tk.Label(window, bg = BG).pack()

	save_button_invalid = tk.Button(window, text = "Save", font = BOLD_FONT, bg = BLUE, fg = WHITE, command = write_data)
	save_button_invalid.pack()

def valid_entry():
	#default widnow for valid entry
	global save_button_valid

	empty_label = tk.Label(window, bg = BG).pack()

	save_button_valid = tk.Button(window, text = "Save", font = BOLD_FONT, bg = BLUE, fg = WHITE, command = write_data)
	save_button_valid.pack()


def write_data():
	#writes data to data file
	global written

	puzzle_sizes_list = ["4", "6", "8", "12"]
	size = puzzle_size_entry.get()
	if size == "":
		size = "6"

	if size not in puzzle_sizes_list:
		invalid_entry()

	else:
		puzzle_type_data = puzzle_type_info.get()

		puzzle_type = "Free Play"

		if puzzle_type_data == 1:
			puzzle_type = "Free Play"
		elif puzzle_type_data == 2:
			puzzle_type = "Today's Puzzle"

		if not os.path.isdir(DATA_DIR):
			os.mkdir(DATA_DIR)

		os.chdir(DATA_DIR)

		creds_file = open("Creds.txt", "w")
		creds_file.write(puzzle_type + "\n")
		creds_file.write(size + "\n")
		creds_file.close()

		print("Data written")

		written = True

		time.sleep(1)

		if written:
			window.destroy()

valid_entry()

window.mainloop()