from luzes import Luzes
from matriz_transf import *
from luzes_movimento import LuzesMovimento
from luzes_movimento_repository import LuzesMovimentoRepository

girar = {
    0:{
        'transf' : (lambda x: x),
        'posica' : (lambda x, y, altura, largura: [x,y]),
    },
    1:{
        'transf' : girarMatriz90,
        'posica' : girarPosicao270,
    },
    2:{
        'transf' : girarMatriz180,
        'posica' : girarPosicao180,
    },
    3:{
        'transf' : girarMatriz270,
        'posica' : girarPosicao90,
    },    
}
inverter = {
    0:{
        'transf' : (lambda x: x),
        'posica' : (lambda x, y, altura, largura: [x,y]),
    },
    1:{
        'transf' : inverterMatrizHorizontal,
        'posica' : inverterPosicaoHorizontal,        
    },
    2:{
        'transf' : inverterMatrizVertical,
        'posica' : inverterPosicaoVertical,        
    },    
}

class MatrizSolucao:

    def __init__(self,  luzRepos: LuzesMovimentoRepository):
        self.__luzRepos = luzRepos
    
    def __encontrarSemelhante(self, luzes):
        largura = luzes.largura
        altura = luzes.altura
        l = Luzes(0, 0)
        for i, fi in inverter.items():                
            for g, fg in girar.items():
                l.matriz = fg['transf'](fi['transf'](luzes.matriz))                
                id = hash(l)
                lm = self.__luzRepos.buscar(id)
                if not (lm is None):                    
                    return [fg['posica'], fi['posica']], lm
        return None,None,None
    
    def solucao(self, luzes):
        largura = luzes.largura
        altura = luzes.altura
        l = Luzes(0, 0)
        fs,lm = self.__encontrarSemelhante(luzes)                   
        rst = []
        if not (lm is None):
            while not (lm is None):
                anterior_id = lm.anterior_id               
                if not anterior_id is None:
                    x,y = lm.movimento
                    for f in fs:
                        x,y = f(x, y, altura, largura)                    
                    rst.append((x,y))
                lm = self.__luzRepos.buscar(anterior_id)            
        return rst
    

    def existSolucao(self, luzes):
        return len(self.solucao(luzes)) > 0
