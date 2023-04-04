from classes.UsuarioBDParent import UsuarioBDParent

class UsuarioBD(UsuarioBDParent):
    def __init__(self, sBanco):
        self.pConexao = UsuarioBDParent(sBanco=sBanco)