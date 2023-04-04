import os
import re

class GeradoraBD:
    def __init__(self, oConstrutor):
        self.oConstrutor = oConstrutor
        self.sNomeArquivo = self.oConstrutor.sClasse + "BD.py"
        self.sNomeArquivoParent = self.oConstrutor.sClasse + "BDParent.py"
        self.sAtributosConstrutor = ""
        self.sListaAtributos = ""
        self.sListaAtributosChave = ""
        self.sListaCamposReg = ""
        self.sListaCamposChave = ""
        self.sListaCamposNaoChave = ""
        self.sListaValoresNaoChave = ""
        self.sComparacaoChaveAtributo = ""
        self.sComparacaoChaveAtributoEsp = ""
        self.sConteudoClasse = ""
        self.sAtribuicaoNaoChave = ""
        self.oTabela = None

    def geraAtributos(self):
        vAtributos = self.oConstrutor.vAtributos
        if len(vAtributos) > 0:
            for sAtributo in vAtributos:
                sNomeAtributo = sAtributo[1:]
                self.sAtributosConstrutor += sAtributo + ","
                self.sListaAtributos += sAtributo + ";\n"
            self.sAtributosConstrutor = self.sAtributosConstrutor[:-1]

    def geraCampos(self):
        vCampos = self.oConstrutor.vCampos
        vAtributos = self.oConstrutor.vAtributos
        if len(vCampos) > 0:
            vAtribuicaoNaoChave = []
            vCamposReg = []
            vValoresNaoChave = []
            vComparacao = []
            vComparacaoEsp = []
            vAtributosChave = []
            vCamposChave = []
            vCamposNaoChave = []
            chaveA = "{"
            chaveF = "}"
            for nIndice, oCampo in enumerate(vCampos):
                if oCampo['pri'] == "pk":
                    sTeste = f"{vAtributos[nIndice]}"
                    sTeste2 = vAtributos[nIndice]
                    sTeste3 = "{"+f"{sTeste}"+"}"
                    vAtributosChave.append(sTeste)
                    vCamposChave.append(oCampo['column_name'])
                    vComparacao.append(f"{oCampo['column_name']} = '{sTeste3}'")
                    vComparacaoEsp.append(
                        f"{oCampo['column_name']} = '{chaveA}o{self.oConstrutor.sClasse}.get{sTeste2[1:]}(){chaveF}'")
                else:
                    vCamposNaoChave.append(oCampo['column_name'])
                    if vAtributos[nIndice][:1] == "s":
                        vAtribuicaoNaoChave.append(
                            f"{oCampo['column_name']} = {chaveA}oConexao.escapeString(o{self.oConstrutor.sClasse}.get{vAtributos[nIndice][1:]}()){chaveF}")
                        vValoresNaoChave.append(
                            f"{chaveA}oConexao.escapeString(o{self.oConstrutor.sClasse}.get{vAtributos[nIndice][1:]}()){chaveF}")
                    else:
                        vAtribuicaoNaoChave.append(
                            f"{oCampo['column_name']} = '{chaveA}o{self.oConstrutor.sClasse}.get{vAtributos[nIndice][1:]}(){chaveF}'")
                        vValoresNaoChave.append(f"'{chaveA}o{self.oConstrutor.sClasse}.get{vAtributos[nIndice][1:]}(){chaveF}'")
                if vAtributos[nIndice][:1] == "s":
                    vCamposReg.append(f"oConexao.unescapeString(oReg[\"{oCampo['column_name']}\"])")
                else:
                    vCamposReg.append(f"oReg[\"{oCampo['column_name']}\"]")

            self.sListaAtributosChave = ",".join(vAtributosChave)
            self.sListaCamposChave = ",".join(vCamposChave)
            self.sListaCamposNaoChave = ",".join(vCamposNaoChave)
            self.sListaValoresNaoChave = ",".join(vValoresNaoChave)
            self.sComparacaoChaveAtributo = " and ".join(vComparacao)
            self.sComparacaoChaveAtributoEsp = " and ".join(vComparacaoEsp)
            self.sAtribuicaoNaoChave = ", ".join(vAtribuicaoNaoChave)
            self.sListaCamposReg = ",".join(vCamposReg)

    def gera(self):
        self.geraAtributos()
        self.geraCampos()
        sArquivo = ""
        with open(os.path.join(os.path.dirname(__file__), "../modelos/modelo_classe_bd.txt"), "r") as f:
            vModelo = f.readlines()
        sArquivo = "".join(vModelo)
        sArquivo = sArquivo.replace("#NOME_CLASSE#", self.oConstrutor.sClasse)
        #sArquivo = sArquivo.replace("#NOME_CLASSE_SIMPLES#", self.oConstrutor.sClasseSimples)
        sArquivo = sArquivo.replace("#LISTA_ATRIBUTOS#", self.sListaAtributos)
        sArquivo = sArquivo.replace("#LISTA_ATRIBUTOS_CONSTRUTOR#", self.sAtributosConstrutor)
        sArquivo = sArquivo.replace("#NOME_TABELA#", self.oConstrutor.sTabela.lower())
        sArquivo = sArquivo.replace("#COMPARACAO_CHAVE_ATRIBUTO#", self.sComparacaoChaveAtributo)
        sArquivo = sArquivo.replace("#COMPARACAO_CHAVE_ATRIBUTO_ESP#", self.sComparacaoChaveAtributoEsp)
        sArquivo = sArquivo.replace("#LISTA_CAMPOS_CHAVE#", self.sListaCamposChave)
        sArquivo = sArquivo.replace("#LISTA_CAMPOS_NAO_CHAVE#", self.sListaCamposNaoChave)
        sArquivo = sArquivo.replace("#VALORES_NAO_CHAVE#", self.sListaValoresNaoChave)
        sArquivo = sArquivo.replace("#LISTA_ATRIBUTOS_CHAVE#", self.sListaAtributosChave)
        sArquivo = sArquivo.replace("#LISTA_CAMPOS_REG#", self.sListaCamposReg)
        sArquivo = sArquivo.replace("#ATRIBUICAO_NAO_CHAVE#", self.sAtribuicaoNaoChave)
        sCaminhoArquivo = os.path.join(os.path.dirname(__file__), "../classes_geradas/", self.sNomeArquivo)
        if os.path.exists(sCaminhoArquivo):
            os.remove(sCaminhoArquivo)
        with open(sCaminhoArquivo, "w+") as pArquivo:
            pArquivo.write(sArquivo)

        sArquivoParent = ""
        with open(os.path.join(os.path.dirname(__file__), "../modelos/modelo_classe_bd_parent.txt"),
                  'r') as vModeloParent:
            sArquivoParent = vModeloParent.read()

        sArquivoParent = sArquivoParent.replace("#NOME_CLASSE#", self.oConstrutor.sClasse)
        #sArquivoParent = sArquivoParent.replace("#NOME_CLASSE_SIMPLES#", self.oConstrutor.sClasseSimples)
        sArquivoParent = sArquivoParent.replace("#LISTA_ATRIBUTOS#", self.sListaAtributos)
        sArquivoParent = sArquivoParent.replace("#LISTA_ATRIBUTOS_CONSTRUTOR#", self.sAtributosConstrutor)
        sArquivoParent = sArquivoParent.replace("#NOME_TABELA#", self.oConstrutor.sTabela.lower())
        sArquivoParent = sArquivoParent.replace("#COMPARACAO_CHAVE_ATRIBUTO#", self.sComparacaoChaveAtributo)
        sArquivoParent = sArquivoParent.replace("#COMPARACAO_CHAVE_ATRIBUTO_ESP#", self.sComparacaoChaveAtributoEsp)
        sArquivoParent = sArquivoParent.replace("#LISTA_CAMPOS_CHAVE#", self.sListaCamposChave)
        sArquivoParent = sArquivoParent.replace("#LISTA_CAMPOS_NAO_CHAVE#", self.sListaCamposNaoChave)
        sArquivoParent = sArquivoParent.replace("#VALORES_NAO_CHAVE#", self.sListaValoresNaoChave)
        sArquivoParent = sArquivoParent.replace("#LISTA_ATRIBUTOS_CHAVE#", self.sListaAtributosChave)
        sArquivoParent = sArquivoParent.replace("#LISTA_CAMPOS_REG#", self.sListaCamposReg)
        sArquivoParent = sArquivoParent.replace("#ATRIBUICAO_NAO_CHAVE#", self.sAtribuicaoNaoChave)

        sCaminhoArquivoParent = os.path.join(os.path.dirname(__file__), "../classes_geradas/", self.sNomeArquivoParent)
        if os.path.exists(sCaminhoArquivoParent):
            os.remove(sCaminhoArquivoParent)

        with open(sCaminhoArquivoParent, 'a+') as pArquivoParent:
            pArquivoParent.write(sArquivoParent)