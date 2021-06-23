def unmutemusic():
    global currentvol
    root.unmutebutton.grid_remove()
    root.mutebutton.grid()
    mixer.music.set_volume(currentvol)

def mutemusic():
    global currentvol
    root.mutebutton.grid_remove()
    root.unmutebutton.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)

def resumemusic():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()

def volumeup():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol+0.1)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100
            
def volumedown():
    vol=mixer.music.get_volume()
    mixer.music.set_volume(vol-0.1)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100

def stopmusic():
    mixer.music.stop()

def pausemusic():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()

def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    ProgressbarMusicLabel.grid()
    mixer.music.play()
    Song=MP3(ad)
    totalsonglength=int(Song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
     
    def Progressbarmusictick():
        CurrentSongLength=mixer.music.get_pos()//1000
        ProgressbarMusic['value']=CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()

def musicurl():
    dd = filedialog.askopenfilename()
    audiotrack.set(dd)
    

def createwidthes():
    global imbrowse, implay, impause, imvolumeup, imvolumedown, imstop, imresume, immute, imunmute
    global AudioStatusLabel, ProgressbarVolumeLabel, ProgressbarLabel, ProgressbarVolume
    global ProgressbarMusicLabel,  ProgressbarMusic, ProgressbarMusicEndTimeLabel, ProgressbarMusicStartTimeLabel
    
    ############################################################################## Images Register
    imbrowse=PhotoImage(file='browsing.png')
    implay=PhotoImage(file='play.png')
    impause=PhotoImage(file='pause.png')
    imvolumeup=PhotoImage(file='volumeup.png')
    imstop=PhotoImage(file='stop.png')  
    imvolumedown=PhotoImage(file='volumedown.png')
    imresume=PhotoImage(file='pause2.png')
    immute=PhotoImage(file='mute.png')
    imunmute=PhotoImage(file='unmute.png')

    ############################################################################ Change image size
    imbrowse=imbrowse.subsample(15,15)
    implay=implay.subsample(19,19)
    impause=impause.subsample(19,19)
    imvolumeup=imvolumeup.subsample(18,18)
    imstop=imstop.subsample(20,20)
    imvolumedown=imvolumedown.subsample(18,18)
    imresume=imresume.subsample(20,20)
    immute=immute.subsample(20,20)
    imunmute=imunmute.subsample(20,20)

    ############################################################################## Labels
    Tracklable = Label(root, text='Select Audio Track ', bg='white',font=('Arial',16,'bold'))
    Tracklable.grid(row=0,column=0,padx=20,pady=20)

    ############################################################################# Entry Box
    TrackLabelEntry = Entry(root, font=('Arial',16,'bold'),width=35, textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)

    ############################################################################ Buttons
    BrowseButton=Button(root,text='Browse ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green'
    ,image=imbrowse,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    PlayButton=Button(root,text='Play ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green',image=implay,compound=RIGHT,command=playmusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    root.PauseButton=Button(root,text='Pause ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green',image=impause,compound=RIGHT,command=pausemusic)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)

    root.ResumeButton=Button(root,text='Resume ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green',image=imresume,compound=RIGHT,command=resumemusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()
    
    VolumeUpButton=Button(root,text='Volume Up ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green',image=imvolumeup,compound=RIGHT,command=volumeup)
    VolumeUpButton.grid(row=1,column=2,padx=20,pady=20)

    StopButton=Button(root,text='Stop ',bg='white',font=('Arial',16,'bold'),width=150,bd=4,activebackground='green',image=imstop,compound=RIGHT,command=stopmusic)
    StopButton.grid(row=2,column=0,padx=20,pady=20)

    VolumeDownButton=Button(root,text='Volume Down ',bg='white',font=('Arial',16,'bold'),width=190,bd=4,activebackground='green',image=imvolumedown,compound=RIGHT,command=volumedown)
    VolumeDownButton.grid(row=2,column=2,padx=20,pady=20)

    root.mutebutton=Button(root,text='Mute',width=150,bg='white',activebackground='black',bd=4,image=immute,compound=RIGHT,command=mutemusic)
    root.mutebutton.grid(row=3,column=2,padx=20,pady=20)

    root.unmutebutton=Button(root,text='UnMute',width=150,bg='white',activebackground='black',bd=4,image=imunmute,compound=RIGHT,command=unmutemusic)
    root.unmutebutton.grid(row=3,column=2,padx=20,pady=20)
    root.unmutebutton.grid_remove()

    ############################################################################### Progress Bar Volume
    ProgressbarLabel = Label(root,text='',bg='black')
    ProgressbarLabel.grid(row=0, column=3,rowspan=3,pady=20,padx=20)

    ProgressbarVolume = Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)
    
    ProgressbarVolumeLabel = Label(ProgressbarLabel,text='0',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

    ######################################################################################### Progress Bar
    ProgressbarMusicLabel=Label(root,text='',bg='black')
    ProgressbarMusicLabel.grid(row=3, column=0,columnspan=3,pady=20,padx=20)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicStartTimeLabel=Label(ProgressbarMusicLabel,text='00:00',bg='white')
    ProgressbarMusicStartTimeLabel.grid(row=0, column=0)

    ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode='determinate',value=50)
    ProgressbarMusic.grid(row=0,column=1,ipadx=170,ipady=3)


    ProgressbarMusicEndTimeLabel=Label(ProgressbarMusicLabel,text='0:00:0',bg='white')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)



from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
from mutagen.m4a import M4A
root = Tk()
root.geometry('1020x500+200+50')
root.title('Simple Music Player')
root.iconbitmap('music.ico')
root.resizable (False,False)
root.configure(bg='darkslategray')

############################################################################### Global variable
audiotrack=StringVar()
currentvol=0
totalsonglength=0
mixer.init()
createwidthes()
root.mainloop()
