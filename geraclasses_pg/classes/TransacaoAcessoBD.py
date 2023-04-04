from classes.TransacaoAcessoBDParent import TransacaoAcessoBDParent

class TransacaoAcessoBD(TransacaoAcessoBDParent):
    def __init__(self, sBanco):
        self.pConexao = TransacaoAcessoBDParent(sBanco=sBanco)
