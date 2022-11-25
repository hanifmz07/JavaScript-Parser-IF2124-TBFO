from FA import *

jsSymbol = ['break','default','for','return','var','const','delete','function','switch','case','while',
            'if', 'else','throw','catch','let','try','continue','finally','null']
bracket = ['[',']','(',')','{','}']
arithOp = ['+', '-', '*', '/', '%','//','**']
assignmentOp = ['=','+=','-=','*=','/=','%=','**=', '<<=','>>=','>>>=', '&=', '|=','^=','&&=', '||=', '??=']
bitwiseOp = ['&','|','^','~','<<','>>','>>>']
compareOp = ['<=', '>=', '==', '!=','>','<','===','!==']
logicalOp = ['&&','||','!','??']
incDec = ['--', '++']
other = ['.',',',';',':','?']
boolean = ['true', 'false']

def removeComment(dir : str):
    # Masukkan string berupa directory file
    # Keluaran string panjang tanpa comment dan newline
    lines = open(dir,'r')
    newStr = ""
    acc = True
    lineComment = False
    for line in lines:
        for i in range(0, len(line)):
            char = line[i]
            if i == 0:          # Remove line comment
                if i < len(line)-1:
                    if char+line[i+1] == "//":
                        acc = False
                        lineComment = True
                    elif char+line[i+1] == "/*":
                        acc = False
                    elif char+line[i+1] == "*/":
                        acc = True

                    if acc and char+line[i+1] != "//" and char+line[i+1] != "/*":
                        newStr+=char

            elif i == len(line) - 1 : 
                if char != '\n':
                    if char+line[i-1] == "//":
                        acc = False 
                        lineComment = True          
                    elif line[i-1]+char == "*/":
                        acc = True 
                    elif line[i-1]+char == "/*":
                        acc = False

                    if acc and line[i-1]+char != "//" and line[i-1]+char != "/*" and line[i-1]+char != "*/":
                        newStr+=char                
                            
            else :
                if char+line[i+1] == "//" or char+line[i-1] == "//":        
                    acc = False
                    lineComment = True
                elif char+line[i+1] == "/*" or line[i-1]+char == "/*":
                    acc = False
                elif char+line[i+1] == "*/" or line[i-1]+char == "*/":
                    acc = True

                if acc and char+line[i+1] != "//" and char+line[i-1] != "//" and char+line[i+1] != "/*" and line[i-1]+char != "/*" and char+line[i+1] != "*/" and line[i-1]+char != "*/":
                    newStr+=char                  
        if lineComment:
            acc = True
            lineComment = False
        newStr+='\n'
    return newStr 

def separate(str1 : str, listPemisah : list):
    op1 = []
    op2 = []
    for elmt in listPemisah:
        if len(elmt) == 1:
            op1.append(elmt)
        elif len(elmt) == 2:
            op2.append(elmt)

    newStr = ''
    for i in range(len(str1)):
        for pemisah in op1:
            char = str1[i]
            if len(pemisah) == 1 and i != 0:
                if char == pemisah and str1[i-1]+char not in op2:
                    if str1[i-1] in '1234567890' and pemisah == '.':
                        newStr += ''
                    else: 
                        newStr += ' '

                if i != 0:
                    if str1[i-1] == pemisah and str1[i-1]+char not in op2:
                        if char in '1234567890' and pemisah == '.':
                            newStr += ''
                        else: 
                            newStr += ' '
        newStr += char
    return newStr

def checkVarName(input):
    # Jika return 0 maka ada kemungkinan merupakan terminal lain   
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    if input[0] not in alphabets:
        return 0
    else :
        return ['__varname__']
    
def checkStr(input):
    # Jika return 0 maka ada kemungkinan merupakan terminal lain 
    if (input[0] == '\''  and input[-1] == '\'') or (input[0] == '\"' and input[-1] == '\"'):
        return ['__str__']        
    else :
        return 0

def checkNum(input):
    # Jika return -1 maka pasti syntax error
    numbers = '-0123456789.n'
    for char in input:
        if char not in numbers:
            return -1

    if '.' in input and 'n' not in input:
        if input.count('.') > 1 :
            return -1

        if input[0] == '.':
            return ['.', '__num__']
        elif input[-1] == '.':
            return ['__num__', '.']
        else:
            return ['__num__', '.','__num__']

    elif 'n' in input and '.' not in input:
        if input.count('n') > 1 :
            return -1
        
        if input[-1] == 'n':
            return ['__bigint__']
        else :
            return -1
    elif 'n' not in input and '.' not in input:
        return ['__num__']
    else :
        return -1

def subtituteSymbol(lst1 : list, allSymbol : list):
    flag = True
    for i in range(len(lst1)):
        if lst1[i] == '**' or lst1[i] ==  '<<' or lst1[i] == '>>' or lst1[i] =='>>>' \
        or lst1[i] =='&&'or lst1[i] =='||' or lst1[i] =='??' or lst1[i] =='+' \
        or lst1[i] =='-' or lst1[i] =='/' or lst1[i] =='*' or lst1[i] =='%' \
        or lst1[i] =='&' or lst1[i] =='|' or lst1[i] =='^':
            lst1[i] = '__op__'
        elif lst1[i] =='!' or lst1[i] =='~':
            lst1[i] = '__unop__'
        elif lst1[i] =='+' or lst1[i] =='-':
            lst1[i] = '__opunop__'
        elif lst1[i] == '==' or lst1[i] == '===' or lst1[i] == '!=' or lst1[i] == '!==' \
        or lst1[i] == '>=' or lst1[i] == '<=' or lst1[i] == '<' or lst1[i] == '>':
            lst1[i] = '__comp__'
        elif lst1[i] == '--' or lst1[i] == '++':
            lst1[i] = '__incdec__'
        elif lst1[i] == '=' or lst1[i] == '+=' or lst1[i] == '-=' or lst1[i] == '*=' \
        or lst1[i] == '**=' or lst1[i] == '/=' or lst1[i] == '<<=' or lst1[i] == '>>=' \
        or lst1[i] == '>>>=' or lst1[i] == '^=' or lst1[i] == '&=' or lst1[i] == '|=' \
        or lst1[i] == '&&=' or lst1[i] == '||=' or lst1[i] == '??=':
            lst1[i] = '__assign__'

        elif lst1[i] not in allSymbol:
            # print(lst1[i], end = " ")
            generateFA('Q0', 'Q1', transition)
            generateFA('Q1', 'Q1', transition)
            generateFA('Q1', 'Q2', transition)
            generateFA('Q0', 'Q2', transition)
            generateFA('Q2', 'Q2', transition)

            # print(cekVariable(input()))
            subtitute = cekVariable(lst1[i])
            if isinstance(subtitute, int):
                subtitute = checkStr(lst1[i])
            if isinstance(subtitute, int):
                subtitute = checkNum(lst1[i])
            if isinstance(subtitute, int):
                flag = False
                break
            # print(subtitute, end = " \n")
            else:
                lst1[i:i+1] = subtitute
    return lst1, flag

def printSource(input : str):
    print("\n\n========================= Source Code =========================")
    print(input)
    print("========================= End Of Line =========================\n")

def checkConBreak(res : str):
    inLoop = False
    inSwitch = False
    loopCount = 0
    switchCount = 0
    flag = True
    for i in range(len(res)):
        if res[i] == 'for' or res[i] == 'while' or res[i] == 'switch':
            if res[i] == 'switch':
                inSwitch = True
            else:
                inLoop = True

        elif (res[i] =='{' or res[i] =='}') and (inLoop or inSwitch):
            if inLoop:
                if res[i] =='{':
                    loopCount+=1
                else:
                    loopCount-=1
                if loopCount==0:
                    inLoop = False
            else:
                if res[i] =='{':
                    switchCount+=1
                else:
                    switchCount-=1
                if switchCount==0:
                    inSwitch = False                
        elif res[i] == 'break' or res[i] == 'continue':
            flag = inLoop or inSwitch
    return flag


listPemisah = bracket + arithOp + assignmentOp + bitwiseOp + compareOp + logicalOp + incDec + other
allSymbol = jsSymbol +  listPemisah + boolean
def preprocess(dir : str):
    # Input string berisi directory file javascript yang akan dicek
    # Output list of tokenize grammar dan flag
    # List of tokenize grammar akan dimasukan ke cyk untuk ngecek valid atau engga
    # flag untuk menandakan apakah ada syntax error ketika tokenize atau tidak
    # Jika flag == true maka berhasil dibuat list of tokenize dari input file javascript
    # Jika flag == false maka tidak berhasil karena ada syntax yang pasti error (Langsung not accepted)

    strNoComment = removeComment(dir)
    printSource(strNoComment)
    strPisah = separate(strNoComment,listPemisah) 
    listPisah = strPisah.split()   
    listSubtitute, flag = subtituteSymbol(listPisah, allSymbol)
    if flag:
        flag = checkConBreak(listSubtitute)

    return listSubtitute, flag


# res, flag = preprocess('test/test.js') 
# print(res)
# print(flag)






# print(checkConBreak(res))    
