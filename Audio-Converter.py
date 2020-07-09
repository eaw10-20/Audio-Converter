from pydub import AudioSegment
from tkinter import *
from tkinter import filedialog, messagebox # why do I need this?!?!?!?!?!
import os, os.path

root = Tk()
root.title("Audio Converter")

def mp3_to_ogg():
	cont = True
	# file to be converted
	fileDir = filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("mp3", "*.mp3"),))
	# get the full file name from path (e.g. audio.mp3)
	noExten = os.path.splitext(fileDir)[0]

	# test for existence of matching ogg file
	if fileDir == '':
		cont = False
	elif os.path.exists(noExten + ".ogg"):
		#ask if you want to replace old file
		MsgBox = messagebox.askquestion ('Replace existing file','An ogg file already exists. Do you want to replace it?',
			icon = 'warning')
		if MsgBox != 'yes':
			cont = False

	# only runs if we're good to create/replace ogg file
	if cont:
		# import in mp3 format
		audio = AudioSegment.from_mp3(fileDir)

		# export in ogg format
		audio.export(noExten + ".ogg", format="ogg")


# Creating a Lable Widget
# 

# Shove widget onto screen
# 

# Creating a button for mp3 to ogg
Btn1 = Button(root, text="mp3 to ogg", command=mp3_to_ogg, width=20, height=2)
Btn2 = Button(root, text="ogg to mp3", width=20, height=2)
Btn1.grid(row=0, column=0)
Btn2.grid(row=1, column=0)

# Creating a space for text
textbox = Label(root, text="Audio Converter", width=50, height=5, fg="white", bg="#252525")
textbox.grid(row=0, column=1, rowspan=2)

# Loop for running program
root.mainloop()