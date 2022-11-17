

def readGrammar(dir):
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

def displayGrammar(grammar_dict):
    for key, values in grammar_dict.items():
        print(key, " : ", values)

x = readGrammar('src/grammar.txt')

displayGrammar(x)
# print(x.values())