import math
           

global SyntaxErrorCode, radians, CannotDivideErrorCode, BODMAS

BODMAS = True
SyntaxErrorCode = "Syntax Error 1"
radians = "radians"
CannotDivideErrorCode = "Math Error 201: Division by Zero is Invalid"

def VSSVEBODMASCalc(parse, BODMASbool, Radians, insymbols, seperator = " "):
    global BODMAS, radians
    BODMAS = BODMASbool
    radians = Radians
    a = parser(str(parse).rsplit(seperator))
    try:
        if insymbols and float(a) != 0 :
            if float(float(a)/math.pi) == int(float(a)/math.pi):
                return str(int(float(a)/math.pi)) + "π"
            elif float(float(a)/math.e) == int(float(a)/math.e):
                return str(int(float(a)/math.e)) + "e"
            elif float(a) == math.pi * math.e:
                return "e * π"
            else:
                return a
        else:
            return a
    except:
        return a

def parser (parse):
    global radians, BODMAS
    if len(parse) > 1:
        alreadyop = False
        index = -1
        newparse = []
        for i in parse:
            index += 1
            if (i == "*" or i == "+" or i == "/" or i == "-" or i == "^" or i == "("):
                if alreadyop:
                    alreadyop = False
                    if i == "+" or i == "-":
                        if index > 0:
                            newparse = parse[:index]
                        
                        if parse[index + 1] == "*" or parse[index + 1] == "/" or parse[index + 1] == "^" or parse[index + 1] == ")":
                            return SyntaxErrorCode + "80 : Formation Error - Irregular Formation"
                        else:
                            if parse[index + 1] == "(":
                                newparse.append(i + "1")
                                if len(parse) > index + 1:
                                    newparse = newparse + parse[index + 1:]
                                return parser(newparse)
                            else:
                                try:
                                    a = float(parse[index + 1])
                                    newparse.append(str(float(i + "1") * a))
                                    if len(parse) > index + 2:
                                        newparse = newparse + parse[index + 2:]
                                    return parser(newparse)
                                except ValueError:
                                    newparse.append(i + "1")
                                    newparse.append("*")
                                    if len(parse[index + 1:]) > index + 1:
                                        newparse = newparse + parse[index + 1:]
                                    return parser(newparse)
                                except:
                                    return SyntaxErrorCode + "80 : Formation Error - Irregular Formation"
                    else:
                        return SyntaxErrorCode + "80 : Formation Error - Irregular Formation"
                else :
                    alreadyop = True
            else :
                alreadyop = False

        truevariable = False
        truevariableLocation = 0
        truevariabletookplace = False
        index = -1
        newparse = list()
        for a in parse:
            index += 1
            if truevariabletookplace == False:
                if a == "(":
                    truevariableLocation = index
                    truevariable = True
                elif a == ")":
                    if truevariable:
                        calcv = calc(parse[truevariableLocation + 1: index])
                        try:
                            calcv = float(calcv)
                        except:
                            return calcv
                        
                        truevariabletookplace = True
                        truevariable = False
                        if truevariableLocation - 1 >= 0 :
                            newparse = parse[:truevariableLocation - 1] 
                            try :
                                float(parse[truevariableLocation - 1])
                                newparse.append(parse[truevariableLocation - 1])
                                newparse.append("*")
                                newparse.append(calcv)    
                            except ValueError:
                                calcv = float(calcv)
                                if parse[truevariableLocation - 1] == "exp":
                                    calcv = math.exp(calcv)
                                elif parse[truevariableLocation - 1] == "fac":
                                    if int(calcv) == float(calcv) and calcv >=0 :
                                        calcv = math.factorial(calcv)
                                    else:
                                        return SyntaxErrorCode + "98 : Factorial Error: Factorial Can be performed only for Whole Numbers"
                                elif parse[truevariableLocation - 1] == "gif":
                                    if calcv >= 0:
                                        calcv = math.modf(calcv)[1]
                                    else:
                                        calcv = math.modf(calcv)[1] - 1
                                elif parse[truevariableLocation - 1] == "fpf":
                                    if calcv >= 0:
                                        calcv = math.modf(calcv)[0]
                                    else:
                                        calcv = math.modf(calcv)[0] + 1
                                elif parse[truevariableLocation - 1] == "mod":
                                    if calcv >= 0:
                                        calcv = calcv
                                    else:
                                        calcv = -calcv
                                elif parse[truevariableLocation - 1].__contains__ == "antilog":
                                    b = parse[truevariableLocation - 1].rsplit("b")[1]
                                    if b == "e":
                                        calcv = math.e ^ calcv
                                    elif b >= 0 and b != 1:
                                        calcv = b ^ calcv
                                    elif b == 1:
                                        return SyntaxErrorCode + "41 : AntiLogrithmic Base Error - Cannot be One"
                                    else:
                                        return SyntaxErrorCode + "42 : AntiLogrithmic Base Error - Cannot be Negative"
                                elif parse[truevariableLocation - 1].__contains__ == "log":
                                    x = parse[truevariableLocation - 1].rsplit("b")[1]
                                    if x == "2":
                                        calcv = math.log2(calcv)
                                    elif x == "e":
                                        calcv = math.log(calcv)
                                    elif x == "10":
                                        calcv = math.log10(calcv)
                                    elif float(x) >= 0 and float(x) != 1:
                                        calcv = math.log(calcv,x)
                                    elif float(x) == 1:
                                        return SyntaxErrorCode + "11 : Logrithmic Base Error - Cannot be One"
                                    else:
                                        return SyntaxErrorCode + "12 : Logrithmic Base Error - Cannot be Negative"
                                elif parse[truevariableLocation - 1] == "sqroot":
                                    if calcv >= 0:
                                        calcv = math.sqrt(calcv)
                                    else :
                                        return SyntaxErrorCode + "21 : Square Root Error - Square Root of Negative Number is Imaginary"
                                elif parse[truevariableLocation - 1] == "cuberoot":
                                    calcv = calcv ^ (1/3)
                                elif parse[truevariableLocation - 1].__contains__ == "root":
                                    a = parse[truevariableLocation - 1].rsplit("th")
                                    try:
                                        if int(a[0]) == float(a[0]):
                                            if float(float(a[0])/2.0) == int(float(a[0])/2.0):
                                                if calcv >= 0:
                                                    calcv = calcv ^ float(a[0])
                                                else:
                                                    return SyntaxErrorCode + "21 : Even Root Error - Even Root of Negative Number is Imaginary"
                                            else:
                                                calcv = float(a[0])
                                        else:
                                            calcv = calcv ^ float(a[0])
                                    except:
                                        return SyntaxErrorCode + "80 : Formation Error - Irregular Formation"
                                elif parse[truevariableLocation - 1] == "sin":
                                    if radians == "radians":
                                        if float(calcv/math.pi) == int(calcv/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.sin(calcv)
                                    elif radians == "gradians":
                                        rd = float(calcv * (math.pi / 200))
                                        if float(rd/math.pi) == int (rd/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.sin(rd)
                                    else:
                                        rd = float(math.radians(calcv))
                                        if float(rd/math.pi) == int(rd/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.sin(rd)
                                elif parse[truevariableLocation - 1] == "cos":
                                    if radians == "radians":
                                        if float((calcv * 2) / math.pi) == int((calcv * 2) / math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.cos(calcv)
                                    elif radians == "gradians":
                                        rd = (calcv * (math.pi / 200))
                                        if float((rd * 2) / math.pi) == int((rd * 2) / math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.cos(rd)
                                    else:
                                        rd = math.radians(calcv)
                                        if float((rd * 2) / math.pi) == int((rd * 2) / math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.cos(rd)
                                elif parse[truevariableLocation - 1] == "tan":
                                    if radians == "radians":
                                        if float(calcv/math.pi) == int(calcv/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.tan(calcv)
                                    elif radians == "gradians":
                                        rd = float(calcv * (math.pi / 200))
                                        if float(rd/math.pi) == int (rd/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.tan(rd)
                                    else:
                                        rd = float(math.radians(calcv))
                                        if float(rd/math.pi) == int(rd/math.pi):
                                            calcv = 0
                                        else:
                                            calcv = math.tan(rd)
                                elif parse[truevariableLocation - 1] == "asin":
                                    if radians == "radians":
                                        calcv = math.asin(calcv)
                                    elif radians == "gradians":
                                        calcv = math.asin((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.asin(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "acos":
                                    if radians == "radians":
                                        calcv = math.acos(calcv)
                                    elif radians == "gradians":
                                        calcv = math.acos((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.acos(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "atan":
                                    if radians == "radians":
                                        calcv = math.atan(calcv)
                                    elif radians == "gradians":
                                        calcv = math.atan((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.atan(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "sinh":
                                    if radians == "radians":
                                        calcv = math.sinh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.sinh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.sinh(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "cosh":
                                    if radians == "radians":
                                        calcv = math.cosh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.cosh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.cosh(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "tanh":
                                    if radians == "radians":
                                        calcv = math.tanh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.tanh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.tanh(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "asinh":
                                    if radians == "radians":
                                        calcv = math.asinh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.asinh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.asinh(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "acosh":
                                    if radians == "radians":
                                        calcv = math.acosh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.acosh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.acosh(math.radians(calcv))
                                elif parse[truevariableLocation - 1] == "atan":
                                    if radians == "radians":
                                        calcv = math.atanh(calcv)
                                    elif radians == "gradians":
                                        calcv = math.atanh((calcv * (math.pi / 200)))
                                    else:
                                        calcv = math.atanh(math.radians(calcv))
                                elif parse[truevariableLocation - 1].__contains__("e"):
                                    newparse.append(parse[truevariableLocation - 1])
                                    newparse.append("*")
                                elif parse[truevariableLocation - 1].__contains__("pi") or parse[truevariableLocation - 1].__contains__("π"):
                                    newparse.append(parse[truevariableLocation - 1])
                                    newparse.append("*")
                                elif parse[truevariableLocation - 1] == ")":
                                    newparse.append(")")
                                    newparse.append("*")
                                else:
                                    newparse.append(parse[truevariableLocation - 1])
                                
                                newparse.append(calcv)
                            except:
                                return SyntaxErrorCode + "99 : Formation Error"

                            if parse[index + 1] != "+" and parse[index + 1] != "-" and parse[index + 1] != "*" and parse[index + 1] != "/" and parse[index + 1] != "^" and parse[index + 1] != ")":
                                newparse.append("*")
                            else:
                                pass
                            if index + 1 < len(parse):
                                newparse = newparse + parse[index + 1:]
                            return parser(newparse)
                        else:
                            return calcv
                    else:
                        return SyntaxErrorCode + "0 : Wrong Parenthesis Error (use '(')"
            else:
                pass

    return SyntaxErrorCode + "1 : Missing Parenthesis Error (Suggested Missing Close Parenthesis (use ')'))"

def calc (operation):
    global BODMAS
    if len(operation) / 2 == int(len(operation)/2):
        return SyntaxErrorCode + " : Formation Error - Cannot Operate without Proper Operand or Operator"

    if len(operation) > 1:
        index = -1
        newoperation = []

        index = -1
        for a in operation:
            index += 1
            a = str(a)
            if a.__contains__("e") and a.rsplit("e")[1] == "":
                if a == "e":
                    operation[index] = math.e
                else:
                    if index > 0:
                        newoperation = operation[:index]
                    newoperation.append(a.rsplit("e")[0])
                    newoperation.append("*")
                    newoperation.append(math.e)
                    if index + 1 < len(operation):
                        newoperation = newoperation + operation[index + 1:] 
                    return calc(newoperation)
            elif a.__contains__("pi") or a.__contains__("π"):
                if a == "pi" or a == "π":
                    operation[index] = math.pi
                elif a.__contains__("π") and a.rsplit("π")[1] == "":
                    if index > 0:
                        newoperation = operation[:index]
                    newoperation.append(a.rsplit("π")[0])
                    newoperation.append("*")
                    newoperation.append(math.pi)
                    if index + 1 < len(operation):
                        newoperation = newoperation + operation[index + 1:] 
                    return calc(newoperation)
                elif a.__contains__("pi") and a.rsplit("pi")[1] == "":
                    if index > 0:
                        newoperation = operation[:index]
                    newoperation.append(a.rsplit("pi")[0])
                    newoperation.append("*")
                    newoperation.append(math.pi)
                    if index + 1 < len(operation):
                        newoperation = newoperation + operation[index + 1:] 
                    return calc(newoperation)
                    
        if BODMAS == False:
            index = -1
            newoperation = []
            for a in operation:
                Calc = "a"
                index += 1
                if a == "P":
                    try:
                        if float(operation[index - 1]) == int (operation[index - 1]) and float(operation[index - 1]) > 0 and float(operation[index + 1]) == int (operation[index + 1]) and float(operation[index + 1]) >= 0 and float(operation[index - 1]) >= float(operation[index + 1]):
                            Calc = math.factorial(float(operation[index - 1])) / math.factorial(float(operation[index - 1]) - float(operation[index + 1]))
                        else:
                            return SyntaxErrorCode + "50 : Permutaion Error - For Natural Numbers in n P m for n > 0, m >= 0 and n >= m"
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "C":
                    try:
                        if float(operation[index - 1]) == int (operation[index - 1]) and float(operation[index - 1]) > 0 and float(operation[index + 1]) == int (operation[index + 1]) and float(operation[index + 1]) >= 0 and float(operation[index - 1]) >= float(operation[index + 1]):
                            Calc = math.factorial(float(operation[index - 1])) / (math.factorial(float(operation[index - 1]) - float(operation[index + 1])) * math.factorial(float(operation[index + 1])))
                        else:
                            return SyntaxErrorCode + "50 : Combination Error - For Natural Numbers in n C m for n > 0, m >= 0 and n >= m"
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "^":
                    try:
                        Calc = float(operation[index - 1]) ^ float(operation[index + 1])
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "/":
                    try:
                        Calc = float(operation[index - 1]) / float(operation[index + 1])
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "*":
                    try:
                        Calc = float(operation[index - 1]) * float(operation[index + 1])
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "+":
                    try:
                        Calc = float(operation[index - 1]) + float(operation[index + 1])
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                elif a == "-":
                    try:
                        Calc = float(operation[index - 1]) - float(operation[index + 1])
                    except ZeroDivisionError:
                        return CannotDivideErrorCode
                    except :
                        return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                if Calc != "a":
                    if index - 2 > 0:
                        newoperation = operation[:index - 1]
                    newoperation.append(Calc)
                    if index + 2 < len(operation):
                        newoperation = newoperation + operation[index + 2:]
                    return calc(newoperation)
            return SyntaxErrorCode + "00 : Cannot Operate without Operator"
        else:
            if operation.__contains__("P"):
                index = -1
                for a in operation:
                    index += 1
                    if a == "P":
                        try:
                            if float(operation[index - 1]) == int (operation[index - 1]) and float(operation[index - 1]) > 0 and float(operation[index + 1]) == int (operation[index + 1]) and float(operation[index + 1]) >= 0 and float(operation[index - 1]) >= float(operation[index + 1]):
                                Calc = math.factorial(float(operation[index - 1])) / math.factorial(float(operation[index - 1]) - float(operation[index + 1]))
                            else:
                                return SyntaxErrorCode + "50 : Permutaion Error - For Natural Numbers in n P m for n > 0, m >= 0 and n >= m"
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except :
                            return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                        
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("C"):
                index = -1
                for a in operation:
                    index += 1
                    if a == "C":
                        try:
                            if float(operation[index - 1]) == int (operation[index - 1]) and float(operation[index - 1]) > 0 and float(operation[index + 1]) == int (operation[index + 1]) and float(operation[index + 1]) >= 0 and float(operation[index - 1]) >= float(operation[index + 1]):
                                Calc = math.factorial(float(operation[index - 1])) / (math.factorial(float(operation[index - 1]) - float(operation[index + 1])) * math.factorial(float(operation[index + 1])))
                            else:
                                return SyntaxErrorCode + "50 : Combination Error - For Natural Numbers in n C m for n > 0, m >= 0 and n >= m"
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except :
                            return SyntaxErrorCode + "99: Cannot Operate Unless an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("^"):
                index = -1
                for a in operation:
                    index += 1
                    if a == "^":
                        try:
                            Calc = float(operation[index - 1]) ^ float(operation[index + 1])            
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except:
                            return SyntaxErrorCode + "99 : Cannot Operate without an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("/"):
                index = -1
                for a in operation:
                    index += 1
                    if a == "/":
                        try:
                            Calc = float(operation[index - 1]) / float(operation[index + 1])            
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except:
                            return SyntaxErrorCode + "99 : Cannot Operate without an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("*"):
                index = -1
                for a in operation:
                    index += 1
                    if a == "*":
                        try:
                            Calc = float(operation[index - 1]) * float(operation[index + 1])            
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except:
                            return SyntaxErrorCode + "99 : Cannot Operate without an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("+"):
                index = -1
                for a in operation:    
                    index += 1
                    if a == "+":
                        try:
                            Calc = float(operation[index - 1]) + float(operation[index + 1])            
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except:
                            return SyntaxErrorCode + "99 : Cannot Operate without an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            elif operation.__contains__("-"):
                index = -1
                for a in operation:    
                    index +=1
                    if a == "-":
                        try:
                            Calc = float(operation[index - 1]) - float(operation[index + 1])            
                        except ZeroDivisionError:
                            return CannotDivideErrorCode
                        except:
                            return SyntaxErrorCode + "99 : Cannot Operate without an Number"
                        if index - 2 > 0:
                            newoperation = operation[:index - 1]
                        newoperation.append(Calc)
                        if index + 2 < len(operation):
                            newoperation = newoperation + operation[index + 2:]
                        return calc(newoperation)
            else:
                return SyntaxErrorCode + "00 : Cannot Operate without Operator"
    else:
        index = -1
        a = str(operation[0])
        if a == "pi" or a == "π":
            operation[0] = math.pi
        elif a == "e":
            operation[0] = math.e
        elif a.__contains__("e") and a.rsplit("e")[1] == "":
            operation[0] = float(a.rsplit("e")[0]) * math.e
        elif a.__contains__("pi") and a.rsplit("pi")[1] == "":
            operation[0] = float(a.rsplit("pi")[0]) * math.pi
        elif a.__contains__("π") and a.rsplit("π")[1] == "":
            operation[0] = float(a.rsplit("π")[0]) * math.pi
        return operation[0]

print(VSSVEBODMASCalc(input("Equation : "), True, "radians", True, " "))