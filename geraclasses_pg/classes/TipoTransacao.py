from classes.TipoTransacaoParent import TipoTransacaoParent

class TipoTransacao(TipoTransacaoParent):
    def __init__(self, nId,nIdCategoriaTipoTransacao,sTransacao,dDtCadastro,bPublicado,bAtivo):
        self.setId(nId)
        self.setIdCategoriaTipoTransacao(nIdCategoriaTipoTransacao)
        self.setTransacao(sTransacao)
        self.setDtCadastro(dDtCadastro)
        self.setPublicado(bPublicado)
        self.setAtivo(bAtivo)
        