import unittest
from matriz_transf import \
    girarMatriz90, girarMatriz180, girarMatriz270, \
    inverterMatrizHorizontal, inverterMatrizVertical

DADOS = {
    'girar em 90°':{
        0:{
            'entrada':[],
            'saida':[]
        },
        1:{
            'entrada':[[0]],
            'saida':[[0]]
        },
        2:{
            'entrada':[[0,1],[3,2]],
            'saida':[[3,0],[2,1]]
        },
        3:{
            'entrada':[[0,1,2],[3,4,5],[6,7,8]],
            'saida':[[6,3,0],[7,4,1],[8,5,2]]
        },
        4:{
            'entrada':[[0,1,2],[3,4,5]],
            'saida':[[3,0],[4,1],[5,2]]
        },
        5:{
            'entrada':[[0,1,2]],
            'saida':[[0],[1],[2]]
        },
    },
    'girar em 180°':{
        0:{
            'entrada':[],
            'saida':[]
        },
        1:{
            'entrada':[[0]],
            'saida':[[0]]
        },
        2:{
            'entrada':[[0,1],[3,2]],
            'saida':[[2,3],[1,0]]
        },
        3:{
            'entrada':[[0,1,2],[3,4,5],[6,7,8]],
            'saida':[[8,7,6],[5,4,3],[2,1,0]]
        },
        4:{
            'entrada':[[0,1,2],[3,4,5]],
            'saida':[[5,4,3],[2,1,0]]
        },
        5:{
            'entrada':[[0,1,2,3,4,5]],
            'saida':[[5,4,3,2,1,0]]
        },
    },
    'girar em 270°':{
        0:{
            'entrada':[],
            'saida':[]
        },
        1:{
            'entrada':[[0]],
            'saida':[[0]]
        },
        2:{
            'entrada':[[0,1],[3,2]],
            'saida':[[1,2],[0,3]]
        },
        3:{
            'entrada':[[0,1,2],[3,4,5],[6,7,8]],
            'saida':[[2,5,8],[1,4,7],[0,3,6]]
        },
        4:{
            'entrada':[[0,1,2],[3,4,5]],
            'saida':[[2,5],[1,4],[0,3]]
        },
        5:{
            'entrada':[[0,1,2,3,4,5]],
            'saida':[[5],[4],[3],[2],[1],[0]]
        },
    },
    'inverter horizontal':{
        0:{
            'entrada':[],
            'saida':[]
        },
        1:{
            'entrada':[[0]],
            'saida':[[0]]
        },
        2:{
            'entrada':[[0,1],[3,2]],
            'saida':[[3,2],[0,1]]
        },
        3:{
            'entrada':[[0,1,2],[3,4,5],[6,7,8]],
            'saida':[[6,7,8],[3,4,5],[0,1,2]]
        },
        4:{
            'entrada':[[0,1,2],[3,4,5]],
            'saida':[[3,4,5],[0,1,2]]
        },
        5:{
            'entrada':[[0,1,2,3,4,5]],
            'saida':[[0,1,2,3,4,5]]
        },
    },
    'inverter vertical':{
        0:{
            'entrada':[],
            'saida':[]
        },
        1:{
            'entrada':[[0]],
            'saida':[[0]]
        },
        2:{
            'entrada':[[0,1],[3,2]],
            'saida':[[1,0],[2,3]]
        },
        3:{
            'entrada':[[0,1,2],[3,4,5],[6,7,8]],
            'saida':[[2,1,0],[5,4,3],[8,7,6]]
        },
        4:{
            'entrada':[[0,1,2],[3,4,5]],
            'saida':[[2,1,0],[5,4,3]]
        },
        5:{
            'entrada':[[0,1,2,3,4,5]],
            'saida':[[5,4,3,2,1,0]]
        },
    },

}

class TesteMatrizTransf(unittest.TestCase):

    def __girar(self, nome, func):
        matrizes = DADOS[nome]
        for _,dados in matrizes.items():
            entrada = dados['entrada']
            saida = dados['saida']
            self.assertEqual(saida , func(entrada) , "Falha ao {}.".format(nome))        
        print("Teste {} OK!!".format(nome))
    
    def test_girar_90(self): 
        self.__girar('girar em 90°', girarMatriz90)
    
    def test_girar_180(self): 
        self.__girar('girar em 180°', girarMatriz180)
    
    def test_girar_270(self): 
        self.__girar('girar em 270°', girarMatriz270)
    
    def test_inverter_horizontal(self): 
        self.__girar('inverter horizontal', inverterMatrizHorizontal)
    
    def test_inverter_vertical(self): 
        self.__girar('inverter vertical', inverterMatrizVertical)        

if __name__ == "__main__":
    unittest.main()