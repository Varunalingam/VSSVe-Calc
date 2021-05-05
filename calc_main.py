import math

def Help():
    print("\n\t\t Help Menu\n\nOperators:\n\nAdd: Num1 + Num2\nSub: Num1 ~ Num2\nMultiply: Num1 * Num2 (or) Num1 x Num2 (or) Num1 X Num2")
    print("Divide: Num1 / Num2 (for Num2 not equals Zero)\nExponential: Num1 ^ Num2\n\nFunctions\n\nSine: sin Num3 (or) sine Num3")
    print("Cosine: cos Num3 (or) cosine Num3\nTangent: tan Num3 or tangent Num3\nSine Inverse: asin Num3 (or) asine Num3")
    print("Cosine Inverse: acos Num3 (or) acosine Num3\nTangent Inverse: atan Num3 (or) atangent Num3\nGreatest Integer: gif Num1 (or) gi Num1")
    print("Fractional Part: fpf Num1 (or) fp Num1\nModulus: mod Num1 (or) modulus Num1\nSignum: sgn Num1")
    print("Factorial: ! Num4 (or) factorial Num4")
    print("\nNum1, Num2 and Num3 can be any real number.\nNum4 can be Zero or Positive Integer Only\n\tFor Negative No:\n\t eg) -1\n\t    -sin 1 (Wrong Syntax)\nNote: Num3 functions consider Num3 to be in radians unit\nNo Other Syntax are allowed")
    print("Brackets are not allowed\nCalculations are made Leniarly not according to BODMAS\n\t eg) 1 + 2 * 3 = 3 * 3 = 9(correct)\n\t     1 + 2 * 3 = 1 + 6 = 7(Wrong)\n")
    print("\n\t\t Error Codes\nError Code 1,2,3,4,6,7,8,9,10,11,13,14,15 : Syntax Error\nError Code 12: Usage of Non Integral (or) Negative Integral Number in Factorial Function\nError Code 5 : Zero Division Error(Usage of Zero as Num2 in Division)")

def operation(a , o , b):
    if o == "+":
        return a + b
    elif o == "~":
        return a - b
    elif o == "*" or o == "X" or o == "x":
        return a * b 
    elif o == "/":
        try:
            return a / b
        except ZeroDivisionError:
            print("\nError Code 5: Value Not Defined, Mathematically\n App to Restart....\n")
            main()
    elif o == "^":
        return a ** b
    elif o == None and b == None or o == "" and b == 0:
        return a
    else:
        print("Syntax Error Code 7. App to Quit")
        exit()

def Calculator(main_stream):
    a = None
    o = None
    b = None

    for cmd in main_stream:
        if a == None:
            try:
                a = float(cmd)
            except ValueError:
                print("\nSyntax Error Code 13! App to Quit")
                exit()
        elif o == None:
            o = cmd
        else:
            try:
                b = float(cmd)
                a = operation( a, o, b)
                o = None
                b = None
            except ValueError:
                print("\nSyntax Error Code 14!App to Quit")
                exit()
    if o == None:
        print ("\n= " + str(a))
        stream = input("\n(ce\\help\\quit\\exit) Calculations : " + str(a) + " ")
        if stream.lower() == "help":
            Help()
            stream = input("\n(ce\\quit\\exit) Calculations : " + str(a) + " ")
            if stream.lower() == "quit" or stream.lower() == "exit":
                print("\nThanks for using VSSVE Calc\n")
                exit()
            elif stream.lower() == "ce":
                main()
            else:
                stream = str(a) + stream
                parser(stream)
        elif stream.lower() == "quit" or stream.lower() == "exit":
            print("\nThanks for using VSSVE Calc\n")
            exit()
        elif stream.lower() == "ce":
            main()
        else:
            stream = str(a) + stream
            parser(stream)
    else:
        print("\nSyntax Error Code 15. App to Quit!")
        exit()

def SingleOperand_calc(main_stream):
    secondary_stream = []
    z = 0
    i = -1
    for set in main_stream:
        set = str(set)
        i = i + 1
        if z == 0:
            if set.lower() == "sin" or set.lower() == "sine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.sin(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "cos" or set.lower() == "cosine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.cos(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "tan" or set.lower() == "tangent":
                z = i + 1
                try:
                    secondary_stream.append(str(math.tan(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "asin" or set.lower() == "asine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.asin(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "acos" or set.lower() == "acosine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.acos(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "atan" or set.lower() == "atangent":
                z = i + 1
                try:
                    secondary_stream.append(str(math.atan(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "gif" or set.lower() == "gi":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(int(c)))
                    elif c == int(c):
                        secondary_stream.append(str(int(c)))
                    else:
                        secondary_stream.append(str(int(c) - 1))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "mod" or set.lower() == "modulus":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(c))
                    else:
                        secondary_stream.append(str(c * (-1)))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "fpf" or set.lower() == "fractionalpart":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(c - int(c)))
                    elif c == int(c):
                        secondary_stream.append(str(0))
                    else:
                        secondary_stream.append(str(c - (int(c) - 1)))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "sgn":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c > 0:
                        secondary_stream.append(str(1))
                    elif c == 0:
                        secondary_stream.append(str(0))
                    else:
                        secondary_stream.append(str(-1))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "factorial" or set == "!":
                z = i + 1
                try:
                    c = int(main_stream[z])
                    if c > 0:
                        secondary_stream.append(str(math.factorial(int(c))))
                    elif c == 0:
                        secondary_stream.append(str(1))
                    else:
                        print("Syntax Error Code 12 - Factorial Input as positive Integer or 0 Only. App to Quit")
                        exit()
                except ValueError:
                    print("Syntax Error Code 12 - Factorial Input as positive Integer or 0 Only. App to Quit")
                    exit()
            else:
                secondary_stream.append(set)  
        elif main_stream[z] == set:
            pass
        else:
            if set.lower() == "sin" or set.lower() == "sine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.sin(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "cos" or set.lower() == "cosine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.cos(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "tan" or set.lower() == "tangent":
                z = i + 1
                try:
                    secondary_stream.append(str(math.tan(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "asin" or set.lower() == "asine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.asin(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "acos" or set.lower() == "acosine":
                z = i + 1
                try:
                    secondary_stream.append(str(math.acos(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "atan" or set.lower() == "atangent":
                z = i + 1
                try:
                    secondary_stream.append(str(math.atan(float(main_stream[z]))))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "gif" or set.lower() == "gi":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(int(c)))
                    else:
                        secondary_stream.append(str(int(c) - 1))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "mod" or set.lower() == "modulus":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(c))
                    else:
                        secondary_stream.append(str(c * (-1)))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "fpf" or set.lower() == "fractionalpart":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c >= 0:
                        secondary_stream.append(str(c - int(c)))
                    else:
                        secondary_stream.append(str(c - (int(c) - 1)))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "sgn":
                z = i + 1
                try:
                    c = float(main_stream[z])
                    if c > 0:
                        secondary_stream.append(str(1))
                    elif c == 0:
                        secondary_stream.append(str(0))
                    else:
                        secondary_stream.append(str(-1))
                except ValueError:
                    print("Syntax Error Code 10. App to Quit")
                    exit()
            elif set.lower() == "factorial" or set == "!":
                z = i + 1
                try:
                    c = int(main_stream[z])
                    if c > 0:
                        secondary_stream.append(str(math.factorial(int(c))))
                    elif c == 0:
                        secondary_stream.append(str(1))
                    else:
                        print("Syntax Error Code 12 - Factorial Input as positive Integer or 0 Only. App to Quit")
                        exit()
                except ValueError:
                    print("Syntax Error Code 12 - Factorial Input as positive Integer or 0 Only. App to Quit")
                    exit()
            else:
                secondary_stream.append(set)  
    
    Calculator(secondary_stream)

def CalculatorSetParser(main_stream):
    
    stream = []
    string = None
    for set in main_stream:
        if string == None:
            try:
                float(set)
                string = set
            except ValueError:
                string = None
                if set == "-":
                    string = set
                else:
                    stream.append(set)
            except:
                print("\nSyntax Error Code 3. App to Quit")
                exit()
        elif set == ".":
            string = string + set
        else:
            try:
                float(set)
                string = string + set
                stream.append(string)
                string = None
            except ValueError:
                stream.append(string)
                stream.append(set)
                string = None
            except:
                print("\nSyntax Error Code 4. App to Quit!")
                exit()
    
    if string != None:
        stream.append(string)
        SingleOperand_calc(stream)
    else:
        SingleOperand_calc(stream)


def parser(main_stream):
    main_stream = str(main_stream).split(None)
    
    stream = []

    for sts in main_stream:
        for letter in sts:
            stream.append(letter)
    
    main_stream = []

    string = None
    string_char = None
    for letter in stream:
        try:
            float(letter)
            if string == None and string_char == None:
                string = letter
            elif string == None:
                main_stream.append(string_char)
                string = letter
                string_char = None
            elif string_char == None:
                string = string + letter
            else:
                main_stream.append(string_char)
                string = string + letter
                string_char = None
        except ValueError:
            if string_char == None and string == None:
                if letter == "+" or letter == "~" or letter == "*" or letter == "/" or letter == "X" or letter == "x" or letter == "^":
                    main_stream.append(letter)
                elif letter == "-":
                    string = "-"
                else:
                    string_char = letter
            elif string_char == None:
                main_stream.append(string)
                string = None
                if letter == "+" or letter == "~" or letter == "*" or letter == "/" or letter == "X" or letter == "x" or letter == "^":
                    main_stream.append(letter)
                elif letter == "-":
                    string = letter
                else:
                    string_char = letter
            elif string == None:
                if letter == "+" or letter == "~" or letter == "*" or letter == "/" or letter == "X" or letter == "x" or letter == "^":
                    print("Syntax Error Code 2. App to Quit")
                    exit()
                elif letter == "-":
                    string = letter
                else:
                    string_char = string_char + letter
            else:
                main_stream.append(string)
                string = None
                if letter == "+" or letter == "~" or letter == "*" or letter == "/" or letter == "X" or letter == "x" or letter == "^":
                    print("Syntax Error Code 2.App to Quit")
                elif letter == "-":
                    main_stream.append(string_char)
                    string_char = None
                    string = letter
                else:
                    string_char = string_char + letter
    if string == None and string_char == None:
        CalculatorSetParser(main_stream)
    elif string == None:
        print("\nSyntax Error Code 11. App to Quit")
        exit()
    elif string_char == None:
        main_stream.append(string)
        CalculatorSetParser(main_stream)
    else:
        main_stream.append(string_char)
        main_stream.append(string)
        CalculatorSetParser(main_stream)

def main():
    print("\nVSSVE Calc v1 Python3.6 \nFor Clear Calculations - type CE in syntax, For Help - type help in syntax , To Quit - type quit or exit in Syntax\n(Not Case Sensitive)")
    main_stream = str(input("\nCalculations :"))
    if main_stream.lower() == "help":
        Help()
        main()
    elif main_stream.lower() == "quit" or main_stream.lower() == "exit":
        print("\nThanks for using VSSVE Calc\n")
        exit()
    elif main_stream.lower() == "ce":
        main()
    parser(main_stream)


main()