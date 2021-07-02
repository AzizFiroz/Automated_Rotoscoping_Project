import cv2
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog as sd
def vidtoimg():
    #print("HELLO")
    
    root = tk.Tk()
    root.withdraw()
    VideoPath = filedialog.askopenfilename(parent=root, initialdir="/", title = 'Please select a Video')
    cap = cv2.VideoCapture(VideoPath)
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print ('Error: Creating directory of data')
    currentFrame = 10
    ret=True
    while(ret):
        ret, frame = cap.read()
        if ret:
            name = './data/frame' + str(currentFrame) + '.jpg'
            print ('Creating...' + name)
            cv2.imwrite(name, frame)
            currentFrame += 1
    cap.release()
    cv2.destroyAllWindows()
    print("END OF CONVERSION")

    