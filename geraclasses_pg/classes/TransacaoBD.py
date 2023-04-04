from classes.TransacaoBDParent import TransacaoBDParent

class TransacaoBD(TransacaoBDParent):
    def __init__(self, sBanco):
        self.pConexao = TransacaoBDParent(sBanco=sBanco)
