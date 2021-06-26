#####################
#Name: Read Dragon Brower Main Program
#Author: Yukikawa(TinQlo)
#####################

import tkinter as tk
import tkinter.font as tf
import tkinter.messagebox as msgbx

def ButtonClick():
    msgbx.showinfo('You Stupid!','404 Not Found\nPlease check your connection')

MainWindow = tk.Tk()
MainWindow.geometry('900x500+100+100')
MainWindow.title('Dragon Browser v0.1')
fontStyle = tf.Font(family="Consolas", size=50)
MainLabel = tk.Label(MainWindow,text='Dragon Browser',font=fontStyle)
MainLabel.place(x=200,y=50)

MainEntry =tk.Entry(MainWindow,width=100)
MainEntry.place(x=100,y=150)

MainButton = tk.Button(MainWindow,text='Search!',width=30,command=ButtonClick)
MainButton.place(x=300,y=200)


MainWindow.mainloop()