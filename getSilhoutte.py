import createSilhoutte as fm
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
from os import listdir
from os import chdir
from os import getcwd 
def auto():
    print("HELLO")
    
    # Get the file directory
    root = tk.Tk()
    root.withdraw()
    temp=getcwd()+'\data'
    print(temp)
    directoryName = temp
    #print(directoryName,type(directoryName))
    #filedialog.askdirectory(parent=root, initialdir="/", title = 'Please select a directory')
    '''
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')
    
    '''
    matteHeight = sd.askinteger("Set the matte size", "Output matte vertical resolution (256 recommended for quick tests)?", parent=root,initialvalue=256)
    listOfFiles = listdir(directoryName)
    for currentFile in listOfFiles:
        sourceFile = directoryName + "/" + currentFile
        mainNameEnd = currentFile.find('.')
        nameForMatte = currentFile[:mainNameEnd] + "_matte" + currentFile[mainNameEnd:]
        fullPathMatteName = directoryName + "/" + nameForMatte
        fm.createMatte(sourceFile, fullPathMatteName, matteHeight)
        print("Just created: " + nameForMatte)
    print("END OF ROTOSCOPING")