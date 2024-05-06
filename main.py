from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import fontstyle
from User import User
from Reservations import *
from hotel import *

old1= OneBedRoom(roomNum="203")
old2= TwoBedRoom(roomNum="204")

modern1= OneBedRoom(roomNum="111")
modern2= TwoBedRoom(roomNum="112")

foglalasok = [] 



login = Tk()
login.geometry("998x700")



image = Image.open("login/button.png")
LoginButton = ImageTk.PhotoImage(image)
#SZÁLLODA KÉPEK
modernH = Image.open("hotels/modern.png")
modernH = ImageTk.PhotoImage(modernH)

oldH = Image.open("hotels/old.png")
oldH = ImageTk.PhotoImage(oldH)



def toOld():
    chooseOld.place(x=0, y=0)
    hotelCanvas.place(x=10000, y=100000)
    canvas.place(x=10000, y=10000)
    loginCanvas.place(x=10000, y=10000)
def toModern():
    chooseModern.place(x=0, y=0)
    hotelCanvas.place(x=10000, y=100000)
    canvas.place(x=10000, y=10000)
    loginCanvas.place(x=10000, y=10000)


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

def foglal(ido, room):
        foglalasok.append(Reservation(ido, room))        
        f = open("foglalások.txt", "a")
        f.write(f"{ido};{room.roomNum};\n")
        f.close()
        
        
    

#Szobák
#Régi sítlusú szobák
oldOneBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
oldOneBed.place(x=100000, y=10000)
oldOneEntry = Entry(oldOneBed, width=100)
oldOneEntry.place(x=0, y=0)
reserve = Button(oldOneBed, width=10, height=5, command= lambda: foglal(oldOneEntry.get(), old1))
reserve.place(x=300, y=300)



oldTwoBed= Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
oldTwoBed.place(x=100000, y=10000)
oldTwoEntry = Entry(oldTwoBed)
oldTwoEntry.place(x=0, y=0)
reserve = Button(oldTwoBed, width=10, height=5, command= lambda: foglal(oldTwoEntry.get()))
reserve.place(x=300, y=300)




#Új sílusú szobák
modernOneBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
modernOneBed.place(x=100000, y=10000)
modernOneEntry = Entry(modernOneBed)


modernTwoBed = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
modernTwoBed.place(x=10000, y=10000)
modernTwoEntry = Entry(modernTwoBed)



#Szoba Választó

chooseOld = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
chooseOld.place(x=10000,y=10000)
oldOneBedbtn = Button(chooseOld,image=modernH,width=500, height=998,borderwidth=0, highlightthickness=0, command=toOldOne)
oldOneBedbtn.place(x=0, y=0)
oldTwoBedbtn = Button(chooseOld, image=modernH, width=500, height=998, borderwidth=0, highlightthickness=0, command=toOldTwo)
oldTwoBedbtn.place(x=500, y=0)


chooseModern = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
chooseModern.place(x=10000,y=10000)
modernOneBedbtn = Button(chooseModern,image=modernH, width=500, height=998,borderwidth=0, highlightthickness=0,command=toModernOne)
modernOneBedbtn.place(x=0, y=0)
modernTwoBedbtn = Button(chooseModern, image=modernH, width=500, height=998, borderwidth=0, highlightthickness=0, command=toModernTwo)
modernTwoBedbtn.place(x=500, y=0)




#Szállodák részleg
hotelCanvas = Canvas(login,width=1002, height=702,border=0,highlightthickness=0)
hotelCanvas.place(x=0, y=750)

modern = Button(hotelCanvas, image=modernH, width=500, height=998, borderwidth=0, highlightthickness=0, command=toModern)
modern.place(x=0, y=0)

old = Button(hotelCanvas, image=oldH, width=500, height=998,borderwidth=0, highlightthickness=0, command=toOld)
old.place(x=500, y=0)

header = Canvas(hotelCanvas, height=90, width=1000, bg="#49256D", border=0,highlightthickness=0)
header.place(x=0, y=0)






#BEJELENTKEZÉS ABLAK 
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

            else:
                hibaLP.config(text="Nem megfelelő jelszó", height=1, width=30, background="#8e8e8e",fg="red")
                hibaLP.place(x=450, y=405)
        else:
            hibaLN.config(text="Nem megfelelő név", height=1, width=30, background="#8e8e8e",fg="red")
            hibaLN.place(x=450, y=305)   

buttonLog=Button(loginCanvas, text="Bejelentkezés", width=199, height=47, command=verify, image=LoginButton, highlightthickness=0, borderwidth=0)
buttonLog.place(x=400, y=500)




#REGISZTRÁCIÓS ABLAK

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




#Regisztráció és annak ellenörzése 

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

buttonReg=Button(canvas, text="Regisztráció", width=199, height=47, command=regBtn, image=LoginButton, highlightthickness=0, borderwidth=0)
buttonReg.place(x=400, y=500)

login.mainloop()









