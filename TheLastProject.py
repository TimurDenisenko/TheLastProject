from tkinter import *
from random import * 

def loe(file):
    tem=[]
    with open(file,"r",encoding="utf-8-sig") as f:
        for i in f:
            tem.append(i.strip())
    return tem 

def salv(tem,file): 
    for i in range(len(tem)):
        tem[i]+="\n"
    with open(file,"w",encoding="utf-8-sig") as f:
        f.writelines(tem)

def kodu(win=None):
    if win:
       win.destroy()
    win=Tk()
    win.geometry("600x800")
    win.resizable(width=False,height=False)
    win.title("Kodu")
    win.iconbitmap("brain.ico")
    
    lbl=Label(win,text="Võllapuud",font="Arial 40")
    imgpet=PhotoImage(file="petl.png")
    imgpet=imgpet.subsample(6,6)
    lblpet=Label(win,image=imgpet)

    btnrez=Button(win,text="Režiimid",bg="Green",fg="White",font="Arial 20", width=19, relief=GROOVE)
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez)

    btnst=Button(win,text="Stuudio",bg="Orange",fg="White",font="Arial 20",width=19,relief=GROOVE)
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk)

    lbl.place(x=165,y=50)
    lblpet.place(x=395,y=30)
    btnrez.place(x=0,y=200)
    lblrez.place(x=320,y=178)
    btnst.place(x=0,y=300)
    lblmk.place(x=330,y=288)
    win.mainloop()

kodu()