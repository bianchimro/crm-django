import sys
from libreria import helpers

def provafunzione(a, b=10, c=6):
    print(a)
    print(b)


provafunzione(10)
provafunzione(10, b=2)
provafunzione(10, b=2, c=10)
provafunzione(10, c=10)



def main(msg):
    print(msg)
    x = helpers.somma(1, 2)
    print(x)


if __name__ == '__main__':
    main(sys.argv[1])
