import youtube_dl
from tkinter import *

def download():
    link = e1.get()
    ydl_opts = {}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

root = Tk()

l1 = Label(root, text="Enter the YouTube link:")
l1.grid(row=0, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

b1 = Button(root, text="Download", command=download)
b1.grid(row=1, column=1)

root.mainloop()
