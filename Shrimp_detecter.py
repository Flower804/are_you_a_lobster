import pygame
from pygame import mixer
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image




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
      
    mainloop()
    
def result2():
    mixer.init()
    sound = mixer.Sound('sound/Kero_Kero_Bonito_Flamengo.mp3')
    
    sound.play()
    
    window = tk.Tk()
    window.title("You made me sad :(")
    
    path = "images/OIP.jpg"
    
    img = ImageTk.PhotoImage(Image.open(path), master=window)
    
    panel = tk.Label(window, image = img)
    
    panel.pack(fill = "both", expand="yes")
    
    mainloop()
    

def scanner():
    window = tk.Tk()
    window.title("The question")
    window.geometry("200x200")
    
    bottom=Frame(window)
    
    text = tk.Label(window,
                    text="Are you a lobster?",
                    font = ("Helvetica", 14))
    
    button = tk.Button(window, text="Yes", command= result1 )
    button2 = tk.Button(window, text="No", command= result2)
    
    bottom.pack(side=BOTTOM, fill=BOTH, expand=TRUE)
    
    #pack stuff
    text.pack(side="top", expand="yes")
    button.pack(in_=bottom, side=LEFT)
    button2.pack(in_=bottom, side=LEFT)
    

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


openNewWindow()
#result1()