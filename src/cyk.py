
# Python implementation for the
# CYK Algorithm

# Rules of the grammar
R = {
     "S": [["A","B"], ["B", "C"]],
     "A": [["B","A"], ["a"]],
     "B": [["C","C"], ["b"]],
     "C": [["A","B"], ["a"]],
    }


def getNonTerminalsCYK(R, symbols): # Mengembalikan non terminal dari production berdasarkan rule
    result = []
    for nonTerminal in R:
        productions = R[nonTerminal]
        for production in productions:
            for symbol in symbols:
                if symbol == production and production not in result:   
                    result.append(nonTerminal)
    return result

def combinationNonTerminalsCYK(symbol1, symbol2):   # Mengkombinasikan antara symbol1 dan symbol2
    result = []
    for nonTerminal1 in symbol1:
        for nonTerminal2 in symbol2:
            temp = [nonTerminal1, nonTerminal2]
            result.append(temp)
    return result    

def union(symbol1, symbol2):   # Union antara symbol1 dan symbol2
    result = []
    for nonTerminal1 in symbol1:
        result.append(nonTerminal1)
    for nonTerminal2 in symbol2:
        if nonTerminal2 not in result:
            result.append(nonTerminal2)
    return result

def getMax(table):
    max = 0
    for cols in table:
        for elmt in cols:
            if len(elmt) > max:
                max = len(elmt)
    return max 

def displayTable(table):    # Menampilkan table dari CYK
    spacing = getMax(table)
    for cols in table:
        for elmt in cols:
            for symbol in elmt:
                print(symbol, end ='')
            print("  ", end ='')
            if len(elmt) < spacing:
                print((spacing-len(elmt))*" ", end ='')
        print()    

def CYK(rule : dict, input : list):
    n = len(input)
    table = [[[] for i in range(j+1)] for j in range(n)]

    for i in range(n):
        for j in range(n-i):
            hasil = []
            if i == 0:
                table[n-i-1][j] = getNonTerminalsCYK(rule, [[input[j]]])
            else:
                for k in range(i):
                    temp = combinationNonTerminalsCYK(table[n-k-1][j], table[n-i+k][j+k+1])                    
                    # print(temp)
                    temp = getNonTerminalsCYK(rule, temp)
                    # print(temp)
                    hasil = union(hasil, temp)
                
                table[n-i-1][j] = hasil

    # for row in table:
    #     print(row)
    if 'S' in table[0][0]:
        return True
    else :
        return False

# print(CYK(R, ['a','b','a','b','a']))
