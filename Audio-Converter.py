from pydub import AudioSegment
from tkinter import *
from tkinter import filedialog # why do I need this?!?!?!?!?!
import os

root = Tk()

def mp3_to_ogg():
	# file to be converted
	fileDir = filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("mp3", "*.mp3"),))
	# get the full file name from path (e.g. audio.mp3)
	noExten = os.path.splitext(fileDir)[0]
	# get the file name from the full name (e.g. audio)
	# fileName = os.path.basename(noExten)

	# AudioSegment is from pydub
	# import in mp3 format
	audio = AudioSegment.from_mp3(fileDir)

	# export in ogg format
	audio.export(noExten + ".ogg", format="ogg")


# Creating a Lable Widget
# myLabel = Label(root, text="Audio Converter")

# Shove widget onto screen
# myLabel.grid(row=0, column=0)

# Creating a button
myButton = Button(root, text="mp3 to ogg", command=mp3_to_ogg)
myButton.pack()

# Loop for running program
root.mainloop()