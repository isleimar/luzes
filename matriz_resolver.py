from luzes import Luzes
from luzes_movimento import LuzesMovimento
from luzes_movimento_repository import LuzesMovimentoRepository

class MatrizResolver:
    def __init__(self, largura, altura, luzRepos: LuzesMovimentoRepository):
        self.__luzRepos = luzRepos
        self.__largura = largura
        self.__altura = altura
    
    def __aprenderLuzes(self, luzesMovimento: LuzesMovimento):        
        largura = self.largura
        altura = self.altura
        id = luzesMovimento.id
        nivel = luzesMovimento.nivel
        l = Luzes(largura, altura)                
        for i in range(largura * altura):
            x = i % largura
            y = int(i / largura)
            l.hashToMatriz(id)
            l.clicar((x,y))
            h = hash(l)
            if (h != 0) and (not self.existSolucao(l)):
                lm = LuzesMovimento(h, nivel +1, x, y, id, True)
                self.__luzRepos.inserir(lm) 
       
    @property
    def altura(self):
        return self.__altura        
    
    @property
    def largura(self):
        return self.__largura    
    
    def aprender(self):                
        ultimos = self.__luzRepos.ultimos()
        l = Luzes(self.largura, self.altura)
        if len(ultimos) == 0:
            if not self.__luzRepos.existId(0):
                self.__luzRepos.inserir(LuzesMovimento(0, 0, 0, 0))            
        else:
            for lm in ultimos:
                self.__aprenderLuzes(lm)
                lm.ultimo = False
                self.__luzRepos.atualizar(lm)                
        self.__luzRepos.commit()