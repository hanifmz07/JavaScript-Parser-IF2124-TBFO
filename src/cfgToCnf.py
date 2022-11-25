import copy

def readGrammars(dir: str):
    # Mengembalikan dictionary berisi grammar hasil pembacaan file txt
    # Contoh : S -> A | BC maka di dictionary akan berbentuk {'S': [['A'], ['B', 'C']]}

    file = open(dir, "r")

    grammarsList = []
    for line in file:
        grammarsList.append(line.split())

    grammar_dict = {}
    for grammar in grammarsList:
        production = []
        for i in range(len(grammar)):
            if i == 0:
                key = grammar[i]
                grammar_dict[key] = []
            elif grammar[i] == '|':
                grammar_dict[key].append(production)
                production = []
            elif grammar[i] != '->':
                production.append(grammar[i])

        if production != []:
            grammar_dict[key].append(production)
    return grammar_dict

def displayGrammar(grammar_dict : dict):
    # Menampilan grammar

    for key, values in grammar_dict.items():
        print(key, " : ", values)

def removeUnitProduction(grammars : dict):
    # Mengembalikan grammar yang sudah tidak ada unit production
    # Tidak akan ada duplicate di tiap production

    tempGrammars = copy.deepcopy(grammars)
    nonTerminal = list(tempGrammars.keys())
    for key in nonTerminal:
        for item in nonTerminal:
            if [item] in tempGrammars[key]:
                tempGrammars[key].remove([item])
                for elmt in tempGrammars[item]:
                    if elmt not in tempGrammars[key]:
                        tempGrammars[key].append(elmt)
    return tempGrammars

def changeProduction(grammars : dict, search : list, change : list, lenMin : int):
    # grammars terdefinisi, tidak mungkin kosong
    # Mencari grammars yang memiliki production tertentu dan merubahnya
    # search adalah variable/terminal yang ingin diganti, contoh : ['B', 'C']
    # change adalah variable/terminal pengganti, contoh : ['X']
    # lenMin adalah panjang minimum dari production yang akan diganti
    # Contoh : changeProduction(S -> ABC, BC, X, 2) akan merubah grammars menjadi S -> AX

    nonTerminal = list(grammars.keys())
    for key in nonTerminal:
        for i in range(len(grammars[key])):
            if (len(grammars[key][i]) > lenMin):
                for j in range(len(grammars[key][i])+1):
                    for k in range(j+1, len(grammars[key][i])+1):
                        if grammars[key][i][j:k] == search:
                            grammars[key][i][j:k] = change

def removeLongVariable(grammars : dict):
    # Grammars terdefinisi, tidak mungkin kosong
    # Mengubah variable yang panjang (lebih dari 2) menjadi hanya terdiri dari 2 variable
    # Contoh: S -> ABC akan berubah menjadi S -> AV_0 dan V_0 -> BC

    # nonTerminal = list(grammars.keys())
    count = 0
    variable =  "V_"
    for key in list(grammars.keys()):
        for i in range(len(grammars[key])):
            production = copy.deepcopy(grammars[key][i])
            if len(production)>2:
                changeProduction(grammars, production[1:], [variable+str(count)], 2)
                grammars[variable+str(count)] = [production[1:]]
                count+=1
        # nonTerminal = list(grammars.keys())

def removeLongVariable1(grammars : dict):
    # Grammars terdefinisi, tidak mungkin kosong
    # Mengubah variable yang panjang (lebih dari 2) menjadi hanya terdiri dari 2 variable
    # Contoh: S -> ABC akan berubah menjadi S -> AV_0 dan V_0 -> BC

    # nonTerminal = 
    count = 0
    variable =  "V_"
    
    newGrammar  = copy.deepcopy(grammars)
    nonTerminal = list(newGrammar.keys())
    for key in nonTerminal:
        for i in range(len(newGrammar[key])):
            production = copy.deepcopy(newGrammar[key][i])
            if len(production)>2:
                changeProduction(newGrammar, production[1:], [variable+str(count)], 2)
                newGrammar[variable+str(count)] = [production[1:]]
                count+=1
        nonTerminal = list(newGrammar.keys())
    return newGrammar
        # nonTerminal = list(grammars.keys())

def removeLongVariable2(grammars : dict):
    # Grammars terdefinisi, tidak mungkin kosong
    # Mengubah variable yang panjang (lebih dari 2) menjadi hanya terdiri dari 2 variable
    # Contoh: S -> ABC akan berubah menjadi S -> AV_0 dan V_0 -> BC

    count = 0
    variable =  "W_"
    
    newGrammar  = copy.deepcopy(grammars)
    nonTerminal = list(newGrammar.keys())
    for key in nonTerminal:
        for i in range(len(newGrammar[key])):
            production = copy.deepcopy(newGrammar[key][i])
            if len(production)>2:
                
                changeProduction(newGrammar, production[1:], [variable+str(count)], 2)
                newGrammar[variable+str(count)] = [production[1:]]
                count+=1
        nonTerminal = list(newGrammar.keys())
        # print(count)
    return newGrammar

def removeLongVariable3(grammars : dict):
    # Grammars terdefinisi, tidak mungkin kosong
    # Mengubah variable yang panjang (lebih dari 2) menjadi hanya terdiri dari 2 variable
    # Contoh: S -> ABC akan berubah menjadi S -> AV_0 dan V_0 -> BC

    count = 0
    variable =  "Y_"
    
    newGrammar  = copy.deepcopy(grammars)
    nonTerminal = list(newGrammar.keys())
    for key in nonTerminal:
        for i in range(len(newGrammar[key])):
            production = copy.deepcopy(newGrammar[key][i])
            if len(production)>2:
                
                changeProduction(newGrammar, production[1:], [variable+str(count)], 2)
                newGrammar[variable+str(count)] = [production[1:]]
                count+=1
        nonTerminal = list(newGrammar.keys())
        # print(count)
    return newGrammar    

def removeLongVariable(grammars : dict):
    g1 = removeLongVariable1(grammars)
    g2 = removeLongVariable2(g1)
    g3 = removeLongVariable3(g2)
    return g3

def removeTerminalVariables(grammars):
    # Menghilangkan terminal yang tergabung dengan variables
    # Contoh: S -> Aa akan menjadi S -> AT_0 dan T_0 -> a

    count = 0
    variable =  "T_"
    nonTerminal = list(grammars.keys())
    for key in nonTerminal:
        for i in range(len(grammars[key])):
            # print(grammars[key][i])
            if len(grammars[key][i])>1:
                for j in range(len(grammars[key][i])):
                    if grammars[key][i][j] not in nonTerminal:
                        temp = [variable + str(count)]
                        grammars[variable + str(count)] = [[grammars[key][i][j]]]
                        changeProduction(grammars, [grammars[key][i][j]], temp, 1)
                        nonTerminal = list(grammars.keys())
                        count+=1



def cfgToCnfDebug(dir : str):
    # Fungsi untuk keperluan debug

    grammars = readGrammars(dir)
    print("Grammar mentah: ")
    displayGrammar(grammars)
    
    print("\nRemove unit prod: ")
    grammars = removeUnitProduction(grammars)
    displayGrammar(grammars)
    
    print("\nRemove terminal dan variables yang masih tergabung: ")
    removeTerminalVariables(grammars)
    displayGrammar(grammars)
    
    print("\nRemove production yang memiliki lebh dari 2 simbol: ")
    removeLongVariable(grammars)
    displayGrammar(grammars)
    print()

# cfgToCnfDebug("src/sample.txt")


def cfgToCnf(dir : str):
    # CFG to CNF
    grammars = readGrammars(dir)
    grammars = removeUnitProduction(grammars)
    removeTerminalVariables(grammars)
    grammars = removeLongVariable(grammars)
    return grammars