import pygame, tkinter, os
from tkinter.filedialog import askdirectory

player = tkinter.Tk()
player.title("UB Social Music")
player.geometry("300x300")

var = tkinter.StringVar()
var.set("Escolha a música")

os.chdir(askdirectory())
songlist = os.listdir()

playing = tkinter.Listbox(player,width=28,selectmode=tkinter.SINGLE)

for item in songlist:
    playing.insert(0,item)

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(playing.get(tkinter.ACTIVE))
    name = playing.get(tkinter.ACTIVE)
    var.set(f"{name[:30]}..." if len(name)>18 else name)
    pygame.mixer.music.play()

def pause():
    pygame.mixer.music.pause()

def resume():
    pygame.mixer.music.unpause()

text = tkinter.Label(player,textvariable=var).grid(row=0,columnspan=3)
playing.grid(columnspan=3)

playB = tkinter.Button(player,width=7,height=1,text="Play",command=play).grid(row=2,column=0)
pauseB = tkinter.Button(player,width=7,height=1,text="Pause",command=pause).grid(row=2,column=1)
resumeB = tkinter.Button(player,width=7,height=1,text="Resume",command=resume).grid(row=2,column=2)
player.mainloop()
