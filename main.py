from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import fontstyle
from User import User
from Reservations import *
from hotel import *
import re
import ctypes
import datetime

old1= OneBedRoom(roomNum="203", )
old2= TwoBedRoom(roomNum="204", )

modern1= OneBedRoom(roomNum="111",)
modern2= TwoBedRoom(roomNum="112",)

foglalasok = [] 

login = Tk()
login.geometry("998x700")

rectF = Image.open("rooms/rectF.png")
rectF = ImageTk.PhotoImage(rectF)

LoginButton = Image.open("login/bejelentkezesB.png")
LoginButton = ImageTk.PhotoImage(LoginButton)
regButton = Image.open("login/regisztracioB.png")
regButton = ImageTk.PhotoImage(regButton)
listaButton = Image.open("login/listazasB.png")
listaButton = ImageTk.PhotoImage(listaButton)
foglalasButton = Image.open("login/foglalasB.png")
foglalasButton = ImageTk.PhotoImage(foglalasButton)
backButton  = Image.open("header/vissza.png")
backButton  = ImageTk.PhotoImage(backButton)
res  = Image.open("header/foglalas.png")
res  = ImageTk.PhotoImage(res)
#SZÁLLODA KÉPEK-------------------------------
modernH = Image.open("hotels/modern.png")
modernH = ImageTk.PhotoImage(modernH)

oldH = Image.open("hotels/old.png")
oldH = ImageTk.PhotoImage(oldH)

#Header Képek---------------------------------
hotelHeader= Image.open("header/hotelHead.png")
hotelHeader = ImageTk.PhotoImage(hotelHeader)
roomHeaderphoto= Image.open("header/roomHead.png")
roomHeaderphoto = ImageTk.PhotoImage(roomHeaderphoto)
roomHead = Image.open("header/room.png")
roomHead = ImageTk.PhotoImage(roomHead)

#Szoba gomb Képek-----------------------------
oldOne= Image.open("rooms/oldOne.png")
oldOne = ImageTk.PhotoImage(oldOne)
oldTwo= Image.open("rooms/oldTwo.png")
oldTwo = ImageTk.PhotoImage(oldTwo)
modernOne= Image.open("rooms/modernOne.png")
modernOne = ImageTk.PhotoImage(modernOne)
modernTwo= Image.open("rooms/modernTwo.png")
modernTwo = ImageTk.PhotoImage(modernTwo)
roomModernOneBg= Image.open("rooms/roomModernOneBg.png")
roomModernOneBg = ImageTk.PhotoImage(roomModernOneBg)
roomModernTwoBg= Image.open("rooms/roomModernTwoBg.png")
roomModernTwoBg = ImageTk.PhotoImage(roomModernTwoBg)
roomOldOneBg= Image.open("rooms/roomOldOneBg.png")
roomOldOneBg = ImageTk.PhotoImage(roomOldOneBg)
roomOldTwoBg= Image.open("rooms/roomOldTwoBg.png")
roomOldTwoBg = ImageTk.PhotoImage(roomOldTwoBg)



roomModernOneBg



def visszaOld():
    chooseOld.place(x=0, y=0)
    oldOneBed.place(x=100000, y=1000000)
    oldTwoBed.place(x=100000, y=100000)

def visszaModernhez():
    chooseModern.place(x=0, y=0)
    modernOneBed.place(x=100000, y=1000000)
    modernTwoBed.place(x=100000, y=100000)

def visszaSzallodakhoz():
    hotelCanvas.place(x=0, y=0)
    chooseModern.place(x=1000000, y=100000)
    chooseOld.place(x=10000, y=100000)
    lista.place_forget

def visszaLoghoz():
    hotelCanvas.place(x=1000,y=1000000)
    loginCanvas.place(x=0,y=0)

def toOld():
    chooseOld.place(x=0, y=0)
    hotelCanvas.place(x=10000, y=100000)
    canvas.place(x=10000, y=10000)
    loginCanvas.place(x=10000, y=10000)
    lista.place(x=100000,y=10000)
def toModern():
    chooseModern.place(x=0, y=0)
    hotelCanvas.place(x=10000, y=100000)
    canvas.place(x=10000, y=10000)
    loginCanvas.place(x=10000, y=10000)
    lista.place(x=100000,y=10000)


def toOldOne():
    oldOneBed.place(x=0, y=0)
    chooseOld.place(x=10000000, y=100000)

def toOldTwo():
    oldTwoBed.place(x=0, y=0)
    chooseOld.place(x=10000000, y=100000)

def toModernTwo():
    modernTwoBed.place(x=0, y=0)
    chooseModern.place(x=10000000, y=100000)

def toModernOne():
    modernOneBed.place(x=0, y=0)
    chooseModern.place(x=10000000, y=100000)


def moveRight():
    canvas.place(x=1050, y=0)
def regBack():
    canvas.place(x=-5, y=0)
def szallodak():
    canvas.place(x=0, y=750)


image1_path = "bg/bg.png"
image1 = Image.open(image1_path)
photo1 = ImageTk.PhotoImage(image1)

def ellenoriz_datum(input_datum):
    minta = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(minta, input_datum))

error=Label(login, text="")

foglalasok = []
file = open("foglalások.txt", "r")
for e in file:
    line = e.split(";")
    foglalasok.append(Reservation(line[0], line[1]))

def foglal(ido, room, ):
        t = ido.split("-")
        if ellenoriz_datum(ido):
            if datetime.datetime(int(t[0]),int(t[1]),int(t[2]))>datetime.datetime.now():
                egyedi2 = True
                for i in range(0, len(foglalasok)):
                    if foglalasok[i].date==ido:
                        egyedi2=False



                if egyedi2:
                    foglalasok.append(Reservation(ido, room))        
                    f = open("foglalások.txt", "a")
                    f.write(f"{ido};{room.roomNum};\n")
                    f.close()
            
            

                    error.config(text="")  
                    error.place_forget()
                    ctypes.windll.user32.MessageBoxW(0, "Foglalás sikeres!", "Siker!", 0)
                
                else:
                    ctypes.windll.user32.MessageBoxW(0, "Ez a dátum már foglalt, kérjük válasszon másikat", "Hiba!", 0)
            else:
                ctypes.windll.user32.MessageBoxW(0, "Múltbeli időt szeretne megadni!", "Hiba!", 0)
        else:
             ctypes.windll.user32.MessageBoxW(0, "Hibás beviteli érték, kérek így add meg a dátumot: xxxx-xx-xx (év, hónap, nap)", "Hiba!", 0)

#Szobák--------------------------------------------------------------------------------------------------------------------------------------------
#Régi sítlusú szobák
oldOneBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
oldOneBed.place(x=100000, y=10000)


modernOneBedBG= Label(oldOneBed,width=1002, height=702,border=0,highlightthickness=0, image=roomOldOneBg)
modernOneBedBG.place(x=-1, y=0)
oldOneEntry = Entry(oldOneBed, width=100)
foglalas=Label(oldOneBed, text="Írja be a dátumot(formátum 'xxxx-xx-xx')", background="#cccccc")
foglalas.place(x=400, y=330,)
oldOneEntry.place(x=400, y=350)
reserve = Button(oldOneBed, width=199, height=47,image=foglalasButton,borderwidth=0,highlightthickness=0, command= lambda: foglal(oldOneEntry.get(), old1, ))
reserve.place(x=400, y=520)
szobaHead= Label(oldOneBed, height=88, width=1000, bg="#49256D", border=0,highlightthickness=0, image=roomHead)
szobaHead.place(x=0, y=0)


visszaBTN = Button(oldOneBed, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaOld)
visszaBTN.place(x=-1, y=0)



oldTwoBed= Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
oldTwoBed.place(x=100000, y=10000)
modernOneBedBG= Label(oldTwoBed,width=1002, height=702,border=0,highlightthickness=0, image=roomOldTwoBg)
modernOneBedBG.place(x=-1, y=0)
foglalas=Label(oldTwoBed, text="Írja be a dátumot(formátum 'xxxx-xx-xx')", background="#cccccc")
foglalas.place(x=400, y=330,)
oldTwoEntry = Entry(oldTwoBed)
oldTwoEntry.place(x=400, y=350)
reserve = Button(oldTwoBed, width=199, height=47,image=foglalasButton,borderwidth=0,highlightthickness=0, command= lambda: foglal(oldTwoEntry.get(), old2))
reserve.place(x=400, y=520)
szobaHead= Label(oldTwoBed, height=88, width=1000, bg="#49256D", border=0,highlightthickness=0, image=roomHead)
szobaHead.place(x=0, y=0)

visszaBTN = Button(oldTwoBed, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaOld)
visszaBTN.place(x=-1, y=0)


#Új sílusú szobák----------------------------------------------------------------------------------------------------------------
modernOneBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
modernOneBed.place(x=100000, y=10000)
modernOneBedBG= Label(modernOneBed,width=1002, height=702,border=0,highlightthickness=0, image=roomModernOneBg)
modernOneBedBG.place(x=-1, y=0)
reserve = Button(modernOneBed, width=199, height=47,image=foglalasButton,borderwidth=0,highlightthickness=0, command= lambda: foglal(modernOneEntry.get(), modern1))
reserve.place(x=400, y=520)
szobaHead= Label(modernOneBed, height=88, width=1000, bg="#49256D", border=0,highlightthickness=0, image=roomHead)
szobaHead.place(x=0, y=0)
visszaBTN = Button(modernOneBed, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaModernhez)
visszaBTN.place(x=-1, y=0)
foglalas=Label(modernOneBed, text="Írja be a dátumot(formátum 'xxxx-xx-xx')", background="#cccccc")
foglalas.place(x=400, y=330,)
modernOneEntry = Entry(modernOneBed)
modernOneEntry.place(x=400, y=350)




modernTwoBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
modernTwoBed.place(x=10000, y=10000)
modernOneBedBG= Label(modernTwoBed,width=1002, height=702,border=0,highlightthickness=0, image=roomModernTwoBg)
modernOneBedBG.place(x=-1, y=0)
reserve = Button(modernTwoBed, width=199, height=47,image=foglalasButton,borderwidth=0,highlightthickness=0, command= lambda: foglal(modernTwoEntry.get(), modern2))
reserve.place(x=400, y=520)
szobaHead= Label(modernTwoBed, height=88, width=1000, bg="#49256D", border=0,highlightthickness=0, image=roomHead)
szobaHead.place(x=0, y=0)
visszaBTN = Button(modernTwoBed, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaModernhez)
visszaBTN.place(x=-1, y=0)
foglalas=Label(modernTwoBed, text="Írja be a dátumot(formátum 'xxxx-xx-xx')", background="#cccccc")
foglalas.place(x=400, y=330,)
modernTwoEntry = Entry(modernTwoBed)
modernTwoEntry.place(x=400, y=350,)

#Szoba Választó------------------------------------------------------------------------------------------------------------------------

chooseOld = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
chooseOld.place(x=10000,y=10000)
oldOneBedbtn = Button(chooseOld,image=oldOne,width=500, height=700,borderwidth=0, highlightthickness=0, command=toOldOne)
oldOneBedbtn.place(x=0, y=0)
oldTwoBedbtn = Button(chooseOld, image=oldTwo, width=500, height=700, borderwidth=0, highlightthickness=0, command=toOldTwo)
oldTwoBedbtn.place(x=500, y=0)
mid = Canvas(chooseOld, width=10,height=700,bg="#8e8e8e",borderwidth=0, highlightthickness=0,)
mid.place(x=490,y=0)
roomHeader= Label(chooseOld,width=1000, height=88, highlightthickness=0, borderwidth=0,image=roomHeaderphoto)
roomHeader.place(x=0, y=0)
visszaBTN = Button(chooseOld, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaSzallodakhoz)
visszaBTN.place(x=-1, y=0)


chooseModern = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
chooseModern.place(x=10000,y=10000)
modernOneBedbtn = Button(chooseModern,image=modernOne, width=500, height=700,borderwidth=0, highlightthickness=0,command=toModernOne)
modernOneBedbtn.place(x=0, y=0)
modernTwoBedbtn = Button(chooseModern, image=modernTwo, width=500, height=700, borderwidth=0, highlightthickness=0, command=toModernTwo)
modernTwoBedbtn.place(x=500, y=0)
mid = Canvas(chooseModern, width=10,height=700,bg="#8e8e8e",borderwidth=0, highlightthickness=0,)
mid.place(x=490,y=0)
roomHeader= Label(chooseModern,width=1000, height=88, highlightthickness=0, borderwidth=0, image=roomHeaderphoto)
roomHeader.place(x=0, y=0)
visszaBTN = Button(chooseModern, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaSzallodakhoz)
visszaBTN.place(x=-1, y=0)

#Foglalási lista kiírása--------------------------------------------------------------------------------------------------------------------------------
def listahoz():
    lista.place(x=0, y=0)
    hotelCanvas.place_forget()

lista= Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
lista.place(x=10000,y=10000000)
kozep= Canvas(lista, width=600, height=700,border=0,highlightthickness=0, background="#8e8e8e")
kozep.place(x=200, y=0)
visszaBTN = Button(lista, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaSzallodakhoz)
visszaBTN.place(x=-1, y=0)




def listazas():
    
        with open("foglalások.txt", "r") as file:
            # Fájl tartalmának beolvasása
            content = file.read()

            # Label létrehozása a beolvasott tartalom megjelenítésére
            label32 = Label(lista, text=content, justify=LEFT, wraplength=400)
            label32.place(x=450, y=200)

listazasBTN= Button(lista, width=199, height=47, command=listazas, image=listaButton, highlightthickness=0, borderwidth=0)
listazasBTN.place(x=400, y=500)
        







#Szállodák részleg------------------------------------------------------------------------------------------------------------------------------
hotelCanvas = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
hotelCanvas.place(x=0, y=750)

modern = Button(hotelCanvas, image=modernH, width=500, height=998, borderwidth=0, highlightthickness=0, command=toModern)
modern.place(x=0, y=0)

old = Button(hotelCanvas, image=oldH, width=500, height=998,borderwidth=0, highlightthickness=0, command=toOld)
old.place(x=500, y=0)

mid = Canvas(hotelCanvas, width=10,height=700,bg="#8e8e8e",borderwidth=0, highlightthickness=0,)
mid.place(x=490,y=0)

header = Label(hotelCanvas, height=88, width=1000, bg="#49256D", border=0,highlightthickness=0, image=hotelHeader)
header.place(x=0, y=0)

visszaBTN = Button(hotelCanvas, width=138, height=88, image=backButton, borderwidth=0,highlightthickness=0,command=visszaLoghoz)
visszaBTN.place(x=-1, y=0)

foglalas = Button(hotelCanvas,width=138, height=88, image=res, borderwidth=0,highlightthickness=0,command=listahoz)
foglalas.place(x=860, y=0)



#BEJELENTKEZÉS ABLAK ----------------------------------------------------------------------------------------------------------------------------------
loginCanvas = Canvas(login, width=1002, height=702, bg="red")
loginCanvas.place(x=-5, y=0)
loginCanvas.create_image(0,0,anchor=NW,image=photo1)


btnLogin2=Button(loginCanvas)
btnLogin2.configure(width=28, height=3, background="#9674B8", text="Bejelentkezés",highlightthickness=0,borderwidth=0, fg="white",)
btnLogin2.place(x=512, y=219)


btnReg2=Button(loginCanvas,)
btnReg2.configure(width=28, height=3, background="#A47FCA", text="Regisztráció",highlightthickness=0,borderwidth=0, fg="white",command=regBack)
btnReg2.place(x=312, y=219)


felhasz1 = Label(loginCanvas, text="Felhasználónév", background="#8e8e8e")
felhasz1.place(y=305, x=350 )

jelszo1 = Label(loginCanvas, text="Jelszó", background="#8e8e8e")
jelszo1.place(y=405, x=350 )

entryLName = Entry(loginCanvas, width=50,)
entryLName.place(x=350, y= 325)

entryLPass = Entry(loginCanvas, width=50)
entryLPass.place(x=350, y= 425)

hibaLP=Label(loginCanvas, text="")
hibaLN=Label(loginCanvas, text="")


def verify():
    f = open("felhasználók.txt", "r")
    for line in f:
        sor=line.split(";")
        if sor[0] == entryLName.get():
            hibaLN.config(text="")
            hibaLN.place_forget()

            if sor[1] == entryLPass.get():
                hotelCanvas.place(x=0, y=0)
                canvas.place(x=10000, y=10000)
                loginCanvas.place(x=10000, y=10000)
                hibaLP.config(text="")  
                hibaLP.place_forget()
                hibaLN.config(text="")
                hibaLN.place_forget()


            else:
                hibaLP.config(text="Nem megfelelő jelszó", height=1, width=30, background="#8e8e8e",fg="red")
                hibaLP.place(x=450, y=405)
        else:
            hibaLN.config(text="Nem megfelelő név", height=1, width=30, background="#8e8e8e",fg="red")
            hibaLN.place(x=450, y=305)   

buttonLog=Button(loginCanvas, text="Bejelentkezés", width=199, height=47, command=verify, image=LoginButton, highlightthickness=0, borderwidth=0)
buttonLog.place(x=400, y=500)


#REGISZTRÁCIÓS ABLAK--------------------------------------------------------------------------------------------------------------------------------------------

canvas = Canvas(login, width=1002, height=702)
canvas.place(x=-5, y=0)
canvas.create_image(0,0,anchor=NW,image=photo1)

btnLogin=Button(canvas)
btnLogin.configure(width=28, height=3, background="#A47FCA", text="Bejelentkezés",highlightthickness=0,borderwidth=0, fg="white", command=moveRight)
btnLogin.place(x=512, y=219)


btnReg=Button(canvas,)
btnReg.configure(width=28, height=3, background="#9674B8", text="Regisztráció",highlightthickness=0,borderwidth=0, fg="white",)
btnReg.place(x=312, y=219)

felhasz = Label(canvas, text="Felhasználónév", background="#8e8e8e")
felhasz.place(y=305, x=350 )

jelszo = Label(canvas, text="Jelszó", background="#8e8e8e")
jelszo.place(y=405, x=350 )



entryRName = Entry(canvas, width=50,)
entryRName.place(x=350, y= 325)

entryRPass = Entry(canvas, width=50)
entryRPass.place(x=350, y= 425)


hibaRP=Label(canvas, text="")
hibaN=Label(canvas, text="")


#Regisztráció és annak ellenörzése ------------------------------------------------------------------------------------------------------------------------------------

felhasznalok = []
file = open("felhasználók.txt", "r")
for e in file:
    line = e.split(";")
    felhasznalok.append(User(line[0], line[1]))

def regName():

    textP=entryRPass.get()
    textN=entryRName.get()

    if len(textN)>3:           
        hibaN.config(text="")
        hibaN.place_forget()                
    else :
        hibaN.config(text="Legalább 4 karaktert adjon meg!", height=1, width=30, background="#8e8e8e",fg="red")
        hibaN.place(x=450, y=305)

    
    
    if len(textP)>3:           
        hibaRP.config(text="")  
        hibaRP.place_forget()       
    else :
        hibaRP.config(text="Legalább 4 karaktert adjon meg!",height=1, width=30, background="#8e8e8e", fg="red",)
        hibaRP.place(x=450, y=405)
    
    if len(textN)>3 and len(textP)>3:
        egyedi = True
        for i in range(0, len(felhasznalok)):
            if felhasznalok[i]._name==textN:
                egyedi=False
            
        if egyedi:
            felhasznalok.append(User(textN, textP))        
            f = open("felhasználók.txt", "a")
            f.write(f"{textN};{textP};\n")
            f.close()
            canvas.place(x=0, y=-710)
        
        else:
            hibaN.config(text="Ilyen felhasználó van már!", height=1, width=30, background="#8e8e8e",fg="red")
            hibaN.place(x=450, y=305)
        
def regBtn():
     regName()

buttonReg=Button(canvas, text="Regisztráció", width=198, height=47, command=regBtn, image=regButton, highlightthickness=0, borderwidth=0)
buttonReg.place(x=400, y=500)

login.mainloop()









