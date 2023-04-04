from classes.CategoriaTipoTransacaoParent import CategoriaTipoTransacaoParent

class CategoriaTipoTransacao(CategoriaTipoTransacaoParent):
    def __init__(self, nId,sDescricao,dDtCadastro,bPublicado,bAtivo):
        self.setId(nId)
        self.setDescricao(sDescricao)
        self.setDtCadastro(dDtCadastro)
        self.setPublicado(bPublicado)
        self.setAtivo(bAtivo)
        