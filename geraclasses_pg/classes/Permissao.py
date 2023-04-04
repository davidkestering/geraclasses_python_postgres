from classes.PermissaoParent import PermissaoParent

class Permissao(PermissaoParent):
    def __init__(self, nIdTipoTransacao,nIdGrupoUsuario,dDtCadastro,bPublicado,bAtivo):
        self.setIdTipoTransacao(nIdTipoTransacao)
        self.setIdGrupoUsuario(nIdGrupoUsuario)
        self.setDtCadastro(dDtCadastro)
        self.setPublicado(bPublicado)
        self.setAtivo(bAtivo)
        