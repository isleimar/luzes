class LuzesMovimento:
    def __init__(self, id: int, nivel:int, m_x: int, m_y: int, anterior_id: int = None, ultimo: bool = True):
        self.__id: int = id
        self.__nivel = nivel
        self.__movimento = (m_x, m_y)
        self.__anterior_id: int = anterior_id
        self.__ultimo: bool = ultimo             
    
    @property
    def id(self)->int:
        return self.__id

    @property
    def nivel(self) -> int:
        return self.__nivel    
    
    @property
    def movimento(self):
        return self.__movimento
    @movimento.setter
    def movimento(self, movimento):
        self.__movimento = movimento
    
    @property
    def anterior_id(self):
        return self.__anterior_id
    
    @property
    def ultimo(self)->bool:
        return self.__ultimo
    @ultimo.setter
    def ultimo(self, ultimo):
        self.__ultimo = ultimo