from classes.CategoriaTipoTransacaoBDParent import CategoriaTipoTransacaoBDParent

class CategoriaTipoTransacaoBD(CategoriaTipoTransacaoBDParent):
    def __init__(self, sBanco):
        self.pConexao = CategoriaTipoTransacaoBDParent(sBanco=sBanco)
