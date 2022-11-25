# DFA
# - start with letter, underscore, dolar sign
# - after first letter bebas
# - dont use js keyword 
# - dont use 
function = ['false', 'true', 'break', 'default', 'for', 'return', 'var', 'const', 'delete', 'function', 'switch', 
            'while', 'case', 'else', 'if', 'throw', 'catch', 'let', 'try', 'continue', 'finally', 'null']
start_state = "Q0"
accept_states = ['Q1']
transition = {}

def generateFA(Src, Dst, transition):
    if (Src == 'Q0' and Dst == 'Q1'):
        for i in range(65,91): #A-Z
            transition[(Src, chr(i))] = Dst
        for j in range(97,123): #a-z
            transition[(Src, chr(j))] = Dst
        transition[(Src, '_')] = Dst
        transition[(Src, '$')] = Dst

    elif (Src == 'Q1' and Dst == 'Q1'):
        for i in range(65,91): #A-Z
            transition[(Src, chr(i))] = Dst
        for j in range(97,123): #a-z
            transition[(Src, chr(j))] = Dst
        for k in range(0,10): #1-9
            transition[(Src, str(k))] = Dst
        transition[(Src, '_')] = Dst
        transition[(Src, '$')] = Dst
    
    elif ((Src == 'Q0' or Src == 'Q1') and Dst == 'Q2'):
        for i in range(33,36): #!-$
            transition[(Src, chr(i))] = Dst
        for j in range(37,48): #%-/
            transition[(Src, chr(j))] = Dst
        for k in range(58,65): #%-/
            transition[(Src, chr(k))] = Dst
        for l in range(91,95): #[-^
            transition[(Src, chr(l))] = Dst
        transition[(Src, '`')] = Dst
        for m in range(123,127): #{-~
            transition[(Src, chr(m))] = Dst
        if (Src == 'Q0'):
            for n in range(0,10):
                transition[(Src, str(n))] = Dst
    elif (Src == 'Q2' and Dst == 'Q2'):
        for i in range(33,127):
            transition[(Src, chr(i))] = Dst


def cekVariable(variable):
    if variable not in function:
        current_state = start_state
        for char in variable:
            current_state = transition[(current_state, char)]
        
        if (current_state in accept_states):
            print("ACCEPTED")
        else:
            print("REJECTED")
    else:
        print("REJECTED")


# DEBUGING
def main():        
    generateFA('Q0', 'Q1', transition)
    generateFA('Q1', 'Q1', transition)
    generateFA('Q1', 'Q2', transition)
    generateFA('Q0', 'Q2', transition)
    generateFA('Q2', 'Q2', transition)

    cekVariable(input())


# DRIVER
if __name__ == "__main__":
    main()