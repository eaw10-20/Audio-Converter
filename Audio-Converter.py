from pydub import AudioSegment
from tkinter import *
from tkinter import filedialog, messagebox
import os, os.path


def main():
	# Creating UI
	global root
	root = Tk()
	root.title("Audio Converter")
	# Creating buttons for UI
	Btn1 = Button(root, text="Create ogg", command=to_ogg, width=20, height=2)
	Btn2 = Button(root, text="Create mp3", command=to_mp3, width=20, height=2)
	BtnQuit = Button(root, text='Quit', command=root.quit, width=20, height=2)
	# Placing buttons on UI in grid format
	Btn1.grid(row=0, column=0)
	Btn2.grid(row=1, column=0)
	BtnQuit.grid(row=2, column=0)

	# Creating a space for text (make sure rowspan = # of buttons above)
	textbox_message("Audio Converter\n\nCurrently supports conversion of\nmp3, ogg, wav, flv, and mp4 formats")

	# Loop for running program
	root.mainloop()


def to_ogg():
	cont = True
	textbox_message("Converting to ogg format...")
	# file to be converted
	fileDir = get_Dir()
	# get the full file name from path (e.g. audio.mp3)
	noExten = os.path.splitext(fileDir)[0]

	# test for existence of matching ogg file
	if fileDir == '':
		cont = False
	elif os.path.exists(noExten + ".ogg"):
		#ask if you want to replace old file
		MsgBox = messagebox.askquestion ('Replace existing file','An ogg file already exists. Do you want to replace it?',
			icon = 'warning')
		if MsgBox == 'no':
			cont = False

	# only runs if we're good to create/replace ogg file
	if cont:
		# import in mp3 format
		audio = get_audio(fileDir)

		# export in ogg format
		audio.export(noExten + ".ogg", format="ogg")
		textbox_message("Conversion complete")
	else:
		textbox_message("Audio Converter\n\nCurrently supports conversion of\nmp3, ogg, wav, flv, and mp4 formats")


def to_mp3():
	cont = True
	textbox_message("Converting to mp3 format...")
	# file to be converted
	fileDir = get_Dir()
	# get the full file name from path (e.g. audio.mp3)
	noExten = os.path.splitext(fileDir)[0]

	# test for existence of matching mp3 file
	if fileDir == '':
		cont = False
	elif os.path.exists(noExten + ".mp3"):
		#ask if you want to replace old file
		MsgBox = messagebox.askquestion ('Replace existing file','An mp3 file already exists. Do you want to replace it?',
			icon = 'warning')
		if MsgBox == 'no':
			cont = False

	# only runs if we're good to create/replace ogg file
	if cont:
		# import in ogg format
		audio = get_audio(fileDir)

		# export in mp3 format
		audio.export(noExten + ".mp3", format="mp3")
		textbox_message("Conversion complete")
	else:
		textbox_message("Audio Converter\n\nCurrently supports conversion of\nmp3, ogg, wav, flv, and mp4 formats")


def get_audio(fileDir):
	type = os.path.splitext(fileDir)[1]
	if type=='.ogg':
		return AudioSegment.from_ogg(fileDir)
	elif type=='.mp3':
		return AudioSegment.from_mp3(fileDir)
	elif type=='.wav':
		return AudioSegment.from_wav(fileDir)
	elif type=='flv':
		return AudioSegment.from_flv(fileDir)
	elif type=='.mp4':
		return AudioSegment.from_file(fileDir, 'mp4')
	else:
		print('Warning! Filetype not yet implemented!')


def get_Dir():
	# file to be converted
	fileDir = filedialog.askopenfilename(initialdir="/", title="Select File",
		filetypes=(("All files", "*.*"),("flv", "*.flv"),("mp3", "*.mp3"),("mp4", "*.mp4"),("ogg", "*.ogg"),("wav", "*.wav")))
	# get the full file name from path (e.g. audio.mp3)
	type = os.path.splitext(fileDir)[1]
	if type=='.ogg' or type=='.mp3' or type=='.wav' or type=='.flv' or type=='.mp4':
		return fileDir
	elif type == '':
		return ''
	else:
		messagebox.showerror('Unsupported file format','This file type is not currently supported.')
		return ''


def textbox_message(message):
	global textbox
	textbox = Label(root, text=message, width=50, height=8, fg="white", bg="#252525")
	textbox.grid(row=0, column=1, rowspan=3)


if __name__ == '__main__':
	main()