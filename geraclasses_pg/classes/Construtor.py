import re
from classes.Conexao import Conexao

class Construtor:
    def __init__(self, sNomeBanco, sNomeTabela):
        oConexao = Conexao("LOCAL")
        self.sNomeBanco = sNomeBanco
        self.sTabela = sNomeTabela
        self.vCampos = []
        self.vAtributos = []
        self.geraNomeClasse()
        self.nQtdCamposTabela = oConexao.carregaQtdCampos(sNomeBanco,sNomeTabela)
        if self.nQtdCamposTabela > 0:
            self.vCampos = oConexao.pegaCampos(sNomeBanco,sNomeTabela)
            self.geraAtributos()

    def geraNomeClasse(self):
        vNome = []
        sSeparador = None
        if re.search("-", self.sTabela):
            sSeparador = "-"
        elif re.search("_", self.sTabela):
            sSeparador = "_"
        if sSeparador:
            vNome = self.sTabela.split(sSeparador)
            vAuxiliar = []
            for i in range(len(vNome)):
                if len(vNome[i]) > 3 or len(vNome[i]) == 2:
                    vAuxiliar.append(vNome[i].lower().capitalize())
            self.sClasse = "".join(vAuxiliar)
            self.sArquivo = "_".join(vAuxiliar).lower()
        else:
            self.sClasse = self.sClasseSimples = self.sTabela.lower().capitalize()
            self.sArquivo = self.sTabela.lower()

    def geraAtributos(self):
        sPadraoNumerico = r"(int|integer|bigint|smallint|mediumint|real|double|float|numeric|decimal)"
        sPadraoData = r"(time|timestamp|date|datetime)"
        vCampos = self.vCampos
        for oCampo in vCampos:
            sNomeAtributo = ""
            bPassouEmPadrao = False
            if re.search(sPadraoNumerico, oCampo['data_type']):
                sNomeAtributo = "n" + str(oCampo['column_name']).lower().capitalize()
                bPassouEmPadrao = True
            if re.search(sPadraoData, oCampo['data_type']):
                sNomeAtributo = "d" + str(oCampo['column_name']).lower().capitalize()
                bPassouEmPadrao = True
            if oCampo['data_type'] == "tinyint" or oCampo['data_type'] == "smallint":
                sNomeAtributo = "b" + str(oCampo['column_name']).lower().capitalize()
                bPassouEmPadrao = True
            if not bPassouEmPadrao:
                sNomeAtributo = "s" + str(oCampo['column_name']).lower().capitalize()
            vNomeAtributo = re.split("-|_", sNomeAtributo)
            if len(vNomeAtributo) > 0:
                for i in range(1, len(vNomeAtributo)):
                    vNomeAtributo[i] = vNomeAtributo[i].capitalize()
                sNomeAtributo = "".join(vNomeAtributo)
            self.vAtributos.append(sNomeAtributo)
