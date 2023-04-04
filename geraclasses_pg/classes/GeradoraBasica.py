import os
import re

class GeradoraBasica:
    def __init__(self, oConstrutor):
        self.oConstrutor = oConstrutor
        self.sNomeArquivo = self.oConstrutor.sClasse + ".py"
        self.sNomeArquivoParent = self.oConstrutor.sClasse + "Parent.py"
        self.sGetSet = ""
        self.sAtributosConstrutor = ""
        self.sListaAtributos = ""
        self.sInicializacaoBasica = ""
        self.sInicializacaoBasicaParent = ""

    def geraAtributos(self):
        vAtributos = self.oConstrutor.vAtributos
        if len(vAtributos) > 0:
            for sAtributo in vAtributos:
                sNomeAtributo = sAtributo[1:]
                self.sAtributosConstrutor += "{},".format(sAtributo)
                self.sListaAtributos += "var {}\n".format(sAtributo, sAtributo)
                self.sGetSet += "def get{}(self):\n        return self.{}\n\n    ".format(sNomeAtributo,sAtributo)
                self.sGetSet += "def set{}(self, {}):\n        self.{} = {}\n\n    ".format(sNomeAtributo,sAtributo,sAtributo,sAtributo)
                self.sInicializacaoBasica += "self.set{}({})\n        ".format(sNomeAtributo, sAtributo)
                self.sInicializacaoBasicaParent += "self.{} = {}\n        ".format(sAtributo, sAtributo)

            self.sAtributosConstrutor = self.sAtributosConstrutor[:-1]

    def gera(self):
        self.geraAtributos()
        sArquivo = ""
        sArquivoParent = ""
        sCaminhoArquivo = os.path.dirname(__file__) + "/../classes_geradas/" + self.sNomeArquivo
        sCaminhoArquivoParent = os.path.dirname(__file__) + "/../classes_geradas/" + self.sNomeArquivoParent

        with open(os.path.dirname(__file__) + "/../modelos/modelo_classe_basica.txt", "r") as f:
            vModelo = f.readlines()
        sArquivo = "".join(vModelo)

        sArquivo = re.sub("#NOME_CLASSE#", self.oConstrutor.sClasse, sArquivo)
        #sArquivo = re.sub("#NOME_CLASSE_SIMPLES#", self.oConstrutor.sClasseSimples, sArquivo)
        sArquivo = re.sub("#LISTA_ATRIBUTOS#", self.sListaAtributos, sArquivo)
        sArquivo = re.sub("#LISTA_ATRIBUTOS_CONSTRUTOR#", self.sAtributosConstrutor, sArquivo)
        sArquivo = re.sub("#INICIALIZACAO#", self.sInicializacaoBasica, sArquivo)
        sArquivo = re.sub("#GET_SET#", self.sGetSet, sArquivo)

        if os.path.exists(sCaminhoArquivo):
            os.remove(sCaminhoArquivo)

        with open(sCaminhoArquivo, "a+") as f:
            f.write(sArquivo)

        with open(os.path.dirname(__file__) + "/../modelos/modelo_classe_basica_parent.txt", "r") as f:
            vModeloParent = f.readlines()
        sArquivoParent = "".join(vModeloParent)

        sArquivoParent = re.sub("#NOME_CLASSE#", self.oConstrutor.sClasse, sArquivoParent)
        #sArquivoParent = re.sub("#NOME_CLASSE_SIMPLES#", self.oConstrutor.sClasseSimples, sArquivoParent)
        sArquivoParent = re.sub("#LISTA_ATRIBUTOS#", self.sListaAtributos, sArquivoParent)
        sArquivoParent = re.sub("#LISTA_ATRIBUTOS_CONSTRUTOR#", self.sAtributosConstrutor, sArquivoParent)
        sArquivoParent = re.sub("#INICIALIZACAO#", self.sInicializacaoBasicaParent, sArquivoParent)
        sArquivoParent = re.sub("#GET_SET#", self.sGetSet, sArquivoParent)

        if os.path.exists(sCaminhoArquivoParent):
            os.remove(sCaminhoArquivoParent)

        with open(sCaminhoArquivoParent, "a+") as f:
            f.write(sArquivoParent)
            # print(sArquivoParent)

