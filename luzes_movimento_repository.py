import sqlite3
from luzes_movimento import LuzesMovimento

class LuzesMovimentoRepository:

    def __init__(self, database: str):
        self.__database = database
        self.__conn = sqlite3.connect(database)
        self.__cursor = self.__conn.cursor()
        self.__nomeTable = 'movimentos'
        if not self.__tabelaExiste():
            self.__criarTabela()

    def __tabelaExiste(self):
        sql = """SELECT name FROM sqlite_master WHERE type='table'
        AND name='{}';""".format(self.__nomeTable)
        lista = self.__cursor.execute(sql).fetchall()
        return len(lista) == 1
    
    def __criarTabela(self):
        sql = """CREATE TABLE {} (
            id INTEGER PRIMARY KEY NOT NULL,
            nivel INTEGER NOT NULL,
            m_x INTEGER NOT NULL,
            m_y INTEGER NOT NULL,
            anterior_id INTEGER DEFAULT NULL,
            ultimo BOOLEAN DEFAULT TRUE NOT NULL
            ); """.format(self.__nomeTable)
        self.__cursor.execute(sql)
    
    def __linhasLuzMov(self, linhas):        
        if linhas is None:
            return []
        # rst = []
        # for o in linhas:            
        #     rst.append(LuzesMovimento(
        #         id = o[0],
        #         nivel = o[1], 
        #         m_x = o[2], 
        #         m_y = o[3], 
        #         anterior_id = o[4], 
        #         ultimo = o[5]))
        # return rst
        return [LuzesMovimento(
             id, nivel, m_x, m_y, anterior_id, ultimo ) 
             for id, nivel, m_x, m_y, anterior_id, ultimo
             in linhas]        

    
    def existId(self, id: int):
        sql = """SELECT * FROM {} WHERE id = ? LIMIT 1;""".format(self.__nomeTable)
        lista = self.__cursor.execute(sql,[id]).fetchall()
        return len(lista) > 0
    
    def inserir(self, luzes_movimento: LuzesMovimento):
        sql = """INSERT INTO {}
        (id, nivel, m_x, m_y, anterior_id, ultimo)
        VALUES(?,?,?,?,?,?)""".format(self.__nomeTable)
        self.__cursor.execute(sql,[
            luzes_movimento.id,
            luzes_movimento.nivel,
            luzes_movimento.movimento[0],
            luzes_movimento.movimento[1],
            luzes_movimento.anterior_id,
            luzes_movimento.ultimo
        ])

    def buscar(self, id):
        sql = """SELECT * FROM {}
        WHERE id = ? LIMIT 1;""".format(self.__nomeTable)
        self.__cursor.execute(sql, [id])
        linhas = self.__linhasLuzMov(self.__cursor.fetchall())
        return linhas[0] if len(linhas) > 0 else None
    
    def ultimos(self):
        sql = """SELECT * FROM {}
        WHERE ultimo = ? """.format(self.__nomeTable)
        self.__cursor.execute(sql,[True])
        return self.__linhasLuzMov(self.__cursor.fetchall())
    
    def atualizar(self, luzes_movimento: LuzesMovimento):
        sql = """UPDATE {} SET 
            nivel = ?,
            m_x = ?,
            m_y = ?,
            anterior_id = ?,
            ultimo = ?
        WHERE id = ?""".format(self.__nomeTable)
        self.__cursor.execute(sql,[
            luzes_movimento.nivel,
            luzes_movimento.movimento[0],
            luzes_movimento.movimento[1],
            luzes_movimento.anterior_id,
            luzes_movimento.ultimo,
            luzes_movimento.id
        ])
    
    def paginar(self, quant, pagina, ultimos = False):
        sql = """SELECT * FROM {} 
        LIMIT {}, OFFSET {};""".format(
            self.__nomeTable,
            quant,
            pagina * quant
            )
        return self.__cursor.execute(sql)
    
    def commit(self):
        self.__conn.commit()

    