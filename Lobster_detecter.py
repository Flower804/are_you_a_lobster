import pygame
from pygame import mixer
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image


#TODO: try to put the sounds as global so it's easier to stop the autios
#TODO: add dinamic logos yk what it means

#def on_close():

#images stuff

def result1():
    #load sound stuff
    mixer.init()
    sound = mixer.Sound('sound/blue_shrimp.mp3')
    
    sound.play()
    
    window = tk.Tk()
    window.title("GOT YOU SUCKER")
    
    path = "images/R.jpg"

    img = ImageTk.PhotoImage(Image.open(path), master=window)
    
    panel = tk.Label(window, image = img)
    
    
    #Pack stuff  
    panel.pack( fill = "both", expand = "yes")
    window.protocol("WM_DELETE_WINDOW", )#create FUNC to stop audio and impletent it
    window.mainloop()
    
def result2():
    mixer.init()
    sound = mixer.Sound('sound/Kero_Kero_Bonito_Flamengo.mp3')
    
    sound.play()
    
    window = tk.Tk()
    window.title("You made me sad :(")
    
    path = "images/OIP.jpg"
    
    img = ImageTk.PhotoImage(Image.open(path), master=window)
    label = tk.Label(window,
                     text="you made the lobster sad",
                     font=("Helvetica", 14))
    
    panel = tk.Label(window, image = img)
    
    label.pack(fill = "both", expand="yes")
    panel.pack(fill = "both", expand="yes")
    
    
    mainloop()
    

def scanner(): #second window
    window = tk.Tk()
    window.title("The question")
    window.geometry("200x200")
    
    bottom=Frame(window)
    
    text = tk.Label(window,
                    text="Are you a lobster?",
                    font = ("Helvetica", 14))
    
    button = tk.Button(window, text="Yes", command= result1, width=5)
    button2 = tk.Button(window, text="No", command= result2, width=5)
    
    bottom.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    
    #pack stuff
    text.pack(side="top", expand="yes")
    button.pack(in_=bottom, side=LEFT,  expand ="yes")
    button2.pack(in_=bottom, side=LEFT, expand="yes")
    

def openNewWindow():
    window = tk.Tk()
    window.title("Shrimp detector")
    window.geometry("500x500")
    
    path = "images/tipical_lobster.jpg"
    text = tk.Label(window,
                    text="Shrimp Detector",
                    font = ("Helvetica", 14))
    img = ImageTk.PhotoImage(Image.open(path))
    
    panel = tk.Label(window, image = img)
    
    button = tk.Button(window, text="Start detecting", command=scanner)
    
    #Pack stuff  
    text.pack(side= "top", expand= "yes")
    panel.pack( fill = "both", expand = "yes")
    button.pack(side = "bottom",expand = "yes")
      
    mainloop()


openNewWindow() #1ºwindow

#result1()       #final window/1
