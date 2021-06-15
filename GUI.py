import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from main import *

audioFile=''

def loadAudio():
    global audioFile
    audioFile = askopenfilename(filetypes = (('audio file','*.mp3 *.wav'),))
    if len(audioFile)>0:
        fileLabel.configure(text="1 file selected")

def reset():
    thr1Slider.set(25)
    thr2Slider.set(50)
    thr3Slider.set(75)
    contToleranceSlider.set(40)
    contMinSlider.set(20)
    slotSlider.set(100)

def analyze():
    if len(audioFile)>0:
        pattern,cont=getHapticaPattern(audioFile,thr1Slider.get(),thr2Slider.get(),thr3Slider.get(),slotSlider.get()/1000,contToleranceSlider.get(),contMinSlider.get())
        patternText.delete(1.0,"end")
        patternText.insert(1.0, pattern)
        contText.delete(1.0, "end")
        contText.insert(1.0, cont)

root = tk.Tk()
root.geometry('570x620+250+100')
root.resizable(False, False)
root.title('Put matplotlib\'s pie chart on tkinter')

tk.Button(root, text='Select File', width=13,fg='blue',bg='white',command=loadAudio).place(x=10, y=10)

thr1Slider=tk.Scale(root,from_=0,to=100,orient=HORIZONTAL)
thr1Slider.pack()
thr1Slider.place(x=10, y=50)
thr1Slider.set(25)
tk.Label( root,text = "Threshold-1 (%)").place(x = 10,y = 90)

thr2Slider=tk.Scale(root,from_=0,to=100,orient=HORIZONTAL)
thr2Slider.pack()
thr2Slider.place(x=10, y=120)
thr2Slider.set(50)
tk.Label( root,text = "Threshold-2 (%)").place(x = 10,y = 160)

thr3Slider=tk.Scale(root,from_=0,to=100,orient=HORIZONTAL)
thr3Slider.pack()
thr3Slider.place(x=10, y=190)
thr3Slider.set(75)
tk.Label( root,text = "Threshold-3 (%)").place(x = 10,y = 230)

contToleranceSlider=tk.Scale(root,from_=0,to=100,orient=HORIZONTAL)
contToleranceSlider.pack()
contToleranceSlider.place(x=10, y=260)
contToleranceSlider.set(40)
tk.Label( root,text = "Cont-Tolerance (%)").place(x = 10,y = 300)

contMinSlider=tk.Scale(root,from_=0,to=100,orient=HORIZONTAL)
contMinSlider.pack()
contMinSlider.place(x=10, y=330)
contMinSlider.set(20)
tk.Label( root,text = "Cont-MinLength (%)").place(x = 10,y = 370)

slotSlider=tk.Scale(root,from_=100,to=1000,orient=HORIZONTAL)
slotSlider.pack()
slotSlider.place(x=10, y=400)
slotSlider.set(100)
tk.Label( root,text = "Slot Duarion (millis)").place(x = 10,y = 440)

fileLabel=tk.Label( root,text = "no file selected", width=13)
fileLabel.place(x = 10,y = 500)

tk.Button(root, text='Reset', width=13,fg='red',bg='white',command=reset).place(x=10, y=550)
tk.Button(root, text='Analyze', width=13,fg='green',bg='white',command=analyze).place(x=10, y=580)

tk.Label( root,text = "Haptica Pattern", width=11).place(x=130,y=10)
patternText = Text(root, height = 5, width = 52)
patternText.place(x=130,y=40)


tk.Label( root,text = "Continuous Pattern", width=14).place(x=130,y=140)
contText = Text(root, height = 27, width = 52)
contText.place(x=130,y=170)


root.mainloop()