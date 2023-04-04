import os

class GeradoraInteriorFachada:
    def __init__(self, oConstrutor):
        self.oConstrutor = oConstrutor
        self.sListaAtributosChave = ""
        self.sInteriorFachada = ""
        self.oTabela = None

    def geraAtributos(self):
        vAtributos = self.oConstrutor.vAtributos
        if len(vAtributos) > 0:
            self.sAtributosConstrutor = ""
            self.sListaAtributos = ""
            for sAtributo in vAtributos:
                sNomeAtributo = sAtributo[1:]
                self.sAtributosConstrutor += f"{sAtributo},"
                self.sListaAtributos += f"{sAtributo};\n"
            self.sAtributosConstrutor = self.sAtributosConstrutor[:-1]

    def geraCampos(self):
        vCampos = self.oConstrutor.vCampos
        vAtributos = self.oConstrutor.vAtributos
        if len(vCampos) > 0:
            vCamposReg, vValoresNaoChave, vComparacao, vAtributosChave, vCamposChave, vCamposNaoChave = [], [], [], [], [], []
            for nIndice, oCampo in enumerate(vCampos):
                if oCampo['pri'] == "pk":
                    sTeste = f"{vAtributos[nIndice]}"
                    vAtributosChave.append(sTeste)
                    vCamposChave.append(oCampo['column_name'])
                    vComparacao.append(f"{oCampo['column_name']} = {sTeste}")
                else:
                    vCamposNaoChave.append(oCampo['column_name'])
                    vValoresNaoChave.append(f"'{self.oConstrutor.sClasse}.get{vAtributos[nIndice][1:]}()'")
                vCamposReg.append(f"oReg->{oCampo['column_name']}")
            self.sListaAtributosChave = ",".join(vAtributosChave)
            self.sListaCamposChave = ",".join(vCamposChave)
            self.sListaCamposNaoChave = ",".join(vCamposNaoChave)
            self.sListaValoresNaoChave = ",".join(vValoresNaoChave)
            self.sComparacaoChaveAtributo = ",\n\t\t\t\t\t".join(vComparacao)
            self.sListaCamposReg = ",".join(vCamposReg)

    def gera(self):
        self.geraAtributos()
        self.geraCampos()
        sArquivo = ""
        with open(os.path.join(os.path.dirname(__file__), "../modelos/modelo_interior_fachada.txt"), 'r') as f:
            vModelo = f.readlines()
        sArquivo = "".join(vModelo)
        sArquivo = sArquivo.replace("#NOME_CLASSE#", self.oConstrutor.sClasse)
        #sArquivo = sArquivo.replace("#NOME_CLASSE_SIMPLES#", self.oConstrutor.sClasseSimples)
        sArquivo = sArquivo.replace("#NOME_TABELA#", self.oConstrutor.sTabela)
        sArquivo = sArquivo.replace("#LISTA_ATRIBUTOS_CHAVE#", self.sListaAtributosChave)
        sArquivo = sArquivo.replace("#LISTA_ATRIBUTOS_CONSTRUTOR#", self.sAtributosConstrutor)
        self.sInteriorFachada = sArquivo
