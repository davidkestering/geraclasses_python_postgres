class UsuarioParent:
    def __init__(self, nId,nIdGrupoUsuario,sNmUsuario,sLogin,sSenha,sEmail,bLogado,dDtCadastro,bPublicado,bAtivo):
        self.nId = nId
        self.nIdGrupoUsuario = nIdGrupoUsuario
        self.sNmUsuario = sNmUsuario
        self.sLogin = sLogin
        self.sSenha = sSenha
        self.sEmail = sEmail
        self.bLogado = bLogado
        self.dDtCadastro = dDtCadastro
        self.bPublicado = bPublicado
        self.bAtivo = bAtivo
        
    def getId(self):
        return self.nId

    def setId(self, nId):
        self.nId = nId

    def getIdGrupoUsuario(self):
        return self.nIdGrupoUsuario

    def setIdGrupoUsuario(self, nIdGrupoUsuario):
        self.nIdGrupoUsuario = nIdGrupoUsuario

    def getNmUsuario(self):
        return self.sNmUsuario

    def setNmUsuario(self, sNmUsuario):
        self.sNmUsuario = sNmUsuario

    def getLogin(self):
        return self.sLogin

    def setLogin(self, sLogin):
        self.sLogin = sLogin

    def getSenha(self):
        return self.sSenha

    def setSenha(self, sSenha):
        self.sSenha = sSenha

    def getEmail(self):
        return self.sEmail

    def setEmail(self, sEmail):
        self.sEmail = sEmail

    def getLogado(self):
        return self.bLogado

    def setLogado(self, bLogado):
        self.bLogado = bLogado

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

    
