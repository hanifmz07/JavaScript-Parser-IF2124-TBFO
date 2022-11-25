from cfgToCnf import *
from cyk import *
from preprocess import *
from FA import *
import sys

def main():
    rule = cfgToCnf('src/grammar.txt')
    displayGrammar(rule)
    nama_file = sys.argv[1]
    hasil, flag = preprocess(nama_file)
    print("Checking Syntax...\n")
    if not flag:
        print("Not Accepted")
    else:
        res = CYK(rule,hasil)
        # displayTable(table)
        if res:
            print("Accepted")
        else:
            print("Not accepted")
    # print(rule)
if __name__ == '__main__':
    main()    
