from luzes import Luzes
from matriz_transf import *

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

class MatrizResolver:
    def __init__(self, largura, altura):
        self.__dados = {}
        self.__largura = largura
        self.__altura = altura
    
    def __aprenderLuzes(self, luzes):
        ho = hash(luzes)        
        largura = self.largura
        altura = self.altura
        if (luzes.largura != largura) or (luzes.altura != altura):
            raise Exception('Tamanho incompatível')
        l = Luzes(largura, altura)
        for i in range(largura * altura):
            x = i % largura
            y = int(i / largura)
            l.matriz = luzes.matriz
            l.clicar((x,y))
            h = hash(l)
            if (h != 0) and (len(self.solucao(l)) == 0):
                self.__dados[h] = {
                    'm': [x,y],
                    'p' : ho,
                    'u' : True,
                }

    
    def solucao(self, luzes):
        l = Luzes(0, 0)        
        largura = self.largura
        altura = self.altura
        for _,i in inverter.items():                
            for _,g in girar.items():
                l.matriz = g['transf'](i['transf'](luzes.matriz))
                h = hash(l)
                if h in self.__dados:
                    rst = []
                    while h != 0:
                        d = self.__dados[h]
                        h = d['p']
                        x,y = d['m']
                        x,y = i['posica'](x, y, altura, largura)
                        x,y = g['posica'](x, y, altura, largura)                        
                        rst.append([x,y])
                    return rst
        return []        
    
    @property
    def altura(self):
        return self.__altura        
    
    @property
    def largura(self):
        return self.__largura
    
    @property
    def dados(self):
        return self.__dados
    @dados.setter
    def dados(self, dados):
        self.__dados = dados
    
    def aprender(self):        
        k = list(self.dados.keys())
        l = Luzes(self.largura, self.altura)
        if len(k) == 0:
            l.hashToMatriz(0)
            self.__aprenderLuzes(l)
        else:
            for h in k:
                if self.dados[h]['u']:
                    l.hashToMatriz(h)
                    self.__aprenderLuzes(l)
                    self.dados[h]['u'] = False