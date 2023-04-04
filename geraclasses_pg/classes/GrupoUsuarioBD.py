from classes.GrupoUsuarioBDParent import GrupoUsuarioBDParent

class GrupoUsuarioBD(GrupoUsuarioBDParent):
    def __init__(self, sBanco):
        self.pConexao = GrupoUsuarioBDParent(sBanco=sBanco)
