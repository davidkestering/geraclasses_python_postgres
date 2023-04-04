class PermissaoParent:
    def __init__(self, nIdTipoTransacao,nIdGrupoUsuario,dDtCadastro,bPublicado,bAtivo):
        self.nIdTipoTransacao = nIdTipoTransacao
        self.nIdGrupoUsuario = nIdGrupoUsuario
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getIdTipoTransacao(self):
        return self.nIdTipoTransacao

    def setIdTipoTransacao(self, nIdTipoTransacao):
        self.nIdTipoTransacao = nIdTipoTransacao

    def getIdGrupoUsuario(self):
        return self.nIdGrupoUsuario

    def setIdGrupoUsuario(self, nIdGrupoUsuario):
        self.nIdGrupoUsuario = nIdGrupoUsuario

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

    
