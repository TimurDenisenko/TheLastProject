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
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.title("Kodu")
    win.iconbitmap("brain.ico")
    
    lbl=Label(win,text="Võllapuud",font="Arial 40")
    imgpet=PhotoImage(file="petl.png")
    imgpet=imgpet.subsample(6,6)
    lblpet=Label(win,image=imgpet)

    btnrez=Button(win,text="Režiimid",bg="Green",fg="White",font="Arial 20", width=19, relief=GROOVE,command=lambda: rez(win))
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez)

    btnst=Button(win,text="Stuudio",bg="Orange",fg="White",font="Arial 20",width=19,relief=GROOVE, command=lambda: stuudio(win))
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk)

    btnlp=Button(win,text="Lõpeta mäng",bg="Red",fg="White",font="Arial 20",width=19,relief=GROOVE,command=lambda: lop(win))
    imglp=PhotoImage(file="lop.png")
    imglp=imglp.subsample(5,5)
    lbllp=Label(win,image=imglp)


    lbl.place(x=165,y=50)
    lblpet.place(x=395,y=30)
    btnrez.place(x=0,y=200)
    lblrez.place(x=320,y=178)
    btnst.place(x=0,y=300)
    lblmk.place(x=330,y=288)
    btnlp.place(x=0,y=400)
    lbllp.place(x=335,y=395)

    win.mainloop()

def lop(win):
    win.destroy()

def rez(win):
    win.destroy()
    win=Tk()
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.iconbitmap("rez.ico")
    win.title("Režiimid")

    lbl=Label(win,text="Režiimid",font="Arial 40")
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez)

    var=IntVar()

    rbsolo=Radiobutton(win,text="Üksikmängija mäng",font="Arial 20",fg="Blue",variable=var,value=1)
    imgsolo=PhotoImage(file="stick.png")
    imgsolo=imgsolo.subsample(9,9)
    lblsolo=Label(win,image=imgsolo)

    rbbot=Radiobutton(win,text="Robotimäng",font="Arial 20",fg="Red",variable=var, value=2)
    imgrob=PhotoImage(file="robot.png")
    imgrob=imgrob.subsample(23,23)
    lblrob=Label(win,image=imgrob)

    rbmulti=Radiobutton(win,text="Mängib sõbraga",font="Arial 20",fg="Purple",variable=var,value=3)
    imgmulti=PhotoImage(file="2stick.png")
    imgmulti=imgmulti.subsample(9,9)
    lblmulti=Label(win,image=imgmulti)

    btnmang=Button(win,text="Mängi",font="Arial 20",width=19,bg="Green",fg="White")

    img=PhotoImage(file="kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    lbl.place(x=190,y=50)
    lblrez.place(x=395,y=30)
    rbsolo.place(x=165,y=200)
    lblsolo.place(x=430,y=190)
    rbbot.place(x=165,y=280)
    lblrob.place(x=350,y=265)
    rbmulti.place(x=165,y=360)
    lblmulti.place(x=390,y=350)
    btnmang.place(x=150,y=450)

    win.mainloop()

def stuudio(win):
    win.destroy()
    win=Tk()
    win.title("Stuudio")
    win.geometry("600x600")
    win.resizable(width=False,height=False)
    win.iconbitmap("molklu.ico")

    lbl=Label(win,text="Stuudio",font="Arial 40")
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk)

    var=IntVar()

    rblt=Radiobutton(win,text="Lisage teema",font="Arial 20",fg="#ffc900",variable=var,value=1)
    imgram=PhotoImage(file="raamat.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram)

    rbls=Radiobutton(win,text="Lisa sõna",font="Arial 20",fg="#ffba00",variable=var,value=2)
    imgleht=PhotoImage(file="leht.png")

    img=PhotoImage(file="kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    lbl.place(x=190,y=50)
    lblmk.place(x=380,y=40)
    rblt.place(x=190,y=200)
    lbllt.place(x=390,y=195)
    rbls.place(x=190,y=250)

    win.mainloop()

kodu()