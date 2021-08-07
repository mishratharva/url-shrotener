from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pyshorteners
import pyperclip
import time



root = Tk()

root.title("URL Shortener")

root.geometry('1920x1080')

load = Image.open(r'C:\Users\mishr\Downloads\img2.jpg')

render = ImageTk.PhotoImage(load)

img = Label(root, image=render, justify='center')

img.place(x=0, y=0)

img1 = PhotoImage(file='C:/Users/mishr/Downloads/button (1).png')

img2 = PhotoImage(file='C:/Users/mishr/Downloads/button.png')

img3 = PhotoImage(file='C:/Users/mishr/Downloads/URL-SHORTENER.png')

lab = Label(root,image=img3, bg="MOCCASIN")

lab.place(x=0, y=0)


def short():


    try:

        link = e.get()

        shortener = pyshorteners.Shortener()

        ur = shortener.tinyurl.short(link)

        global x
        x = str(ur)

        res.insert(0, x)

        b1 = Button(root, image=img1, bg="MOCCASIN", command=cpy)

        b1.pack(pady=0, side=TOP)

        b1.place(x=640, y=370)

    except:

        messagebox.showerror('ERROR ', 'Please Enter a valid URL')


def cpy():

    pyperclip.copy(x)

    time_str = time.asctime()


    l3=Label(root, fg='black', text="Last used at "+time_str,font=('Helvetica',12,"normal"),bg='MOCCASIN')

    l3.pack(pady=7,side=TOP)


e = Entry(root, width=40, font=("Helvetica", 16, "normal"), justify='center', bg='MOCCASIN', fg='black')

bt = Button(root, image=img2, bd=0, bg="MOCCASIN", command=short)

l1 = Label(root, fg='black', text="© 2020 URL-SHORTENER created by Atharva Mishra and Krishn Kunal (INDIA)",
           font=('times', 12, "normal"), bg='MOCCASIN')

l2 = Label(root, fg='black', text="Short links, Big results", font=('Helvetica', 34, "bold"), bg='MOCCASIN')

l3 = Label(root, fg='black', text="Enter URL below:", font=('Helvetica', 22, "bold"), bg='MOCCASIN')

res = Entry(root, width=40, font=("Helvetica", 16, "normal"), justify='center', bg='MOCCASIN', fg='black')

lab.pack(pady=10, side=TOP)

l3.pack(pady=20, side=TOP)

e.pack(pady=10, side=TOP)

bt.pack(pady=10, side=TOP)

res.pack(pady=10, side=TOP)

l2.pack(pady=110, side=TOP)

l1.pack(pady=10, side=TOP)

root.mainloop()
