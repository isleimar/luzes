def __inserirEmMatriz(matriz, posicao, valor):
    x,y = posicao
    for _ in range(len(matriz) -1, y):
        matriz.append([])
    for _ in range(len(matriz[y]) -1, x):
        matriz[y].append(None)
    matriz[y][x] = valor    

def __transformar(matriz, func):
    rst_mat = []
    qtd_lin = len(matriz)
    y = 0
    for linha in matriz:
        qtd_col = len(linha)        
        x = 0
        for valor in linha:
            xp, yp = func(x,y,qtd_lin, qtd_col)
            __inserirEmMatriz(rst_mat, (xp,yp), valor)            
            x += 1
        y += 1        
    return rst_mat

def girarPosicao90(x, y, qtd_lin, qtd_col):    
    rst_x = (qtd_lin -1) - y
    rst_y = x
    return rst_x, rst_y

def girarMatriz90(matriz):        
    return __transformar(matriz, girarPosicao90)

def girarPosicao180(x, y, qtd_lin, qtd_col):    
    rst_x = (qtd_col - 1) - x
    rst_y = (qtd_lin - 1) - y
    return rst_x, rst_y

def girarMatriz180(matriz):    
    return __transformar(matriz, girarPosicao180)

def girarPosicao270(x, y, qtd_lin, qtd_col):
    rst_x = y
    rst_y = (qtd_col - 1) - x
    return rst_x, rst_y

def girarMatriz270(matriz):    
    return __transformar(matriz, girarPosicao270)

def inverterPosicaoHorizontal(x, y, qtd_lin, qtd_col):
    rst_x = x
    rst_y = (qtd_lin - 1) - y
    return rst_x, rst_y

def inverterMatrizHorizontal(matriz):    
    return __transformar(matriz, inverterPosicaoHorizontal)

def inverterPosicaoVertical(x, y, qtd_lin, qtd_col):
    rst_x = (qtd_col - 1) - x
    rst_y = y    
    return rst_x, rst_y

def inverterMatrizVertical(matriz):    
    return __transformar(matriz, inverterPosicaoVertical)

