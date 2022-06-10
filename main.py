from luzes import Luzes
from random import randint
largura = 5
altura = 5

l = Luzes(largura, altura)
matriz = [
    [0,1,1,1,0],
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]
l.matriz = matriz

def main():
    global l
    l.resolver()
    pass

if __name__ == "__main__":
    main()

