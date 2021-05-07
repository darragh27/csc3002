#!/usr/bin/python

import tkinter as tk
from tkinter.filedialog import askopenfilename

root =tk.Tk()

button= tk.Button(root, text = "select an audio file", bg ='red', fg= 'white', command = lambda: file_opener())
button.pack()

canvas=tk.Canvas(root, height=700, width=800)
canvas.pack

def file_opener():
	filename = askopenfilename()
	print(filename)

root.mainloop()
