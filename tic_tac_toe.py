from tkinter import *

root = Tk()
root.geometry("300x500")
root.title("TIC TAC TOE")

head = Label(root,text="TIC-TAC-TOE",fg="forestgreen",bg="light cyan",font=("Arial",20,"italic"))
head.pack()

p1_name = ""
p2_name = ""
START = False
def Start():
    global p1_name,p2_name,START
    P1 = p1.get()
    P2 = p2.get()

    if P1.split() == []:
        text = "Enter Player 1 Name"
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P2.split() == []:
        text = "Enter Player 2 Name"
        turn.place(x=50,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    elif P1.split() == P2.split():
        text = "Enter Different Player Names"
        turn.place(x=25,y=455)
        turn['fg'] = "red"
        turn['text'] = text
    else:
        p1_name = P1
        p2_name = P2
        p1['font'] = ("Arial",8,"bold")
        p2['font'] = ("Arial",8,"bold")
        p1['state']=DISABLED
        p2['state']=DISABLED

        start.place(x=1000,y=1000)
        turn['text'] = "{}{} Turn".format(p1_name,"'s")
        turn['fg'] = "blue"
        turn['font'] = ("Ubuntu",20,"bold")
        turn.place(x=50,y=425)
        START = True
        
def WinCheck():
    if b1['text'] == "O" and b2['text'] == "O" and b3['text'] == "O":
        b1['bg']="light green";b2['bg']="light green";b3['bg']="light green"
        return "p1"
    elif b4['text'] == "O" and b5['text'] == "O" and b6['text'] == "O":
        b4['bg']="light green";b5['bg']="light green";b6['bg']="light green"
        return "p1"
    elif b7['text'] == "O" and b8['text'] == "O" and b9['text'] == "O":
        b7['bg']="light green";b8['bg']="light green";b9['bg']="light green"
        return "p1"
    elif b1['text'] == "O" and b4['text'] == "O" and b7['text'] == "O":
        b1['bg']="light green";b4['bg']="light green";b7['bg']="light green"
        return "p1"
    elif b2['text'] == "O" and b5['text'] == "O" and b8['text'] == "O":
        b2['bg']="light green";b5['bg']="light green";b8['bg']="light green"
        return "p1"
    elif b3['text'] == "O" and b6['text'] == "O" and b9['text'] == "O":
        b3['bg']="light green";b6['bg']="light green";b9['bg']="light green"
        return "p1"
    elif b1['text'] == "O" and b5['text'] == "O" and b9['text'] == "O":
        b1['bg']="light green";b5['bg']="light green";b9['bg']="light green"
        return "p1"
    elif b3['text'] == "O" and b5['text'] == "O" and b7['text'] == "O":
        b3['bg']="light green";b5['bg']="light green";b7['bg']="light green"
        return "p1"
    
    if b1['text'] == "X" and b2['text'] == "X" and b3['text'] == "X":
        b1['bg']="light blue";b2['bg']="light blue";b3['bg']="light blue"
        return "p2"
    elif b4['text'] == "X" and b5['text'] == "X" and b6['text'] == "X":
        b4['bg']="light blue";b5['bg']="light blue";b6['bg']="light blue"
        return "p2"
    elif b7['text'] == "X" and b8['text'] == "X" and b9['text'] == "X":
        b7['bg']="light blue";b8['bg']="light blue";b9['bg']="light blue"
        return "p2"
    elif b1['text'] == "X" and b4['text'] == "X" and b7['text'] == "X":
        b1['bg']="light blue";b4['bg']="light blue";b7['bg']="light blue"
        return "p2"
    elif b2['text'] == "X" and b5['text'] == "X" and b8['text'] == "X":
        b2['bg']="light blue";b5['bg']="light blue";b8['bg']="light blue"
        return "p2"
    elif b3['text'] == "X" and b6['text'] == "X" and b9['text'] == "X":
        b3['bg']="light blue";b6['bg']="light blue";b9['bg']="light blue"
        return "p2"
    elif b1['text'] == "X" and b5['text'] == "X" and b9['text'] == "X":
        b1['bg']="light blue";b5['bg']="light blue";b9['bg']="light blue"
        return "p2"
    elif b3['text'] == "X" and b5['text'] == "X" and b7['text'] == "X":
        b3['bg']="light blue";b5['bg']="light blue";b7['bg']="light blue"
        return "p2"
    
    elif (b1['text'] != "" and b2['text'] != "" and b3['text'] != "" and
        b4['text'] != "" and b5['text'] != "" and b6['text'] != "" and
        b7['text'] != "" and b8['text'] != "" and b9['text'] != ""):
        return "tie"
        
    else:
        return False
def DisableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = DISABLED
def EnableButtons(ButtonList):
    for a in range(len(ButtonList)):
        ButtonList[a]['state'] = NORMAL
def BtnClick(button):
    global START,p1_name,p2_name
    if START == True:
        if button['text'] == "":
            if turn['text'] == "{}{} Turn".format(p1_name,"'s"):
                button['text'] = "O"
                turn['text'] = "{}{} Turn".format(p2_name,"'s")
            else:
                button['text'] = "X"
                turn['text'] = "{}{} Turn".format(p1_name,"'s")

        check = WinCheck()
        if check != False:
            restart.place(x=105,y=470)
            START = False
            if check=="p1":
                text = "{} Wins".format(p1_name)
                buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "light green":
                        Remove.append(buttons[i])
            elif check=="p2":
                text = "{} Wins".format(p2_name)
                buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
                Remove = []
                for i in range(9):
                    if buttons[i]['bg'] == "light blue":
                        Remove.append(buttons[i])
            else:
                text = "It is a tie !"
            turn['fg'] = "forestgreen"
            turn['text'] = text

            if check == "p1" or check == "p2":
                for i in range(len(Remove)):
                    buttons.remove(Remove[i])
                DisableButtons(buttons)

def Restart():
    Buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9]
    EnableButtons([p1,p2])
    EnableButtons(Buttons)
    restart.place(x=1000,y=1000)
    for a in range(len(Buttons)):
        Buttons[a]['text'] = ""
        Buttons[a]['bg'] = "SystemButtonFace"
    turn['text'] = ""
    start.place(x=107,y=410)
    p1['font'] = "TkTextFont"
    p2['font'] = "TkTextFont"
####################################################################################

Label(root,text="Player 1 :",fg="brown",font=("Courier",10,"bold")).place(x=0,y=50)
p1 = Entry(root)
p1.place(x=90,y=52)

Label(root,text="Player 2 :",fg="brown",font=("Courier",10,"bold")).place(x=0,y=75)
p2 = Entry(root)
p2.place(x=90,y=77)

start = Button(root,text="START",bg="gray90",fg="green",font=("Ubuntu",15,"bold"),command=Start)
start.place(x=107,y=410)

turn = Label(root,text="",font=("Ubuntu",15,"normal"))
turn.place(x=50,y=455)

###################################

b1 = Button(root,width=13,height=6,command = lambda:BtnClick(b1))
b1.place(x=0,y=100)

b2 = Button(root,width=13,height=6,command = lambda:BtnClick(b2))
b2.place(x=100,y=100)

b3 = Button(root,width=13,height=6,command = lambda:BtnClick(b3))
b3.place(x=200,y=100)

b4 = Button(root,width=13,height=6,command = lambda:BtnClick(b4))
b4.place(x=0,y=200)

b5 = Button(root,width=13,height=6,command = lambda:BtnClick(b5))
b5.place(x=100,y=200)

b6 = Button(root,width=13,height=6,command = lambda:BtnClick(b6))
b6.place(x=200,y=200)

b7 = Button(root,width=13,height=6,command = lambda:BtnClick(b7))
b7.place(x=0,y=300)

b8 = Button(root,width=13,height=6,command = lambda:BtnClick(b8))
b8.place(x=100,y=300)

b9 = Button(root,width=13,height=6,command = lambda:BtnClick(b9))
b9.place(x=200,y=300)

###################################

restart = Button(root,text="Restart",fg="blue",bg="aquamarine",width = 10,height=1,font=("Courier",10,"bold"),command = Restart)
##restart.place(x=105,y=470)
restart.place(x=1000,y=1000)

root.mainloop()
