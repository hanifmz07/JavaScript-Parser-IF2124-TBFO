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

def changeProduction(grammars : dict, search : list, change : list):
    # grammars terdefinisi, tidak mungkin kosong
    # Merubah mencari gramamrs yang memiliki production tertentu dan merubahnya
    # Contoh : changeProduction(S -> ABC, ABC, XYZ) akan merubah grammars menjadi S -> XYZ
    nonTerminal = list(grammars.keys())
    for key in nonTerminal:
        for i in range(len(grammars[key])):
            if search == grammars[key][i]:
                grammars[key][i] = change

def removeLongVariable(grammars : dict):
    # Grammars terdefinisi, tidak mungkin kosong
    # Mengubah variable yang panjang (lebih dari 2) menjadi hanya terdiri dari 2 variabe
    # Contoh: S -> ABC akan berubah menjadi S -> AX_0 dan X_0 -> BC

    nonTerminal = list(grammars.keys())
    count = 0
    variable =  "X_"
    for key in nonTerminal:
        for i in range(len(grammars[key])):
            production = grammars[key][i]
            if len(production)>2:
                tempProd = [production[0]]
                tempProd.append(variable+str(count))
                changeProduction(grammars, production, tempProd)
                count+=1
                grammars[variable+str(count)] = [production[1:]]


# grammars = readGrammars('src/sample.txt')
# grammars = removeUnitProduction(grammars)
# displayGrammar(grammars)