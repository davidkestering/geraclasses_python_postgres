class TransacaoParent:
    def __init__(self, nId,nIdTipoTransacao,nIdUsuario,sObjeto,sIp,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.nIdTipoTransacao = nIdTipoTransacao
        self.nIdUsuario = nIdUsuario
        self.sObjeto = sObjeto
        self.sIp = sIp
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.nId = nId

    def getIdTipoTransacao(self):
        return self.nIdTipoTransacao

    def setIdTipoTransacao(self, nIdTipoTransacao):
        self.nIdTipoTransacao = nIdTipoTransacao

    def getIdUsuario(self):
        return self.nIdUsuario

    def setIdUsuario(self, nIdUsuario):
        self.nIdUsuario = nIdUsuario

    def getObjeto(self):
        return self.sObjeto

    def setObjeto(self, sObjeto):
        self.sObjeto = sObjeto

    def getIp(self):
        return self.sIp

    def setIp(self, sIp):
        self.sIp = sIp

    def getDtCadastro(self):
        return self.dDtCadastro

    def setDtCadastro(self, dDtCadastro):
        self.dDtCadastro = dDtCadastro

    def getPublicado(self):
        return self.bPublicado

    def setPublicado(self, bPublicado):
        self.bPublicado = bPublicado

    def getAtivo(self):
        return self.bAtivo

    def setAtivo(self, bAtivo):
        self.bAtivo = bAtivo

    
