from tkinter import *
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1031))

a=""

msg = s.recv(100)
a += msg.decode("utf-8")

rt = Tk()
rt.geometry("600x100")
l1 = Label(rt, text=a, font=(22))


def ert():
    rt.destroy()


btn = Button(rt, text="Ok", command=ert)
btn.place(x=290, y=70)
rt.mainloop()
