from classes.UsuarioParent import UsuarioParent

class Usuario(UsuarioParent):
    def __init__(self, nId, nIdGrupoUsuario, sNmUsuario, sLogin, sSenha, sEmail, bLogado, dDtCadastro, bPublicado, bAtivo):
        #super().__init__()
        self.setId(nId)
        self.setIdGrupoUsuario(nIdGrupoUsuario)
        self.setNmUsuario(sNmUsuario)
        self.setLogin(sLogin)
        self.setSenha(sSenha)
        self.setEmail(sEmail)
        self.setLogado(bLogado)
        self.setDtCadastro(dDtCadastro)
        self.setPublicado(bPublicado)
        self.setAtivo(bAtivo)


