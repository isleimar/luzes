import json
from luzes import Luzes
from os.path import isfile
from random import randint
from luzes_movimento_repository import LuzesMovimentoRepository
from luzes_movimento import LuzesMovimento
from matriz_resolver import MatrizResolver
from matriz_solucao import MatrizSolucao
largura = 5
altura = 5
nome_arquivo = "luzes.db"
lr = LuzesMovimentoRepository(nome_arquivo)   

def aprender():    
    global largura, altura, lr
    rm: MatrizResolver = MatrizResolver(largura, altura, lr)
    for i in range(10):
        print("Nível: %d" % (i + 1))
        rm.aprender()

def resolver():
    global largura, altura, lr
    ms = MatrizSolucao(lr)
    l = Luzes(largura, altura)
    with open('desafios.json') as arq:
        dados = json.load(arq)
        for i, d in dados.items():
            print("Desafio {}.".format(i))
            l.matriz = d            
            solucao = ms.solucao(l)
            print(l)
            for s in solucao:
                l.clicar(s)
            if hash(l) != 0 :
                print("Falhou!!!")
                print(l)
            print(solucao)
            print("-"*50)

def main():    
    resolver()    

if __name__ == "__main__":
    main()

