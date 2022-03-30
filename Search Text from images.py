#This application uses tkinter, cv2, tesseract libraries.
#Before using this app you have to intall tesseract
#Yerkebulan Zhaiylkan - yerkkee@gmail.com

import tkinter
import cv2
import pytesseract
import glob
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog as fd

#You must show tesseract's directory.
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # Direcotry of the tesseract
tessdata_dir_config = r'--oem 3 --psm 6 --tessdata-dir "C:\Program Files\Tesseract-OCR\tessdata"' # You can change the config values
listFile = glob.glob("C:\Documents\python\WordSearch\*.png") #The base directory where the program will look for the words written in the text box.

#---There is a config for reading from Russian.---
#img2 = cv2.imread('C:\Documents\python\WordSearch\kaz.png')
#img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
#print(pytesseract.image_to_string(img, config=config))
#print(pytesseract.image_to_string(img2, lang='rus+eng', config=tessdata_dir_config))
#print(glob.glob("C:\Documents\python\WordSearch\*"))

#cv2.imshow('Result', img)
#cv2.waitKey(0)

root = Tk()
root.title('Search word from png')
root.resizable(False, False)
root.geometry('300x150')
e = Entry(root, width=50)
e.place(x=10, y=10)
e.grid(row=2, column=2)
e.pack()

my_list = list()

def myClick():
    my_list.clear()
    for i in listFile:
        img = cv2.imread(i)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        config = r'--oem 3 --psm 6'
        allString = pytesseract.pytesseract.image_to_string(img, config=config)
        if allString.find(e.get()) == -1:
            continue
        else: 
            my_list.append(i)
    
    for i in my_list:
        myLabel = Label(root, text=i)
        myLabel.pack()

myButton = Button(root, text="Search", command=myClick)
myButton.pack()
myButton.place(x=250, y=30)

root.mainloop()