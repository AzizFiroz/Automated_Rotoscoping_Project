#import player
import videotoimage
import getSilhoutte
import imagetovideo
import imageroto
import tkinter
import sys
#from tkvideo import tkvideo
# window_main = tkinter.Tk(className=' Auto_Rotoscoping Project', )
# window_main.geometry("600x600")

def OnExit():
    sys.exit()
    window_main.destroy()
window_main=tkinter.Tk()
myCanvas = tkinter.Canvas(window_main, bg="#282a36", height=700, width=600)

button1 = tkinter.Button(window_main, text ="Click for Converting Video to Image frames",
                         command=videotoimage.vidtoimg,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button1.config(width=45, height=3)

button1.place(x=310,y=100,anchor="center")

button2 = tkinter.Button(window_main, text ="Click for Rotoscoping", 
                         command=getSilhoutte.auto,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button2.config(width=45, height=3)
button2.place(x=310,y=200,anchor="center")

button3 = tkinter.Button(window_main, text ="Click for Converting Rotoscoped Images back to Video", 
                         command=imagetovideo.imgtovid,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button3.config(width=45, height=3)
button3.place(x=310,y=300,anchor="center")

button4 = tkinter.Button(window_main, text ="EXIT", 
                         command=window_main.destroy,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button4.config(width=45, height=3)
button4.place(x=310,y=600,anchor="center")

'''
button5=tkinter.Button(window_main, text ="PLAY-VIDEO", 
                         command=player.playing,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button5.config(width=45, height=3)
button5.place(x=310,y=500,anchor="center")
'''
button6=tkinter.Button(window_main, text ="Rotoscope a single IMAGE", 
                         command=imageroto.rotoimg,font = (("Times New Roman"),10),bd=10,relief="ridge",bg="#e8de25")
button6.config(width=45, height=3)
button6.place(x=310,y=400,anchor="center")

myCanvas.pack()
window_main.mainloop()