from classes.GrupoUsuarioParent import GrupoUsuarioParent

class GrupoUsuario(GrupoUsuarioParent):
    def __init__(self, nId,sNmGrupoUsuario,dDtCadastro,bPublicado,bAtivo):
        self.setId(nId)
        self.setNmGrupoUsuario(sNmGrupoUsuario)
        self.setDtCadastro(dDtCadastro)
        self.setPublicado(bPublicado)
        self.setAtivo(bAtivo)
        