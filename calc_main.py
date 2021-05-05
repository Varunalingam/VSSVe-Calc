import tkinter
import math
import time


main_window = tkinter.Tk()
main_window.title("VSSVE Calc")
main_window.iconbitmap("logo.bmp")

a = 0
b = None
o = "+"
oo = None
calc = "0+"

def Operation(a,o,oo,b):
    try:
        a = float(a)
        if b == None:
            b = 0
            if oo == None:
                if o == "+":
                    return a + b
                elif o == "-" or o == "~":
                    return a - b
                elif o == "*":
                    return a * b
                elif o == "/":
                    try:
                        return a/b
                    except ZeroDivisionError:
                        calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 5! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                        tkinter.Label(calculations_Label).update()
                        time.sleep(2)
                        exit()
                elif o == "^":
                    return a ** b
                else:
                    return a
            else:
                if oo == "sin":
                    return Operation(a,o,None,math.sin(b))
                elif oo == "cos":
                    return Operation(a,o,None,math.cos(b))
                elif oo == "tan":
                    return Operation(a,o,None,math.tan(b))
                elif oo == "sin\u207B\u00B9":
                    return Operation(a,o,None,math.asin(b))
                elif oo == "cos\u207B\u00B9":
                    return Operation(a,o,None,math.acos(b))
                elif oo == "tan\u207B\u00B9":
                    return Operation(a,o,None,math.atan(b))
                elif oo == "fpf":
                    if b >= 0:
                        return Operation(a,o,None,b - int(b))
                    else:
                        return Operation(a,o,None,b - (int(b) - 1))
                elif oo == "gif":
                    if b >= 0:
                        return Operation(a,o,None,int(b))
                    elif int(b) == b:
                        return Operation(a,o,None,int(b))
                    else:
                        return Operation(a,o,None,int(b) - 1)
                elif oo == "sgn":
                    if b > 0:
                        return Operation(a,o,None,1)
                    elif b == 0:
                        return Operation(a,o,None,0)
                    else:
                        return Operation(a,o,None,-1)
                elif oo == "!":
                    try:
                        return Operation(a,o,None,math.factorial(b))
                    except ValueError:
                        calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 5! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                        tkinter.Label(calculations_Label).update()
                        time.sleep(2)
                        exit()
                elif oo == "ln":
                    return Operation(a,o,None,math.log(b,math.e))
                elif oo == "log\u2081\u2080":
                    return Operation(a,o,None,math.log10(b))
                elif oo == "log\u2082":
                    return Operation(a,o,None,math.log2(b))
                elif oo == "log\u2083":
                    return Operation(a,o,None,math.log(b,3))
                elif oo == "ln\u207B\u00B9":
                    return Operation(a,o,None,math.e ** b)
                elif oo == "log\u207B\u00B9\u2081\u2080":
                    return Operation(a,o,None,10 ** b)
                elif oo == "log\u207B\u00B9\u2082":
                    return Operation(a,o,None,2 ** b)
                elif oo == "log\u207B\u00B9\u2083":
                    return Operation(a,o,None,3 ** b)
                else:
                    calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 6! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                    tkinter.Label(calculations_Label).update()
                    time.sleep(2)
                    exit()
        elif b == "π":
            return Operation(a,o,oo,math.pi)
        elif b == "e":
            return Operation(a,o,oo,math.e)
        else:
            b = float(b)
            if oo == None:
                if o == "+":
                    return a + b
                elif o == "-" or o == "~":
                    return a - b
                elif o == "*":
                    return a * b
                elif o == "/":
                    try:
                        return a/b
                    except ZeroDivisionError:
                        calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 5! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                        tkinter.Label(calculations_Label).update()
                        time.sleep(2)
                        exit()
                elif o == "^":
                    return a ** b
                else:
                    return a
            else:
                if oo == "sin":
                    return Operation(a,o,None,math.sin(b))
                elif oo == "cos":
                    return Operation(a,o,None,math.cos(b))
                elif oo == "tan":
                    return Operation(a,o,None,math.tan(b))
                elif oo == "sin\u207B\u00B9":
                    return Operation(a,o,None,math.asin(b))
                elif oo == "cos\u207B\u00B9":
                    return Operation(a,o,None,math.acos(b))
                elif oo == "tan\u207B\u00B9":
                    return Operation(a,o,None,math.atan(b))
                elif oo == "fpf":
                    if b >= 0:
                        return Operation(a,o,None,b - int(b))
                    else:
                        return Operation(a,o,None,b - (int(b) - 1))
                elif oo == "gif":
                    if b >= 0:
                        return Operation(a,o,None,int(b))
                    elif int(b) == b:
                        return Operation(a,o,None,int(b))
                    else:
                        return Operation(a,o,None,int(b) - 1)
                elif oo == "sgn":
                    if b > 0:
                        return Operation(a,o,None,1)
                    elif b == 0:
                        return Operation(a,o,None,0)
                    else:
                        return Operation(a,o,None,-1)
                elif oo == "mod":
                    if b > 0:
                        return Operation(a,o,None,b)
                    elif b == 0:
                        return Operation(a,o,None,0)
                    else:
                        return Operation(a,o,None,-b)
                elif oo == "!":
                    try:
                        return Operation(a,o,None,math.factorial(b))
                    except ValueError:
                        calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 5! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                        tkinter.Label(calculations_Label).update()
                        time.sleep(2)
                        exit()
                elif oo == "ln":
                    return Operation(a,o,None,math.log(b,math.e))
                elif oo == "log\u2081\u2080":
                    return Operation(a,o,None,math.log10(b))
                elif oo == "log\u2082":
                    return Operation(a,o,None,math.log2(b))
                elif oo == "log\u2083":
                    return Operation(a,o,None,math.log(b,3))
                elif oo == "ln\u207B\u00B9":
                    return Operation(a,o,None,math.e ** b)
                elif oo == "log\u207B\u00B9\u2081\u2080":
                    return Operation(a,o,None,10 ** b)
                elif oo == "log\u207B\u00B9\u2082":
                    return Operation(a,o,None,2 ** b)
                elif oo == "log\u207B\u00B9\u2083":
                    return Operation(a,o,None,3 ** b)
                else:
                    calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 6! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                    tkinter.Label(calculations_Label).update()
                    time.sleep(2)
                    exit()
    except ValueError:
        calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 4! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
        tkinter.Label(calculations_Label).update()
        time.sleep(2)
        exit()

def close(c):
    global helptext
    helptext = tkinter.Label(main_window,text = "Copyrighted to VSSVE.inc by copyrights 2017",bg = "Black", fg = "white", anchor = "n").grid(row = 8, columnspan = 6, rowspan = 2, sticky = "nswe")

def Button(input):
    global calc
    global a
    global b
    global o
    global oo
    global helptext
    calc = calc + str(input)
    calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
    tkinter.Label(calculations_sub).update()
    if (str(input).lower() == "exit"):
        exit()
    elif str(input).lower() == "help":
        help = "Help Menu\nFor Negative No use -() Button.\nFor Negative Function use -().\nCalc Calculates Linearly not according to BODMAS"
        calc = calc[:-4]
        calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
        tkinter.Label(calculations_sub).update()
        helptext = tkinter.Label(main_window, bg = "gray", fg = "white", text = help).grid(row = 8, columnspan = 6, sticky = "nswe")
        Close = tkinter.Button(main_window,bg = "black",fg = "white",text = "Close",highlightbackground = "black",command = lambda: close(Close)).grid(row = 9, columnspan = 6)
    elif str(input).lower() == "ce":
        a = 0
        b = None
        o = "+"
        oo = None
        calc = "0+"
        calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
        calculations_Label = tkinter.Label(main_window, text = "0", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
    elif input == "=":
        a = Operation(a,o,oo,b)
        o = "+"
        oo = None
        b = None
        calc = str(a) + str(o)
        calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
        tkinter.Label(calculations_sub).update()
        calculations_Label = tkinter.Label(main_window, text = str(a) + str(o), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
        tkinter.Label(calculations_Label).update()
    elif o != None and b == None and oo == None:
        if type(input) == type(0):
            b = str(input)
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "pi":
            b = "π"
            calc = calc[:-3] + "π"
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "e":
            b = "e"
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == ".":
            b = str("0" + ".")
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "-" and o == "+":
            o = input
            calc = calc[:-2] + input
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "-":
            b = str("-")
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input != "+" and input != "~" and input != "*" and input != "/" and input != "^":
            oo = str(input)
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "~":
            o = "-"
            calc = calc[:-2] + "-"
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            calculations_Label = tkinter.Label(main_window, text = str(a) + str("-"), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()            
        else:
            o = input
            calc = calc[:-2] + input
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
    elif o != None and b == None:
        if type(input) == type(0):
            b = str(input)
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "pi":
            b = "π"
            calc = calc[:-3] + "π"
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "e":
            b = "e"
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == ".":
            b = str("0" + ".")
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "-":
            b = str("-")
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input != "+" and input != "~" and input != "*" and input != "/" and input != "^":
            calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 3! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
            time.sleep(2)
            exit()
        else:
            calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 1! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
            time.sleep(2)
            exit()
    elif o != None:
        if type(input) == type(0) or input == ".":
            if b != "π" and b!= "e":
                b = b + str(input)
                if oo == None:
                    calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                    tkinter.Label(calculations_Label).update()
                else:
                    calculations_Label = tkinter.Label(main_window, text = str(a) + str(o) + str(oo) + str(b), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                    tkinter.Label(calculations_Label).update()
            else:
                calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 2! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
                tkinter.Label(calculations_Label).update()
                time.sleep(2)
                exit()
        elif input == "~":
            calc = calc[:-2] + "-"
            calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
            tkinter.Label(calculations_sub).update()
            a = Operation(a, o , oo, b)
            o = str("-")
            oo = None
            b = None
            calculations_Label = tkinter.Label(main_window, text = str(a) + str("-"), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        elif input == "+" or input == "*" or input =="/" or input =="^" or input == "-":
            a = Operation(a, o , oo, b)
            o = str(input)
            oo = None
            b = None
            calculations_Label = tkinter.Label(main_window, text = str(a) + str(o), bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
        else:
            calculations_Label = tkinter.Label(main_window, text = "Syntax Error Code 2! App to Quit!", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 18)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)
            tkinter.Label(calculations_Label).update()
            time.sleep(2)
            exit()
    else:
        None

calculations_sub = tkinter.Label(main_window, text = calc, bg = "black", fg = "gray",anchor = "e" ,font = ("Courier", 18)).grid(row = 0, sticky = "nswe", columnspan = 5)
calculations_Label = tkinter.Label(main_window, text = "0", bg = "black", fg = "White",anchor = "e" ,font = ("Courier", 36)).grid(row = 1, sticky = "nswe", columnspan = 5, rowspan = 2)

button9 = tkinter.Button(main_window,bg = "black",fg = "white", text = "9",command = lambda:Button(9), highlightbackground = "Black", font = ("Courier","25")).grid(column = 2, row = 4, sticky = "nswe")
button8 = tkinter.Button(main_window,bg = "black",fg = "white", text = "8",command = lambda:Button(8), font = ("Courier","25"), highlightbackground = "Black").grid(column = 1, row = 4, sticky = "nswe")
button7 = tkinter.Button(main_window,bg = "black",fg = "white", text = "7",command = lambda:Button(7), font = ("Courier","25"), highlightbackground = "Black").grid(column = 0, row = 4, sticky = "nswe")
button6 = tkinter.Button(main_window,bg = "black",fg = "white", text = "6",command = lambda:Button(6), font = ("Courier","25"), highlightbackground = "Black").grid(column = 2, row = 5, sticky = "nswe")
button5 = tkinter.Button(main_window,bg = "black",fg = "white", text = "5",command = lambda:Button(5), font = ("Courier","25"), highlightbackground = "Black").grid(column = 1, row = 5, sticky = "nswe")
button4 = tkinter.Button(main_window,bg = "black",fg = "white", text = "4",command = lambda:Button(4), font = ("Courier","25"), highlightbackground = "Black").grid(column = 0, row = 5, sticky = "nswe")
button3 = tkinter.Button(main_window,bg = "black",fg = "white", text = "3",command = lambda:Button(3), font = ("Courier","25"), highlightbackground = "Black").grid(column = 2, row = 6, sticky = "nswe")
button2 = tkinter.Button(main_window,bg = "black",fg = "white", text = "2",command = lambda:Button(2), font = ("Courier","25"), highlightbackground = "Black").grid(column = 1, row = 6, sticky = "nswe")
button1 = tkinter.Button(main_window,bg = "black",fg = "white", text = "1",command = lambda:Button(1), font = ("Courier","25"), highlightbackground = "Black").grid(column = 0, row = 6, sticky = "nswe")
button0 = tkinter.Button(main_window,bg = "black",fg = "white", text = "0",command = lambda:Button(0), font = ("Courier","25"), highlightbackground = "Black").grid(column = 0, row = 7, columnspan = 2, sticky = "nswe")
buttondot = tkinter.Button(main_window,bg = "black",fg = "white", text = ".",command = lambda:Button("."), font = ("Courier","25"), highlightbackground = "Black").grid(column = 2, row = 7, sticky = "nswe")
buttoneq = tkinter.Button(main_window,bg = "black",fg = "white", text = "=",command = lambda:Button("="), font = ("Courier","25"), highlightbackground = "Black").grid(column = 3, row = 7, sticky = "nswe")
buttonplus = tkinter.Button(main_window,bg = "black",fg = "white", text = "+",command = lambda:Button("+"), font = ("Courier","25"), highlightbackground = "Black").grid(column = 3, row = 6, sticky = "nswe")
buttonsub = tkinter.Button(main_window,bg = "black",fg = "white", text = "-",command = lambda:Button("-"), font = ("Courier","25"), highlightbackground = "Black").grid(column = 3, row = 5, sticky = "nswe")
buttonmul = tkinter.Button(main_window,bg = "black",fg = "white", text = "*",command = lambda:Button("*"), font = ("Courier","25"), highlightbackground = "Black").grid(column = 3, row = 4, sticky = "nswe")
buttondiv = tkinter.Button(main_window,bg = "black",fg = "white", text = "/",command = lambda:Button("/"), font = ("Courier","22"), highlightbackground = "Black").grid(column = 3, row = 3, sticky = "nswe")
buttonexp = tkinter.Button(main_window,bg = "black",fg = "white", text = "^",command = lambda:Button("^"), font = ("Courier","22"), highlightbackground = "Black").grid(column = 2, row = 3, sticky = "nswe")
buttonce = tkinter.Button(main_window,bg = "black",fg = "white", text = "CE",command = lambda:Button("CE"), font = ("Courier","15"), highlightbackground = "Black").grid(column = 0, row = 3, sticky = "nswe")
buttonexit = tkinter.Button(main_window,bg = "black",fg = "white", text = "Off",command = lambda:Button("exit"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 0, sticky = "nswe")
buttone = tkinter.Button(main_window,bg = "black",fg = "white", text = "e",command = lambda:Button("e"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 4, row = 3, sticky = "nswe")
buttonsgn = tkinter.Button(main_window,bg = "black",fg = "white", text = "Sgn",command = lambda:Button("sgn"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 3, sticky = "nswe")
buttonsin = tkinter.Button(main_window,bg = "black",fg = "white", text = "Sin",command = lambda:Button("sin"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 4, row = 4, sticky = "nswe")
buttoncos = tkinter.Button(main_window,bg = "black",fg = "white", text = "Cos",command = lambda:Button("cos"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 4, row = 5, sticky = "nswe")
buttontan = tkinter.Button(main_window,bg = "black",fg = "white", text = "Tan",command = lambda:Button("tan"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 4, row = 6, sticky = "nswe")
buttonasin = tkinter.Button(main_window,bg = "black",fg = "white", text = 'Sin\u207B\u00B9' ,command = lambda:Button("sin\u207B\u00B9"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 4, sticky = "nswe")
buttonacos = tkinter.Button(main_window,bg = "black",fg = "white", text = "Cos\u207B\u00B9",command = lambda:Button("cos\u207B\u00B9"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 5, sticky = "nswe")
buttonatan = tkinter.Button(main_window,bg = "black",fg = "white", text = "Tan\u207B\u00B9",command = lambda:Button("tan\u207B\u00B9"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 6, sticky = "nswe")
buttonMod = tkinter.Button(main_window,bg = "black",fg = "white", text = "|.|",command = lambda:Button("mod"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 7, sticky = "nswe")
buttonafac = tkinter.Button(main_window,bg = "black",fg = "white", text = "!",command = lambda:Button("!"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 4, row = 7, sticky = "nswe")
buttonfpf = tkinter.Button(main_window,bg = "black",fg = "white", text = "{.}",command = lambda:Button("fpf"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 2, sticky = "nswe")
buttongif = tkinter.Button(main_window,bg = "black",fg = "white", text = "[.]",command = lambda:Button("gif"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 5, row = 1, sticky = "nswe")
buttonpi = tkinter.Button(main_window,bg = "black",fg = "white", text = "π",command = lambda:Button("pi"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 1, row = 3, sticky = "nswe")
buttonln = tkinter.Button(main_window,bg = "black",fg = "white", text = "ln",command = lambda:Button("ln"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 6, row = 4, sticky = "nswe")
buttonlog10 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u2081\u2080",command = lambda:Button("log\u2081\u2080"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 5, sticky = "nswe")
buttonlog2 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u2082",command = lambda:Button("log\u2082"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 6, sticky = "nswe")
buttonlog3 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u2083",command = lambda:Button("log\u2083"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 7, sticky = "nswe")
buttonln = tkinter.Button(main_window,bg = "black",fg = "white", text = "ln\u207B\u00B9",command = lambda:Button("ln\u207B\u00B9"), font = ("Courier","18"), highlightbackground = "Black").grid(column = 6, row = 0, sticky = "nswe")
buttonlog10 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u207B\u00B9\u2081\u2080",command = lambda:Button("log\u207B\u00B9\u2081\u2080"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 1, sticky = "nswe")
buttonlog2 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u207B\u00B9\u2082",command = lambda:Button("log\u207B\u00B9\u2082"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 2, sticky = "nswe")
buttonlog3 = tkinter.Button(main_window,bg = "black",fg = "white", text = "log\u207B\u00B9\u2083",command = lambda:Button("log\u207B\u00B9\u2083"), font = ("Courier","16"), highlightbackground = "Black").grid(column = 6, row = 3, sticky = "nswe")

helptext = tkinter.Label(main_window,text = "Copyrighted to VSSVE.inc under copyrights 2017.",bg = "Black", fg = "white").grid(row = 8, columnspan = 7,rowspan = 2, sticky = "nswe")

main_window.mainloop()