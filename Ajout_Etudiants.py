
from tkinter import *
from tkinter.filedialog import *
import tkinter as tk
import os
from tkinter import filedialog
from PIL import Image, ImageTk #python3-pil.inagetk python3-inaging-tk

#variables


def showimage():
    global im
    path = filedialog.askopenfilename(filetypes=[("Image File", '.jpeg')])
    im = Image.open(path)
    resize_image = im.resize((150, 160))
    tkimage = ImageTk.PhotoImage(resize_image)
    myvar = Label(logo, image=tkimage,width=150,height=160)
    myvar.image = tkimage
    myvar.place(x=220,y=100)

def savedata():
    fullname = nominput.get()+" " + prenominput.get()
    imgname = "ImagesAttendance/"+fullname+".jpeg"
    im.save(imgname)
    print("Image saved")
    nominput.delete(0,END)
    prenominput.delete(0, END)
    imageCanvas.place(x=220,y=100)

main = Tk()
main.title("Gestion Absence")
main.geometry("450x380+180+50")

logo = Canvas(main,width=450,height=380,bg="#135896")
logo.place(x=0,y=10)

log = Label(logo,bg="#135896",text="Gestion Absence",font=('arial',19,'bold'),fg="black")
log.place(x=110,y=10)

#FORMULAIRE

identifiant = Label(logo,text="Nom",bg="#135896",font=('arial',13,'bold'),fg="white")
identifiant.place(x=10,y=100)

mdp = Label(logo,text="Prenom",bg="#135896",font=('arial',13,'bold'),fg="white")
mdp.place(x=10,y=160)

nominput = Entry(logo,width=15,relief=FLAT,font=('arial,12'))
nominput.place(x=12,y=130)

prenominput = Entry(logo,width=15,relief=FLAT,font=('arial,12'))
prenominput.place(x=12,y=190)

#Button

saveetudiant = Button(logo,width=15,text="Sauvegarder",bg="#135896",fg="white",font=('arial',12),command=savedata)
saveetudiant.place(x=18,y=230)

browseImage = Button(logo,text="Importer image",bg="#135896",fg="white",font=('arial',10),command=showimage)
browseImage.place(x=245,y=270)

#MONTRER IMAGE
imageCanvas = Canvas(logo,bg="gray",width=150,height=160)
imageCanvas.place(x=220,y=100)



main.mainloop()







