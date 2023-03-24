from tkinter import *
from random import *
import io as io 
from os import *

def loe(file):
    tem=[]
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for i in f:
            tem.append(i.strip())
    return tem 

def salv(tem,file): 
    for i in range(len(tem)):
        tem[i]+="\n"
    with io.open(file,"w",encoding="utf-8-sig") as f:
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

    btnrez=Button(win,text="Režiimid",bg="Green",fg="White",font="Arial 20", width=19, relief=GROOVE,activeforeground="Green",command=lambda: rez(win))
    imgrez=PhotoImage(file="rez.png")
    imgrez=imgrez.subsample(5,5)
    lblrez=Label(win,image=imgrez)

    btnst=Button(win,text="Stuudio",bg="Orange",fg="White",font="Arial 20",width=19,relief=GROOVE,activeforeground="Orange", command=lambda: stuudio(win))
    imgmk=PhotoImage(file="molklu.png")
    imgmk=imgmk.subsample(11,11)
    lblmk=Label(win,image=imgmk)

    btnlp=Button(win,text="Lõpeta mäng",bg="Red",fg="White",font="Arial 20",width=19,relief=GROOVE,activeforeground="Red",command=lambda: lop(win))
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

    btnmang=Button(win,text="Mängi",font="Arial 20",width=19,bg="Green",fg="White",activeforeground="Green")

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
    imgleht=imgleht.subsample(10,10)
    lblleht=Label(win,image=imgleht)

    rbms=Radiobutton(win,text="Muuda sõna",font="Arial 20",fg="#e6ae19",variable=var,value=3)
    imgpl=PhotoImage(file="pliiats.png")
    imgpl=imgpl.subsample(11,11)
    lblpl=Label(win,image=imgpl)

    btnhak=Button(win,text="Alusta",font="Arial 20",width=19,bg="Green",fg="White",activeforeground="Green",command=lambda: stuvar(var,win))

    img=PhotoImage(file="kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    lbl.place(x=190,y=50)
    lblmk.place(x=380,y=40)
    rblt.place(x=190,y=200)
    lbllt.place(x=390,y=195)
    rbls.place(x=190,y=260)
    lblleht.place(x=350,y=260)
    rbms.place(x=190,y=320)
    lblpl.place(x=380,y=320)
    btnhak.place(x=150,y=450)

    win.mainloop()

def stuvar(var,win):
    v=var.get()
    if v==1:
        win.destroy()
        lisateema()
    elif v==2:
        win.destroy()
        lisasona()

def lisateema():
    win=Tk()
    win.geometry("600x600")
    win.title("Lisa teema")
    win.resizable(width=False,height=False)
    win.iconbitmap("raamat.ico")

    lbl=Label(win,text="Lisa teema",font="Arial 40")
    imgram=PhotoImage(file="raamat.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram)

    lblsona=Label(win,text="Lisa uus sõna",font="Arial 20")
    entso=Entry(win,font="Arial 15",width=16,fg="#00008b")
    btnso=Button(win,text="Lisa",font="Arial 18",width=12,bg="Red",fg="White",state="disabled",activeforeground="Red")

    lblteema=Label(win,text="Kirjuta uus teema",font="Arial 20")
    entte=Entry(win,font="Arial 15",width=19,fg="#00008b")
    btnte=Button(win,text="Lisa",font="Arial 18",width=14,bg="Green",fg="White",activeforeground="Green",command=lambda: lisateemacom(btnte,entte,btnso,entso))

    img=PhotoImage(file="kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    lbl.place(x=155,y=40)
    lbllt.place(x=420,y=45)
    lblteema.place(x=50,y=200)
    entte.place(x=50,y=250)
    btnte.place(x=52,y=300)
    lblsona.place(x=380,y=200)
    entso.place(x=380,y=250)
    btnso.place(x=382,y=300)

    win.mainloop()

def error():
        er=Tk()
        er.geometry("400x100")
        er.title("Viga")
        er.resizable(width=False,height=False)
        er.iconbitmap("error.ico")
        lbl=Label(er,text="Kontrollige, kas sisestatud väärtust pole olemas\n ja kas see pole tühi",font="Arial 13",justify=LEFT)
        lbl.pack(side=LEFT)
        er.mainloop()

def lisateemacom(btnte,entte,btnso,entso):
    nimi=entte.get()
    if len(nimi)==0:
        error()
    else:
        try:
            with io.open(f"{nimi}.txt","x",encoding="utf-8-sig") as f:
                btnte.configure(bg="Red",activeforeground="Red",state="disabled")
                entte.configure(state="disabled")
                btnso.configure(bg="Green",activeforeground="Green",state="normal",command=lambda: lisasonacom(nimi,entso,btnso))
        except:
            error()

def filetolist(file): 
    lst=[] 
    with io.open(file,"r",encoding="utf-8-sig") as f:
        for i in f:
            lst.append(i.strip())
    return lst

def listtofile(lst,file):
    lst1=[]
    for i in lst:
        lst1.append(i+"\n")
    with io.open(file,"w",encoding="utf-8-sig") as f:
        f.writelines(lst1)

def lisasonacom(nimi,entso,btnso):
    sona=entso.get()
    nimi+=".txt"
    lst=filetolist(nimi)
    if sona not in lst and len(sona)!=0:
        lst.append(sona)
        btnso.configure(bg="Green")
        entso.delete(0,END)
        listtofile(lst,nimi)
    else:
        btnso.configure(bg="Red")
        error()

def kontrollteema(entte,btnso,btnte,entso):
    nimi=entte.get()
    nimi1=nimi
    nimi1+=".txt"
    if path.isfile(nimi1): 
        entte.configure(state="disabled")
        btnte.configure(state="disabled")
        btnso.configure(bg="Green",activeforeground="Green",state="normal",command=lambda: lisasonacom(nimi,entso,btnso))
    else:
        entte.configure(bg="Red")


def lisasona():
    win=Tk()
    win.geometry("600x600")
    win.title("Lisa sõna")
    win.resizable(width=False,height=False)
    win.iconbitmap("leht.ico")

    lbl=Label(win,text="Lisa sõna",font="Arial 40")
    imgram=PhotoImage(file="leht.png")
    imgram=imgram.subsample(9,9)
    lbllt=Label(win,image=imgram)

    lblsona=Label(win,text="Kirjuta uus sõna",font="Arial 20")
    entso=Entry(win,font="Arial 15",width=16,fg="#00008b")
    btnso=Button(win,text="Lisa",font="Arial 18",width=12,bg="Red",fg="White",state="disabled",activeforeground="Red")

    lblteema=Label(win,text="Kirjuta olemasolev teema ",font="Arial 20")
    entte=Entry(win,font="Arial 15",width=23,fg="#00008b")
    btnte=Button(win,text="Kontrollima",font="Arial 18",width=17,bg="Green",fg="White",activeforeground="Green",command=lambda: kontrollteema(entte,btnso,btnte,entso))

    img=PhotoImage(file="kodu.png")
    img=img.subsample(9,9)
    btn=Button(win,image=img,command=lambda: kodu(win))
    btn.place(x=0,y=0)

    lbl.place(x=155,y=40)
    lbllt.place(x=420,y=45)
    lblteema.place(x=30,y=200)
    entte.place(x=50,y=250)
    btnte.place(x=55,y=300)
    lblsona.place(x=380,y=200)
    entso.place(x=380,y=250)
    btnso.place(x=382,y=300)

    win.mainloop()

kodu()