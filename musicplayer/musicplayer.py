from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from pygame import mixer
from mutagen.mp3 import MP3 
import os
import time
import tqdm

root=Tk()
root.config(bg="black")
root.geometry("500x600+450+20")
root.title('MyMusicMp3.com')
ph = PhotoImage(file='icon1.png')
root.iconphoto(False, ph)
filename=''
paused=FALSE
ps=TRUE

musicimg = PhotoImage(file="tenor.gif")
startimg=PhotoImage(file="img1.png")
pauseimg=PhotoImage(file="img2.png")
stopimg=PhotoImage(file="stop3.png")
forwardimg=PhotoImage(file="img3.png")
backwardimg=PhotoImage(file="img4.png")
volumeimg=PhotoImage(file="vol.png")
muteimg=PhotoImage(file="mut.png")
paused=FALSE
ps=TRUE
vl=TRUE
total_length = 0
mixer.init()
f1=Label(root,font=("Lucida calligraphy", 12,'bold'),fg='black',bg='black')
f1.place(relx=.30,rely=.07)

def Play():
    global paused,ps
    root.config(bg='medium slate blue')
    f1['bg']='medium slate blue'
    if ps:
        b1['image']=pauseimg
        statusbar['text']=os.path.basename(filename)
        ps=FALSE
        if paused:
            mixer.music.unpause()
            paused=FALSE
        else:
            try:
                mixer.music.load(filename)
                mixer.music.play()
            except:
                root.config(bg='pale violet red')
                f1['bg']='pale violet red'
                b1['image']=startimg
                ps=TRUE
                paused=FALSE
                statusbar['text']="File not found"
                messagebox.showerror('File not found','Please Select the Song !')
    else:
        root.config(bg='light coral')
        f1['bg'] = 'light coral'
        statusbar['text']="Music Paused"
        ps=TRUE
        b1['image']=startimg
        mixer.music.pause()
        paused=TRUE

def Stop():
    global ps,paused
    f1['bg']='IndianRed2'
    statusbar['text']="Music Stopped"
    root.config(bg='IndianRed2')
    ps=TRUE
    paused=FALSE
    b1['image']=startimg
    mixer.music.stop()

def Display():
    global filename
    filename=filedialog.askopenfilename()
    statusbar['text']=os.path.basename(filename)
    Stop()
    Play()
    showdetails()

menubar=Menu(root)
root.config(menu=menubar)
filesubmenu=Menu(menubar,tearoff=0)
filemenu=menubar.add_cascade(label='File',menu=filesubmenu)
filesubmenu.add_command(label='Open',command=Display)

def musiclength():
    pass

def Volume(val):
    if val==0:
        volume=int(val)/100
        mixer.music.set_volume(volume)
        #scale.set(0)
    else:
        volume=int(val)/100
        mixer.music.set_volume(volume)
        scale.set(val)

def Mute():
    global vl
    if vl:
        b5['image']=muteimg
        root.config(bg='turquoise2')
        f1['bg']='turquoise2'
        val=0
        Volume(val)
        vl=FALSE
    else:
        b5['image']=volumeimg
        root.config(bg='medium purple')
        f1['bg']='medium purple'
        val=scale.get()
        Volume(val)
        vl=TRUE

def showdetails():
    global total_length
    file_data=os.path.splitext(filename)
    if file_data[1]=='.mp3':
        audio=MP3(filename)
        total_length=audio.info.length
    print(total_length)
    mins,secs=divmod(total_length,60)
    mins=round(mins)
    secs=round(secs)
    timeformat='{:02d}:{:02d}'.format(mins,secs)
    f1['text']='Total Length'+'-'+timeformat
    musiclength()

ml = Label(root,image=musicimg)
ml.pack(pady=80)
button_frame = Frame(root)
button_frame.config(bg='white')
b1=Button(button_frame,image=startimg,borderwidth=0,command=Play,padx=10,pady=10)
b1.place(relx=.38,rely=.23)
b2=Button(button_frame,image=stopimg,command=Stop,borderwidth=0)
b2.place(relx=.15,rely=.32)
b3=Button(button_frame,image=forwardimg,borderwidth=0)
b3.place(relx=.26,rely=.32)
b4=Button(button_frame,image=backwardimg,borderwidth=0)
b4.place(relx=.54,rely=.32)
b5=Button(button_frame,image=volumeimg,borderwidth=0,command=Mute)
b5.place(relx=.65,rely=.36)
button_frame.pack(fill=BOTH,expand=YES)
scale=Scale(button_frame,from_=0,to=100,orient=HORIZONTAL,relief=RAISED,command=Volume,showvalue=0)
scale.config(borderwidth = 0,activebackground= 'red',bg='black',bigincrement = 10,fg='yellow',highlightthickness=0,sliderlength=10,width=10,state=ACTIVE)
scale.set(20)
scale.place(relx=.75,rely=.47)
#scale1=Scale(root,from_=0,to=100,orient=HORIZONTAL,relief=RAISED,showvalue=10)
#scale1.config(borderwidth = 0,activebackground= 'red',bg='blue',fg='yellow',highlightthickness=0,sliderlength=10,width=5,state=ACTIVE,length=200)
#scale1.set(0)
#scale1.place(relx=.10,rely=.32)
statusbar=Label(root,width=500,height = 1,relief=SUNKEN,font=("Lucida calligraphy", 10,'bold'),fg='white',bg='black')
statusbar.pack(side=BOTTOM)
root.mainloop()
