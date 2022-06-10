class Luzes():
    def __init__(self, largura, altura):
        self.__largura: int = largura
        self.__altura: int = altura
        self.__matriz = []
        self.__gerarMatriz()
        self.__mascara = [[0,-1],[-1,0],[0,0],[1,0],[0,1]]
        self.__historico = []
    
    def __str__(self):
        v = [' ', '@']
        s = ''
        for linha in self.__matriz:
            s = s + '|'
            for celula in linha:
                s = s + v[celula]
            s = s + '|\n'
        return s
    
    def __gerarMatriz(self):
        m = []
        for i in range(self.__altura):
            n = []
            for j in range(self.__largura):
                n.append(0)
            m.append(n)
        self.__matriz = m
    
    def __inverterPosicao(self, posicao):
        xo,yo = posicao
        for xm, ym in self.__mascara:
            x = xo + xm
            y = yo + ym
            if (x >= 0) and (y >= 0) and (x < self.__largura) and (y < self.__altura):                
                valor = self.__matriz[y][x]
                self.__matriz[y][x] = (valor + 1) % 2
    
    def __inserirHistorico(self, posicao):
        self.__historico.append(posicao)
        self.__inverterPosicao(posicao)
    
    def __desfazerHistorico(self):
        posicao = self.__historico.pop()
        self.__inverterPosicao(posicao)
    
    def __resolver(self, maximo, movimentos):        
        if self.concluiu:
            return True, movimentos
        if len(movimentos) >= maximo:
            return False, movimentos
        for x in range(self.__largura):
            for y in range(self.__altura):
                exist = [x,y] in movimentos
                if not exist:
                    movimento = [x,y]
                    movimentos.append(movimento)
                    self.__inverterPosicao(movimento)                    
                    concluiu, movimentos = self.__resolver(maximo, movimentos)
                    if concluiu:
                        return True, movimentos
                    self.__inverterPosicao(movimentos.pop())        
        return False, movimentos

    @property
    def largura(self)->int:
        return self.__largura
    @largura.setter
    def largura(self, largura: int):        
        self.__largura = 0 if largura < 0 else largura
        self.__gerarMatriz()
    
    @property
    def altura(self)->int:
        return self.__altura
    @altura.setter
    def altura(self, altura: int):
        self.__altura = 0 if altura < 0 else altura
        self.__gerarMatriz()
    
    @property
    def matriz(self):
        return self.__matriz
    @matriz.setter
    def matriz(self, matriz):
        self.__matriz = matriz
        self.__altura = len(matriz)
        self.__altura = len(matriz[0])
    
    @property
    def concluiu(self):
        for linha in self.__matriz:            
            for celula in linha:
                if not (celula == 0):
                    return False
        return True
    
    @property
    def tamHistorico(self):
        return len(self.__historico)
    
    def clicar(self, posicao):
        self.__inserirHistorico(posicao)
    
    def desfazer(self):
        self.__desfazerHistorico()

    def resolver(self):
        maximo = 0
        concluiu = False
        while not concluiu:
            maximo += 1
            print("Resolvendo em {:,} movimentos.".format(maximo))
            concluiu, movimentos = self.__resolver(maximo,[])
        print(concluiu)
        print(movimentos)
        
