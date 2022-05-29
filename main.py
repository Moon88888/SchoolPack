# import everything from tkinter module
from tkinter import *
from tkinter.font import Font

from AirPresent import AirPresent
from Quitz import q
from drowsinessdetection import s
from Game import game
from PIL import ImageTk, Image

# create a tkinter window
root = Tk()
root.title('SchoolPack')
# Open window having dimension 100x100
root.geometry('700x700')

icon = ImageTk.PhotoImage(Image.open("icons\icons8-v-live-256.png"))
label_icon = Label( image=icon)
label_icon.pack()

# Create a Button
root.iconbitmap(r'C:\Users\SUNNIHITHA\PycharmProjects\SchoolPackage\icons\school-director.ico')

btn1 = Button(root, text='Air_Present',  fg='black', bg= 'cyan',  bd = '5',command=AirPresent)
btn1.place( x=170, y=300, height=60, width=140)

btn2 = Button(root, text='Quitz',  fg='black', bg= 'cyan',  bd = '5',command=q)
btn2.place( x=370, y=300, height=60, width=140)

btn3 = Button(root, text='Anti_Sleep',  fg='black', bg= 'cyan',  bd = '5',command=s)
btn3.place( x=170, y=400, height=60, width=140)

btn4 = Button(root, text='Quick_Break',  fg='black', bg= 'cyan',  bd = '5',command=game)
btn4.place( x=370, y=400, height=60, width=140)

btn = Button(root, text = 'EXIT Program', bd = '5', command = root.quit)
btn.pack(side = 'bottom')

root.mainloop()





