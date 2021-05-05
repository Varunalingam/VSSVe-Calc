import tkinter
import time
from PIL import Image
from PIL import ImageTk
import os
import inspect

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

main_window = tkinter.Tk()
main_window.title("VSSVE Calc")
main_window.iconbitmap(path + "/ICONS/logo.bmp")
main_window.resizable(False,False)
main_window.maxsize(300,500)
main_window.minsize(300,500)

Equation = "( 0"
BracketsUnclosed = 1

i = 0
while i < 29 :
    i += 1
    main_window.columnconfigure(i,minsize = 10,weight = 10,pad = 0)

i = 0
while i < 49 :
    i += 1
    main_window.rowconfigure(i,minsize = 10,weight = 10,pad = 0)

Basiccolor = "white"
Oppbasiccolor = "black"
Activestatecolor = "#191919"
CurrentInputValue = "Radians"
Hyp = "Normal"
Inv = "Normal"
CurrentInputType = "BODMAS"

photo = Image.open( path + "/Icons/logo.bmp")
photo = photo.resize((40,40),Image.ANTIALIAS)
photo = ImageTk.PhotoImage(photo)

menui = Image.open( path + "/ICONS/" + Basiccolor +"/Menu.png")
menui = menui.resize((30,30),Image.ANTIALIAS)
menui = ImageTk.PhotoImage(menui)

menuclose = Image.open(path + "/ICONS/" + Basiccolor +"/Menu_Close.png")
menuclose = menuclose.resize((40,40),Image.ANTIALIAS)
menuclose = ImageTk.PhotoImage(menuclose)

normali = Image.open(path + "/ICONS/" + Basiccolor +"/Normal.png")
normali = normali.resize((40,40),Image.ANTIALIAS)
normali = ImageTk.PhotoImage(normali)

Scientifici = Image.open(path + "/ICONS/" + Basiccolor +"/Scientific.png")
Scientifici = Scientifici.resize((40,40),Image.ANTIALIAS)
Scientifici = ImageTk.PhotoImage(Scientifici)

Settingsi = Image.open(path + "/ICONS/" + Basiccolor +"/Settings.png")
Settingsi = Settingsi.resize((40,40),Image.ANTIALIAS)
Settingsi = ImageTk.PhotoImage(Settingsi)

Functioni = Image.open(path + "/ICONS/" + Basiccolor +"/Settings.png")
Functioni = Functioni.resize((40,40),Image.ANTIALIAS)
Functioni = ImageTk.PhotoImage(Functioni)

menustate = True
currentMode = "Normal"

def menubutton():
    global menustate,main_window,photo,menui,Basiccolor,Oppbasiccolor,Activestatecolor,menuclose,normali,Scientifici,Settingsi,currentMode, Functioni
    if menustate == False:
        menustate = True
        tkinter.Frame(main_window,bg = Oppbasiccolor).grid(row = 0, column = 5,rowspan = 5,columnspan = 25,sticky = "nswe")
        tkinter.Button(main_window,image = menuclose,command = menubutton,bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 0, rowspan = 5, columnspan = 5,sticky = "nswe")
        if currentMode == "Normal":
            tkinter.Button(main_window,state = "disabled",image = normali,command = lambda: Buttons("Normal Window"),bg = "green",activebackground = Activestatecolor).grid(row = 0,column = 6, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Scientifici,command = lambda: Buttons("Scientific Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 12, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Functioni,command = menubutton,bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 18, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Settingsi,command = lambda: Buttons("Settings Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 24, rowspan = 5, columnspan = 5,sticky = "nswe")
        elif currentMode == "Scientific":
            tkinter.Button(main_window,state = "normal",image = normali,command = lambda: Buttons("Normal Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 6, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Scientifici,command = lambda: Buttons("Scientific Window"),bg = "green",activebackground = Activestatecolor).grid(row = 0,column = 12, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Functioni,command = menubutton,bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 18, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Settingsi,command = lambda: Buttons("Settings Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 24, rowspan = 5, columnspan = 5,sticky = "nswe")
        elif currentMode == "Settings":
            tkinter.Button(main_window,state = "normal",image = normali,command = lambda: Buttons("Normal Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 6, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Scientifici,command = lambda: Buttons("Scientific Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 12, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Functioni,command = menubutton,bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 18, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Settingsi,command = lambda: Buttons("Settings Window"),bg = "green",activebackground = Activestatecolor).grid(row = 0,column = 24, rowspan = 5, columnspan = 5,sticky = "nswe")
        elif currentMode == "Function":
            tkinter.Button(main_window,state = "normal",image = normali,command = lambda: Buttons("Normal Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 6, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Scientifici,command = lambda: Buttons("Scientific Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 12, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "disabled",image = Functioni,command = menubutton,bg = "green",activebackground = Activestatecolor).grid(row = 0,column = 18, rowspan = 5, columnspan = 5,sticky = "nswe")
            tkinter.Button(main_window,state = "normal",image = Settingsi,command = lambda: Buttons("Settings Window"),bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 24, rowspan = 5, columnspan = 5,sticky = "nswe")
    else:
        menustate = False
        tkinter.Label(main_window,text = "VSSVE Calc",font = "Comic 22 bold",bg = Oppbasiccolor,fg = Basiccolor).grid(row = 0, column = 5,rowspan = 5,columnspan = 20,sticky = "nswe")
        tkinter.Label(main_window,image = photo,bg = Oppbasiccolor ).grid(row = 0,column = 25, rowspan = 5, columnspan = 5,sticky = "nswe")
        tkinter.Button(main_window,image = menui,command = menubutton,bg = Oppbasiccolor,activebackground = Activestatecolor).grid(row = 0,column = 0, rowspan = 5, columnspan = 5,sticky = "nswe")

def EnableAll():
    global main_window,window, keypad,Hyp,Inv

    if currentMode == "Normal":
        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 14, column = 18 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(window, text = "(",command = lambda:Buttons("(") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 19, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "-",command = lambda:Buttons("-") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 3 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "π",command = lambda:Buttons("pi") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "e",command = lambda:Buttons("e") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 39, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")

        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 17 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 2 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
    elif currentMode == "Scientific":
        if Hyp == "Normal" and Inv == "Normal":
            tkinter.Button(window, text = "ln",command = lambda:Buttons("logbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2082",command = lambda:Buttons("logb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2081\u2080",command = lambda:Buttons("logb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2093",command = lambda:Buttons("log") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window, text = "sin",command = lambda:Buttons("sin") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "cos",command = lambda:Buttons("cos") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "tan",command = lambda:Buttons("tan") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        
        elif Hyp == "Normal":
            tkinter.Button(window, text = "antiln",command = lambda:Buttons("antilogbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2082",command = lambda:Buttons("antilogb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2081\u2080",command = lambda:Buttons("antilogb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2093",command = lambda:Buttons("antilog") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window, text = "sin\u207b\u00B9",command = lambda:Buttons("asin") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "cos\u207b\u00B9",command = lambda:Buttons("acos") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "tan\u207b\u00B9",command = lambda:Buttons("atan") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        elif Inv == "Normal":
            tkinter.Button(window, text = "ln",command = lambda:Buttons("logbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2082",command = lambda:Buttons("logb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2081\u2080",command = lambda:Buttons("logb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "log\u2093",command = lambda:Buttons("log") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window, text = "sinh",command = lambda:Buttons("sinh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "cosh",command = lambda:Buttons("cosh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "tanh",command = lambda:Buttons("tanh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        
        else:
            tkinter.Button(window, text = "antiln",command = lambda:Buttons("antilogbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2082",command = lambda:Buttons("antilogb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2081\u2080",command = lambda:Buttons("antilogb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "antilog\u2093",command = lambda:Buttons("antilog") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window, text = "sinh\u207b\u00B9",command = lambda:Buttons("asinh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "cosh\u207b\u00B9",command = lambda:Buttons("acosh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window, text = "tanh\u207b\u00B9",command = lambda:Buttons("atanh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 11 ,rowspan = 3, columnspan = 17,sticky = "nswe")

        tkinter.Button(window, text = "[.]",command = lambda:Buttons("gif") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "|.|",command = lambda:Buttons("mod") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "!",command = lambda:Buttons("fac") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "P",command = lambda:Buttons("P") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "C",command = lambda:Buttons("C") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        
        tkinter.Button(window, text = "{.}",command = lambda:Buttons("fpf") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2093√",command = lambda:Buttons("root") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2082√",command = lambda:Buttons("sqroot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2083√",command = lambda:Buttons("cuberoot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "eˣ",command = lambda:Buttons("exp") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")


        tkinter.Button(keypad, text = "(",command = lambda:Buttons("(") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "-",command = lambda:Buttons("-") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 2 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "π",command = lambda:Buttons("pi") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "e",command = lambda:Buttons("e") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 18 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 6 ,rowspan = 3, columnspan = 7,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")

def EnableExceptFunction():
    global main_window,window, keypad,Hyp,Inv

    if currentMode == "Normal":
        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 14, column = 18 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(window, text = "(",command = lambda:Buttons("(") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 19, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "-",command = lambda:Buttons("-") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 3 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "π",command = lambda:Buttons("pi") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "e",command = lambda:Buttons("e") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 39, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")

        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 17 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 2 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
    elif currentMode == "Scientific":
        if Hyp == "Normal" and Inv == "Normal":
            tkinter.Button(window,state = "disabled",text = "ln",command = lambda:Buttons("logbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2082",command = lambda:Buttons("logb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2081\u2080",command = lambda:Buttons("logb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2093",command = lambda:Buttons("log") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window,state = "disabled", text = "sin",command = lambda:Buttons("sin") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "cos",command = lambda:Buttons("cos") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "tan",command = lambda:Buttons("tan") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        
        elif Hyp == "Normal":
            tkinter.Button(window,state = "disabled", text = "antiln",command = lambda:Buttons("antilogbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2082",command = lambda:Buttons("antilogb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2081\u2080",command = lambda:Buttons("antilogb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2093",command = lambda:Buttons("antilog") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window,state = "disabled", text = "sin\u207b\u00B9",command = lambda:Buttons("asin") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "cos\u207b\u00B9",command = lambda:Buttons("acos") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "tan\u207b\u00B9",command = lambda:Buttons("atan") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        elif Inv == "Normal":
            tkinter.Button(window,state = "disabled", text = "ln",command = lambda:Buttons("logbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2082",command = lambda:Buttons("logb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2081\u2080",command = lambda:Buttons("logb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "log\u2093",command = lambda:Buttons("log") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window,state = "disabled", text = "sinh",command = lambda:Buttons("sinh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "cosh",command = lambda:Buttons("cosh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "tanh",command = lambda:Buttons("tanh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        
        else:
            tkinter.Button(window,state = "disabled", text = "antiln",command = lambda:Buttons("antilogbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2082",command = lambda:Buttons("antilogb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2081\u2080",command = lambda:Buttons("antilogb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "antilog\u2093",command = lambda:Buttons("antilog") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

            tkinter.Button(window,state = "disabled", text = "sinh\u207b\u00B9",command = lambda:Buttons("asinh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "cosh\u207b\u00B9",command = lambda:Buttons("acosh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
            tkinter.Button(window,state = "disabled", text = "tanh\u207b\u00B9",command = lambda:Buttons("atanh") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 11 ,rowspan = 3, columnspan = 17,sticky = "nswe")

        tkinter.Button(window,state = "disabled", text = "[.]",command = lambda:Buttons("gif") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "|.|",command = lambda:Buttons("mod") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "!",command = lambda:Buttons("fac") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "P",command = lambda:Buttons("P") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "C",command = lambda:Buttons("C") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        
        tkinter.Button(window,state = "disabled", text = "{.}",command = lambda:Buttons("fpf") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "\u2093√",command = lambda:Buttons("root") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "\u2082√",command = lambda:Buttons("sqroot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "\u2083√",command = lambda:Buttons("cuberoot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = "eˣ",command = lambda:Buttons("exp") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")


        tkinter.Button(keypad, text = "(",command = lambda:Buttons("(") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "-",command = lambda:Buttons("-") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 2 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "π",command = lambda:Buttons("pi") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "e",command = lambda:Buttons("e") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 18 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 6 ,rowspan = 3, columnspan = 7,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")


def Buttons(btype):
    global currentMode, Equation, BracketsUnclosed, main_window, window, keypad
    print(btype)
    btype = str(btype)
    if btype == "Normal Window":
        currentMode = "Normal"
        Equation = "( 0"
        BracketsUnclosed = 1
        menubutton()
        WindowSelector()
    elif btype == "Scientific Window":
        currentMode = "Scientific"
        menubutton()
        WindowSelector()
    elif btype == "Settings Window":
        currentMode = "Settings"
        menubutton()
        WindowSelector()
    elif btype == "1":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "1"
            else:
                Equation += "1"
        except:
            Equation += " 1"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "2":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "2"
            else:
                Equation += "2"
        except:
            Equation += " 2"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "3":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "3"
            else:
                Equation += "3"
        except:
            Equation += " 3"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "4":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "4"
            else:
                Equation += "4"
        except:
            Equation += " 4"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "5":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "5"
            else:
                Equation += "5"
        except:
            Equation += " 5"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "6":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "6"
            else:
                Equation += "6"
        except:
            Equation += " 6"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "7":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "7"
            else:
                Equation += "7"
        except:
            Equation += " 7"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "8":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "8"
            else:
                Equation += "8"
        except:
            Equation += " 8"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "9":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "9"
            else:
                Equation += "9"
        except:
            Equation += " 9"
            EnableExceptFunction()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
    elif btype == "0":
        try:
            a = float(Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1])
            if a == 0:
                Equation = Equation[:len(Equation) - 1] + "0"
            elif str(a).__contains__(".") and str(a)[len(str(a)) - 1] == 0:
                pass
            else:
                Equation += "0"
        except:
            Equation += " 0"
            EnableAll()
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")

def WindowSelector():
    global main_window,Activestatecolor,Basiccolor,Oppbasiccolor,currentMode,CurrentInputValue,CurrentInputType,Hyp,Inv, BracketsUnclosed, Equation, window, keypad
    if currentMode == "Normal":
        window = tkinter.Frame(main_window, bg = Oppbasiccolor, highlightcolor = Activestatecolor, highlightbackground = Activestatecolor, highlightthickness = 5)
        i = 0
        while i < 28 :
            i += 1
            window.columnconfigure(i,minsize = 10,weight = 10,pad = 0)

        i = 0
        while i < 43 :
            i += 1
            window.rowconfigure(i,minsize = 10,weight = 10,pad = 0)
        
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Frame(window, bg = Activestatecolor).grid(row = 0, rowspan = 3, columnspan = 29, sticky = "nswe")
        tkinter.Frame(window, bg = Activestatecolor).grid(row = 3, rowspan = 6, columnspan = 6, sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
        tkinter.Button(window, text = "˅",command = lambda:Buttons("Down") ,font = "Comic 12 bold",bg = Basiccolor, highlightbackground = Basiccolor,highlightcolor = Basiccolor, fg = Oppbasiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 9, column = 0 ,rowspan = 2, columnspan = 3,sticky = "nswe")
        
        keypad = tkinter.Frame(window,bg = Oppbasiccolor, highlightthickness = 0)
        
        tkinter.Button(window, text = "CE",command = lambda:Buttons("CE") ,font = "Comic 10 bold",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 26 ,rowspan = 2, columnspan = 4,sticky = "nswe")
        tkinter.Button(window,state = "disabled", text = CurrentInputValue,command = lambda:Buttons(CurrentInputValue) ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 0 ,rowspan = 2, columnspan = 6,sticky = "nswe")
        tkinter.Button(window,state = "disabled",text = "Hyperbolic",command = lambda:Buttons(Hyp + " hyp") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Oppbasiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 7 ,rowspan = 2, columnspan = 6,sticky = "nswe")
        tkinter.Button(window,state = "disabled",text = "Inverse",command = lambda:Buttons(Inv + " inv") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Oppbasiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 14 ,rowspan = 2, columnspan = 5,sticky = "nswe")

        tkinter.Button(window,text = CurrentInputType,command = lambda:Buttons(CurrentInputType) ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 20 ,rowspan = 2, columnspan = 5,sticky = "nswe")
        tkinter.Button(window,text = "Copy",command = lambda:Buttons("copy") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 4, column = 0 ,rowspan = 2, columnspan = 6,sticky = "nswe")

        i = 2
        while 2 <= i <= 20 :
            keypad.columnconfigure(i,minsize = 10,weight = 10,pad = 0)
            i += 1

        i = 13
        while 13 <= i <= 36 :
            keypad.rowconfigure(i,minsize = 10,weight = 10,pad = 0)
            i += 1

        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 14, column = 18 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(window, text = "(",command = lambda:Buttons("(") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 19, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "-",command = lambda:Buttons("-") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 3 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "π",command = lambda:Buttons("pi") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(window, text = "e",command = lambda:Buttons("e") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 39, column = 3 ,rowspan = 4, columnspan = 4,sticky = "nswe")

        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 13, column = 17 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 23, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 2 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 7 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 17 ,rowspan = 9, columnspan = 4,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 2 ,rowspan = 4, columnspan = 9,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 18 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 33, column = 12 ,rowspan = 4, columnspan = 4,sticky = "nswe")
        keypad.grid(row = 19, column = 8, columnspan = 19, rowspan = 24)
        window.grid(row = 5,rowspan = 45,columnspan = 30,sticky = "nswe")
    
    elif currentMode == "Scientific":
        window = tkinter.Frame(main_window, bg = Oppbasiccolor, highlightcolor = Activestatecolor, highlightbackground = Activestatecolor, highlightthickness = 5)
        i = 0
        while i < 28 :
            i += 1
            window.columnconfigure(i,minsize = 10,weight = 10,pad = 0)

        i = 0
        while i < 43 :
            i += 1
            window.rowconfigure(i,minsize = 10,weight = 10,pad = 0)
        
        tkinter.Label(window,text = Equation.rsplit(" ")[len(Equation.rsplit(" ")) - 1], font = "Comic 36 bold",bg = Activestatecolor,fg = Basiccolor,anchor = "se").grid(column = 6,row = 3,rowspan = 6,columnspan = 23,sticky = "nswe")
        tkinter.Frame(window, bg = Activestatecolor).grid(row = 0, rowspan = 3, columnspan = 29, sticky = "nswe")
        tkinter.Frame(window, bg = Activestatecolor).grid(row = 3, rowspan = 6, columnspan = 6, sticky = "nswe")
        tkinter.Label(window,text = Equation, font = "Comic 12 bold",bg = Basiccolor,fg = Oppbasiccolor,anchor = "e").grid(row = 9,column = 3,rowspan = 2,columnspan = 27,sticky = "nswe")
        tkinter.Button(window, text = "˅",command = lambda:Buttons("Down") ,font = "Comic 12 bold",bg = Basiccolor, highlightbackground = Basiccolor,highlightcolor = Basiccolor, fg = Oppbasiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 9, column = 0 ,rowspan = 2, columnspan = 3,sticky = "nswe")
        
        keypad = tkinter.Frame(window,bg = Oppbasiccolor, highlightthickness = 0)
        
        tkinter.Button(window, text = "CE",command = lambda:Buttons("CE") ,font = "Comic 10 bold",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 26 ,rowspan = 2, columnspan = 4,sticky = "nswe")
        tkinter.Button(window,text = CurrentInputValue,command = lambda:Buttons(CurrentInputValue) ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 0 ,rowspan = 2, columnspan = 6,sticky = "nswe")
        tkinter.Button(window,text = "Hyperbolic",command = lambda:Buttons(Hyp + " hyp") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = "grey", activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 7 ,rowspan = 2, columnspan = 6,sticky = "nswe")
        tkinter.Button(window,text = "Inverse",command = lambda:Buttons(Inv + " inv") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = "grey", activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 14 ,rowspan = 2, columnspan = 5,sticky = "nswe")

        tkinter.Button(window,text = CurrentInputType,command = lambda:Buttons(CurrentInputType) ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 1, column = 20 ,rowspan = 2, columnspan = 5,sticky = "nswe")
        tkinter.Button(window,text = "Copy",command = lambda:Buttons("copy") ,font = "Comic 8",bg = Activestatecolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Oppbasiccolor, activeforeground = Basiccolor).grid(row = 4, column = 0 ,rowspan = 2, columnspan = 6,sticky = "nswe")

        i = 2
        while 2 <= i <= 20 :
            keypad.columnconfigure(i,minsize = 10,weight = 10,pad = 0)
            i += 1

        i = 18
        while 18 <= i <= 36 :
            keypad.rowconfigure(i,minsize = 10,weight = 10,pad = 0)
            i += 1
        tkinter.Button(window, text = "ln",command = lambda:Buttons("logbe") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        tkinter.Button(window, text = "log\u2082",command = lambda:Buttons("logb2") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        tkinter.Button(window, text = "log\u2081\u2080",command = lambda:Buttons("logb10") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 12, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        tkinter.Button(window, text = "sin",command = lambda:Buttons("sin") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        tkinter.Button(window, text = "cos",command = lambda:Buttons("cos") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 11 ,rowspan = 3, columnspan = 8,sticky = "nswe")
        tkinter.Button(window, text = "tan",command = lambda:Buttons("tan") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 16, column = 20 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        tkinter.Button(window, text = "log\u2093",command = lambda:Buttons("log") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 2 ,rowspan = 3, columnspan = 8,sticky = "nswe")

        tkinter.Button(window, text = "Backspace",command = lambda:Buttons("<") ,font = "Comic 10 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 20, column = 11 ,rowspan = 3, columnspan = 17,sticky = "nswe")

        tkinter.Button(window, text = "[.]",command = lambda:Buttons("gif") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "|.|",command = lambda:Buttons("mod") ,font = "Comic 16",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "!",command = lambda:Buttons("fac") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "P",command = lambda:Buttons("P") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "C",command = lambda:Buttons("C") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 25 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        
        tkinter.Button(window, text = "{.}",command = lambda:Buttons("fpf") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 24, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2093√",command = lambda:Buttons("root") ,font = "Comic 14",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 28, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2082√",command = lambda:Buttons("sqroot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 32, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "\u2083√",command = lambda:Buttons("cuberoot") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 36, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(window, text = "eˣ",command = lambda:Buttons("exp") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 40, column = 1 ,rowspan = 3, columnspan = 3,sticky = "nswe")


        tkinter.Button(keypad, text = "(",command = lambda:Buttons("(") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "-",command = lambda:Buttons("-") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 2 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "π",command = lambda:Buttons("pi") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "e",command = lambda:Buttons("e") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 2 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "^",command = lambda:Buttons("^") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "/",command = lambda:Buttons("/") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "*",command = lambda:Buttons("*") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = ")",command = lambda:Buttons(")") ,font = "Comic 14 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 18, column = 18 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "7",command = lambda:Buttons(7) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "8",command = lambda:Buttons(8) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "9",command = lambda:Buttons(9) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "+",command = lambda:Buttons("+") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 22, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "4",command = lambda:Buttons(4) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "5",command = lambda:Buttons(5) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "6",command = lambda:Buttons(6) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 26, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "1",command = lambda:Buttons(1) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 6 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "2",command = lambda:Buttons(2) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 10 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "3",command = lambda:Buttons(3) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "=",command = lambda:Buttons("=") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 30, column = 18 ,rowspan = 7, columnspan = 3,sticky = "nswe")
        tkinter.Button(keypad, text = "0",command = lambda:Buttons(0) ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 6 ,rowspan = 3, columnspan = 7,sticky = "nswe")
        tkinter.Button(keypad, text = ".",command = lambda:Buttons(".") ,font = "Comic 16 bold",bg = Oppbasiccolor,highlightbackground = Oppbasiccolor,highlightcolor = Oppbasiccolor, fg = Basiccolor, activebackground = Activestatecolor, activeforeground = Basiccolor).grid(row = 34, column = 14 ,rowspan = 3, columnspan = 3,sticky = "nswe")
        keypad.grid(row = 24, column = 5, columnspan = 19, rowspan = 19)
        window.grid(row = 5,rowspan = 45,columnspan = 30,sticky = "nswe")
    
    elif currentMode == "Settings":
        window = tkinter.Frame(main_window, bg = Oppbasiccolor, highlightcolor = Activestatecolor, highlightbackground = Activestatecolor, highlightthickness = 5)
        i = 0
        while i < 28 :
            i += 1
            window.columnconfigure(i,minsize = 10,weight = 10,pad = 0)

        i = 0
        while i < 43 :
            i += 1
            window.rowconfigure(i,minsize = 10,weight = 10,pad = 0)


        window.grid(row = 5,rowspan = 45,columnspan = 30,sticky = "nswe")

def SettingsManager(command):
    if command == "Load":
        try:
            a = open(path + "/Settings.vcalc","w")
        except:
            a = open(path + "/Settings.vcalc","w+")
            

menubutton()
WindowSelector()

main_window.mainloop()

