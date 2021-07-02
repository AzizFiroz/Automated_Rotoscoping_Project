import createSilhoutte as fm
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
from os import listdir


def rotoimg():
    root = tk.Tk()
    root.withdraw()
    imagePath = filedialog.askopenfilename( initialdir="/", title = 'Please select an IMAGE')
    p=imagePath
    # nameForMatte = currentFile[:mainNameEnd] + "_matte" + currentFile[mainNameEnd:]
    matteHeight = sd.askinteger("Set the matte size", "Output matte vertical resolution (256 recommended for quick tests)?", parent=root,initialvalue=256)
    
    
    fm.createMatte(p, "rotoimage.jpg", matteHeight)
    
    print("Just created: ")