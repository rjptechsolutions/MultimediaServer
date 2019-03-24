from pygame import mixer
import sys
mixer.init()
multidict = {}

def menucard():
    print("----Menu---- \n 1.Registration \n 2.Call \n 3.Phonebook \n 4.exit")
    menu()
def exit():
    sys.exit(1)
def menu():    
    m=int(input("Enter the Menu No."))
    if(m==1):
        Reg()
    elif(m==2):
        call()
    elif (m==3):
        phonebook()
    elif(m==4):
        exit()
    else:
        menucard()
    menucard()
    
def Reg():
    b=int(input("Enter the Mobile No"))
    print("Select music \n 1.t1.wav \n 2.t2.wav")
    c=int(input("Enter the Music No."))
    if(c==1):
        c="t1.wav"
    else:
        c="t2.wav"
    print("Mobile No. is ",b)
    print("Selected Music is "+c)
    multidict[b]=c
    print(multidict)
    mixer.music.load(c)
    mixer.music.play()
    menucard()
    
def call():
    print("Dial the Number")
    b=int(input("Enter the Mobile No"))
    print("calling ",b)
    temp=multidict.get(b)
    x=''+temp
    mixer.music.load(x)
    mixer.music.play()
    menucard()
    
def phonebook():
    print("Total Users")
    print(multidict)
    menucard()

menucard()
