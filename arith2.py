import sys

def main():
    formula = ''.join(sys.argv[1:])
    print eval(formula)

main()