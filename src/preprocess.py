
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
                if char != '\n':
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
    return newStr
    
print(removeComment('test/test.js'), end='')