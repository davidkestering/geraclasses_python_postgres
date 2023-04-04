import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extensions import AsIs

class Conexao:
    def __init__(self, sServidor='BANCO'):
        self.pConexao = None
        self.pConsulta = None
        self.pBanco = None
        self.sErro = None
        self.sSqlError = None
        self.nQtdTabelas = None
        self.nQtdCampos = None
        self.sServidor = sServidor
        self.setServidor(sServidor)
        if sServidor == 'LOCAL':
            self.conectaBD('localhost', 'tunisia', 'fb123', 'tunisia')
        elif sServidor == 'BANCO':
            self.conectaBD('localhost', 'tunisia', 'fb123', 'tunisia')
        else:
            raise Exception(f'Não foi possível conectar ao servidor: {sServidor}')

    def setServidor(self, sServidor):
        self.sServidor = sServidor

    def getServidor(self):
        return self.sServidor

    def conectaBD(self, sHost, sUser, sSenha, sBanco):
        self.pConexao = psycopg2.connect(f"host='{sHost}' user='{sUser}' password='{sSenha}' dbname='{sBanco}'")

    def execute(self, sSql):
        self.pConsulta = self.pConexao.cursor(cursor_factory=DictCursor)
        try:
            self.pConsulta.execute(sSql)
            #self.pConsulta.commit()
        except psycopg2.Error as e:
            self.sSqlError = str(e)
            self.sErro = f'Ocorreu o seguinte erro na consulta: {self.sSqlError} <br> Query: {sSql}'
            self.insereErroSql(sSql)
            return self.getErro()

    def insereErroSql(self, sSql):
        try:
            with self.pConexao.cursor(cursor_factory=DictCursor) as cursor:
                sSqlErroExecucao = f"INSERT INTO seg_erros_sql (erro,ip,publicado) VALUES ('{self.escapeString(self.getErro())}','{IP_SERVIDOR}',1)"
                cursor.execute(sSqlErroExecucao)
                self.pConexao.commit()
        except psycopg2.Error as e:
            self.sSqlError = str(e)
            self.sErro = f'Ocorreu o seguinte erro na inserção do erro na tabela seg_erros_sql: {self.sSqlError} <br> Query: {sSqlErroExecucao}'

    def recordCount(self):
        if self.pConsulta.description is not None:
            return self.pConsulta.rowcount()

    def fetchObject(self):
        if self.pConsulta.description is not None:
            return self.pConsulta.fetchone()

    def close(self):
        self.pConexao.close()

    def getErroSql(self):
        return self.sSqlError

    def setConexao(self,sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return self.pConexao

    def getConsulta(self):
        return self.pConsulta

    def getErro(self):
        return self.sErro

    def escapeString(self, sAtributo):
        return psycopg2.extensions.escape_string(sAtributo)

    def unescapeString(self, sEscapedString):
        return bytes(str(sEscapedString), 'utf-8').decode('unicode_escape')


    def getLastId(self):
        return self.pConsulta.lastrowid

    def setQtdTabelas(self,nQtdTabelas):
        self.nQtdTabelas = nQtdTabelas

    def getQtdTabelas(self):
        return self.nQtdTabelas

    def setQtdCampos(self,nQtdCampos):
        self.nQtdCampos = nQtdCampos

    def getQtdCampos(self):
        return self.nQtdCampos

    def carregaQtdTabelas(self):
        self.pConsulta = self.pConexao.cursor(cursor_factory=DictCursor)
        sSql = f"SELECT count(*) as qtd FROM information_schema.tables A where A.TABLE_SCHEMA = 'public' "
        self.pConsulta.execute(sSql)
        oReg = self.pConsulta.fetchone()
        if oReg:
            self.setQtdTabelas(oReg["qtd"])
        return self.getQtdTabelas()

    def pegaTabelas(self):
        self.pConsulta = self.pConexao.cursor(cursor_factory=DictCursor)
        sSql = "SELECT * FROM INFORMATION_SCHEMA.TABLES A where A.table_schema='public' ORDER BY TABLE_NAME"
        self.pConsulta.execute(sSql)
        voObjeto = []
        while True:
            oReg = self.pConsulta.fetchone()
            if not oReg:
                break
            voObjeto.append(oReg["table_name"])
            del oReg
        return voObjeto

    def carregaQtdCampos(self,sNomeBanco,sNomeTabela):
        self.pConsulta = self.pConexao.cursor(cursor_factory=DictCursor)
        sSql = f"select count(COLUMN_NAME) as qtd from information_schema.columns where TABLE_CATALOG = '{sNomeBanco}' and table_name = '{sNomeTabela}'"
        self.pConsulta.execute(sSql)
        oReg = self.pConsulta.fetchone()
        if oReg:
            self.setQtdTabelas(oReg["qtd"])
        return self.getQtdTabelas()

    def pegaCampos(self,sNomeBanco, sNomeTabela):
        pConsulta = self.pConexao.cursor(cursor_factory=DictCursor)
        sSql = f"""select T.TABLE_CATALOG, T.TABLE_SCHEMA, T.TABLE_NAME, C.COLUMN_NAME, C.DATA_TYPE, substring(substring(CCU.CONSTRAINT_NAME,length(ccu.constraint_name)-3,length(ccu.constraint_name)),1,2) as PRI from INFORMATION_SCHEMA.TABLES T
                    join INFORMATION_SCHEMA.COLUMNS C
                        on C.TABLE_CATALOG = T.TABLE_CATALOG
                        and C.TABLE_NAME = T.TABLE_NAME
                        and C.TABLE_SCHEMA = T.TABLE_SCHEMA
                    left join INFORMATION_SCHEMA.CONSTRAINT_COLUMN_USAGE CCU
                        on CCU.TABLE_CATALOG = C.TABLE_CATALOG
                        and CCU.TABLE_NAME = C.TABLE_NAME
                        and CCU.TABLE_SCHEMA = C.TABLE_SCHEMA
                        and CCU.COLUMN_NAME = C.COLUMN_NAME
                        and substring(CCU.CONSTRAINT_NAME,length(ccu.constraint_name)-3,length(ccu.constraint_name)) = 'pkey'
                    where T.TABLE_CATALOG = '{sNomeBanco}' and T.TABLE_NAME = '{sNomeTabela}' order by C.ORDINAL_POSITION"""
        self.pConsulta.execute(sSql)
        rows = self.pConsulta.fetchall()
        cols = [desc[0] for desc in self.pConsulta.description]
        voObjeto = []
        for row in rows:
            d = {}
            for i in range(len(cols)):
                d[cols[i]] = row[i]
            voObjeto.append(d)
        return voObjeto


