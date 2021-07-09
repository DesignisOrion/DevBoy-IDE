from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

# allows the code to run in the back of ide before output

ide = Tk()

# name of the ide
ide.title('DevBoy IDE')
file_path = ''


# save
def set_file_path(path):
	global file_path
	file_path = path


# Run Function
def run():
	if file_path == '':
		save_prompt = Toplevel() # prompt for saving work before running
		text = Label(save_prompt, text="Aye....save that work first dev!")
		text.pack()
		return
	command = f'Python {file_path}'
	process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	output, error = process.communicate()
	# show process of output and error
	code_output.insert('1.0', output)
	code_output.insert('1.0', error)

# Open File
def open_file():
	path = askopenfilename(filetypes=[('Python Files', '*.py')])  # saves only python files (of course :P)
	with open(path, 'r') as file:
		# read file
		code = file.read()
		# delete on screen file
		editor.delete('1.0', END)
		# place open file on screen
		editor.insert('1.0', code)
		set_file_path(path)


#  Save As
def save_as():
	if file_path == '':
		path = asksaveasfilename(filetypes=[('Python Files', '*.py')])  # saves only python files (of course :P)
	else:
		path = file_path
	with open(path, 'w') as file:
		# capture all of the code in editor
		code = editor.get('1.0', END)
		file.write(code)
		set_file_path(path)


# menu
menu_bar = Menu(ide)

# file menu
file_menu = Menu(menu_bar, tearoff=0)  # tear off takes the --- from the menu.
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label="File", menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)  # tear off takes the --- from the menu.
run_bar.add_command(label='Run Code', command=run)  # command run is what runs the function called 'run'
menu_bar.add_cascade(label="Run", menu=run_bar)

ide.config(menu=menu_bar)

# text editor space
editor = Text()
editor.pack()

# placing output of code within the ide
code_output = Text(height=10)
code_output.pack()



ide.mainloop()

