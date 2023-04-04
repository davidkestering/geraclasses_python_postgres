import os
import re

class GeradoraFachada:
    def __init__(self, sBanco, vsInteriorFachada, vNomeClasses):
        self.sBanco = sBanco.capitalize()
        self.vsInteriorFachada = vsInteriorFachada
        self.sInteriorFachada = ""
        self.vNomeClasses = vNomeClasses
        self.sNomeArquivo = f'Fachada{self.sBanco}BD.py'
        self.sNomeArquivoParent = f'Fachada{self.sBanco}BDParent.py'

    def geraIncludeClasses(self):
        if len(self.vNomeClasses) > 0:
            self.sIncludeClasses = ''
            for sNomeClasse in self.vNomeClasses:
                self.sIncludeClasses += f'from classes.{sNomeClasse} import {sNomeClasse}\n'
                self.sIncludeClasses += f'from classes.{sNomeClasse}BD import {sNomeClasse}BD\n'
            self.sIncludeClasses = self.sIncludeClasses[:-1]

    def gera(self):
        self.geraIncludeClasses()
        with open(os.path.join(os.path.dirname(__file__), '..', 'modelos', 'modelo_classe_fachada.txt'), 'r') as f:
            sArquivo = f.read()
        sBancoPrimeiraMaiuscula = ''.join([sNome.capitalize() for sNome in self.sBanco.split('_')])
        sArquivo = sArquivo.replace('#INCLUDE_CLASSES#', self.sIncludeClasses)
        sArquivo = sArquivo.replace('#BANCO#', sBancoPrimeiraMaiuscula)
        sCaminhoArquivo = os.path.join(os.path.dirname(__file__), '..', 'classes_geradas', self.sNomeArquivo)
        if os.path.exists(sCaminhoArquivo):
            os.remove(sCaminhoArquivo)
        with open(sCaminhoArquivo, 'a+') as pArquivo:
            pArquivo.write(sArquivo)

        with open(os.path.join(os.path.dirname(__file__), '..', 'modelos', 'modelo_classe_fachada_parent.txt'),
                  'r') as f:
            sArquivoParent = f.read()
        sBancoPrimeiraMaiuscula = ''.join([sNome.capitalize() for sNome in self.sBanco.split('_')])
        sArquivoParent = sArquivoParent.replace('#INCLUDE_CLASSES#', self.sIncludeClasses)
        sArquivoParent = sArquivoParent.replace('#BANCO#', sBancoPrimeiraMaiuscula)

        self.sInteriorFachada = '\n'.join(sTexto for sTexto in self.vsInteriorFachada)

        sArquivoParent = sArquivoParent.replace('#INTERIOR_FACHADA#', self.sInteriorFachada)
        sCaminhoArquivoParent = os.path.join(os.path.dirname(__file__), '..', 'classes_geradas',
                                             self.sNomeArquivoParent)
        if os.path.exists(sCaminhoArquivoParent):
            os.remove(sCaminhoArquivoParent)
        with open(sCaminhoArquivoParent, 'a+') as pArquivoParent:
            pArquivoParent.write(sArquivoParent)
