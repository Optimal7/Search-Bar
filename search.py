# Imports
from tkinter import *
import tkinter as tk
import webbrowser
import os

#Chrome Path, Python3 and up uses Microsoft Edge or IE as defualt when opening for some reason. Just change if needed
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#Basic Vars
win = tk.Tk()
font = "Arial"

#Window Details
win.title("Search Bar") #The Title of the program
win.geometry("400x80") #The size of the application on start
win.resizable(height=False, width=False) #Makes it so you can't go Fullscreen
win.iconphoto(False, tk.PhotoImage(file='icon.png')) #Window Icon

#Gets the chrome path and opens the link you gave.
Tk.attributes
def search():
    url = entry.get()
    webbrowser.get(chrome_path).open(url)

#GitHub Repo button
def repo():
    webbrowser.get(chrome_path).open("https://github.com/Optimal7/Search-Bar")
label1 = Label(win,text="Enter URL Here:    "
               ,font=(f"{font}",10,"bold"))
label1.grid(row=0,column=0)

# Search Bar
entry = Entry(win,width=40)
entry.grid(row=0,column=1)

#Made by Optimal7 Text
label1 = Label(win,text="Made by Optimal7"
               ,font=(f"{font}",10,"bold"))
label1.grid(row=1,column=0)

#Search Button
button = Button(win,text="Search",command=search)
button.grid(row=1,column=0,columnspan=2,pady=10)

#GitHub Repo Button
button = Button(win,text="Github Repo",command=repo)
button.grid(row=1,column=1,columnspan=2,pady=10)

#This is requried
win.mainloop()