from tkinter import *


def main():
	root = Tk()
	root.title("Text output")
	root.geometry("250x150+300+300")
	
	# function Hello
	def printText(event):
		print('Hello!')


	button = Button(root,text='Вывод текста', width=12, height=2)   # Create button
	
	button.bind('<Button>', printText)  # The left mouse button click with the output text

	button.pack()   # Button on the main screen
	root.mainloop() # Endless cycle

main()