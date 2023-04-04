from classes.Conexao import Conexao
from classes.Usuario import Usuario
from classes.UsuarioBD import UsuarioBD
from classes.ErrosMysql import ErrosMysql
from classes.ErrosMysqlBD import ErrosMysqlBD
from classes.CategoriaTipoTransacao import CategoriaTipoTransacao
from classes.CategoriaTipoTransacaoBD import CategoriaTipoTransacaoBD
from classes.GrupoUsuario import GrupoUsuario
from classes.GrupoUsuarioBD import GrupoUsuarioBD
from classes.Permissao import Permissao
from classes.PermissaoBD import PermissaoBD
from classes.TipoTransacao import TipoTransacao
from classes.TipoTransacaoBD import TipoTransacaoBD
from classes.Transacao import Transacao
from classes.TransacaoBD import TransacaoBD
from classes.TransacaoAcesso import TransacaoAcesso
from classes.TransacaoAcessoBD import TransacaoAcessoBD

class FachadaSegurancaBDParent:
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def inicializaUsuario(self, nId, nIdGrupoUsuario, sNmUsuario, sLogin, sSenha, sEmail, bLogado, dDtCadastro,
                          bPublicado, bAtivo):
        oUsuario = Usuario(nId, nIdGrupoUsuario, sNmUsuario, sLogin, sSenha, sEmail, bLogado, dDtCadastro, bPublicado,
                           bAtivo)
        return oUsuario

    def inicializaUsuarioBD(self, sBanco):
        oUsuarioBD = UsuarioBD(sBanco)
        return oUsuarioBD

    def recuperaUsuario(self, nId, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        oUsuario = oUsuarioBD.recupera(nId)
        return oUsuario

    def recuperaTodosUsuario(self, sBanco, vWhere=None, vOrder=None):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        voObjeto = []
        voObjeto = oUsuarioBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteUsuario(self, nId, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        bResultado = oUsuarioBD.presente(nId)
        return bResultado

    def insereUsuario(self, oUsuario, voTransacao, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        nId = oUsuarioBD.insere(oUsuario)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraUsuario(self, oUsuario, voTransacao, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        bResultado = oUsuarioBD.altera(oUsuario)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiUsuario(self, nId, voTransacao, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        bResultado = oUsuarioBD.exclui(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaUsuario(self, nId, voTransacao, sBanco):
        oUsuarioBD = self.inicializaUsuarioBD(sBanco)
        bResultado = oUsuarioBD.desativa(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaErrosMysql(self, nId, sErro, nIdUsuario, sIp, dDtCadastro, bPublicado, bAtivo):
        oErrosMysql = ErrosMysql(nId, sErro, nIdUsuario, sIp, dDtCadastro, bPublicado, bAtivo)
        return oErrosMysql

    def inicializaErrosMysqlBD(self, sBanco):
        oErrosMysqlBD = ErrosMysqlBD(sBanco)
        return oErrosMysqlBD

    def recuperaErrosMysql(self, nId, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        oErrosMysql = oErrosMysqlBD.recupera(nId)
        return oErrosMysql

    def recuperaTodosErrosMysql(self, sBanco, vWhere=None, vOrder=None):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        voObjeto = []
        voObjeto = oErrosMysqlBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteErrosMysql(self, nId, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        bResultado = oErrosMysqlBD.presente(nId)
        return bResultado

    def insereErrosMysql(self, oErrosMysql, voTransacao, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        nId = oErrosMysqlBD.insere(oErrosMysql)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraErrosMysql(self, oErrosMysql, voTransacao, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        bResultado = oErrosMysqlBD.altera(oErrosMysql)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiErrosMysql(self, nId, voTransacao, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        bResultado = oErrosMysqlBD.exclui(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaErrosMysql(self, nId, voTransacao, sBanco):
        oErrosMysqlBD = self.inicializaErrosMysqlBD(sBanco)
        bResultado = oErrosMysqlBD.desativa(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaCategoriaTipoTransacao(self, nId, sDescricao, dDtCadastro, bPublicado, bAtivo):
        oCategoriaTipoTransacao = CategoriaTipoTransacao(nId, sDescricao, dDtCadastro, bPublicado, bAtivo)
        return oCategoriaTipoTransacao

    def inicializaCategoriaTipoTransacaoBD(self, sBanco):
        oCategoriaTipoTransacaoBD = CategoriaTipoTransacaoBD(sBanco)
        return oCategoriaTipoTransacaoBD

    def recuperaCategoriaTipoTransacao(self, nId, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        oCategoriaTipoTransacao = oCategoriaTipoTransacaoBD.recupera(nId)
        return oCategoriaTipoTransacao

    def recuperaTodosCategoriaTipoTransacao(self, sBanco, vWhere=None, vOrder=None):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        voObjeto = []
        voObjeto = oCategoriaTipoTransacaoBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteCategoriaTipoTransacao(self, nId, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        bResultado = oCategoriaTipoTransacaoBD.presente(nId)
        return bResultado

    def insereCategoriaTipoTransacao(self, oCategoriaTipoTransacao, voTransacao, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        nId = oCategoriaTipoTransacaoBD.insere(oCategoriaTipoTransacao)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraCategoriaTipoTransacao(self, oCategoriaTipoTransacao, voTransacao, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        bResultado = oCategoriaTipoTransacaoBD.altera(oCategoriaTipoTransacao)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiCategoriaTipoTransacao(self, nId, voTransacao, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        bResultado = oCategoriaTipoTransacaoBD.exclui(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaCategoriaTipoTransacao(self, nId, voTransacao, sBanco):
        oCategoriaTipoTransacaoBD = self.inicializaCategoriaTipoTransacaoBD(sBanco)
        bResultado = oCategoriaTipoTransacaoBD.desativa(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaGrupoUsuario(self, nId, sNmGrupoUsuario, dDtCadastro, bPublicado, bAtivo):
        oGrupoUsuario = GrupoUsuario(nId, sNmGrupoUsuario, dDtCadastro, bPublicado, bAtivo)
        return oGrupoUsuario

    def inicializaGrupoUsuarioBD(self, sBanco):
        oGrupoUsuarioBD = GrupoUsuarioBD(sBanco)
        return oGrupoUsuarioBD

    def recuperaGrupoUsuario(self, nId, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        oGrupoUsuario = oGrupoUsuarioBD.recupera(nId)
        return oGrupoUsuario

    def recuperaTodosGrupoUsuario(self, sBanco, vWhere=None, vOrder=None):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        voObjeto = []
        voObjeto = oGrupoUsuarioBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteGrupoUsuario(self, nId, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        bResultado = oGrupoUsuarioBD.presente(nId)
        return bResultado

    def insereGrupoUsuario(self, oGrupoUsuario, voTransacao, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        nId = oGrupoUsuarioBD.insere(oGrupoUsuario)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraGrupoUsuario(self, oGrupoUsuario, voTransacao, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        bResultado = oGrupoUsuarioBD.altera(oGrupoUsuario)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiGrupoUsuario(self, nId, voTransacao, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        bResultado = oGrupoUsuarioBD.exclui(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaGrupoUsuario(self, nId, voTransacao, sBanco):
        oGrupoUsuarioBD = self.inicializaGrupoUsuarioBD(sBanco)
        bResultado = oGrupoUsuarioBD.desativa(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaPermissao(self, nIdTipoTransacao, nIdGrupoUsuario, dDtCadastro, bPublicado, bAtivo):
        oPermissao = Permissao(nIdTipoTransacao, nIdGrupoUsuario, dDtCadastro, bPublicado, bAtivo)
        return oPermissao

    def inicializaPermissaoBD(self, sBanco):
        oPermissaoBD = PermissaoBD(sBanco)
        return oPermissaoBD

    def recuperaPermissao(self, nIdTipoTransacao, nIdGrupoUsuario, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        oPermissao = oPermissaoBD.recupera(nIdTipoTransacao, nIdGrupoUsuario)
        return oPermissao

    def recuperaTodosPermissao(self, sBanco, vWhere=None, vOrder=None):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        voObjeto = []
        voObjeto = oPermissaoBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presentePermissao(self, nIdTipoTransacao, nIdGrupoUsuario, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        bResultado = oPermissaoBD.presente(nIdTipoTransacao, nIdGrupoUsuario)
        return bResultado

    def inserePermissao(self, oPermissao, voTransacao, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        nId = oPermissaoBD.insere(oPermissao)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraPermissao(self, oPermissao, voTransacao, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        bResultado = oPermissaoBD.altera(oPermissao)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiPermissao(self, nIdTipoTransacao, nIdGrupoUsuario, voTransacao, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        bResultado = oPermissaoBD.exclui(nIdTipoTransacao, nIdGrupoUsuario)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaPermissao(self, nIdTipoTransacao, nIdGrupoUsuario, voTransacao, sBanco):
        oPermissaoBD = self.inicializaPermissaoBD(sBanco)
        bResultado = oPermissaoBD.desativa(nIdTipoTransacao, nIdGrupoUsuario)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaTipoTransacao(self, nId, nIdCategoriaTipoTransacao, sTransacao, dDtCadastro, bPublicado, bAtivo):
        oTipoTransacao = TipoTransacao(nId, nIdCategoriaTipoTransacao, sTransacao, dDtCadastro, bPublicado, bAtivo)
        return oTipoTransacao

    def inicializaTipoTransacaoBD(self, sBanco):
        oTipoTransacaoBD = TipoTransacaoBD(sBanco)
        return oTipoTransacaoBD

    def recuperaTipoTransacao(self, nId, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        oTipoTransacao = oTipoTransacaoBD.recupera(nId)
        return oTipoTransacao

    def recuperaTodosTipoTransacao(self, sBanco, vWhere=None, vOrder=None):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        voObjeto = []
        voObjeto = oTipoTransacaoBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteTipoTransacao(self, nId, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        bResultado = oTipoTransacaoBD.presente(nId)
        return bResultado

    def insereTipoTransacao(self, oTipoTransacao, voTransacao, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        nId = oTipoTransacaoBD.insere(oTipoTransacao)
        if nId and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return nId

    def alteraTipoTransacao(self, oTipoTransacao, voTransacao, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        bResultado = oTipoTransacaoBD.altera(oTipoTransacao)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def excluiTipoTransacao(self, nId, voTransacao, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        bResultado = oTipoTransacaoBD.exclui(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def desativaTipoTransacao(self, nId, voTransacao, sBanco):
        oTipoTransacaoBD = self.inicializaTipoTransacaoBD(sBanco)
        bResultado = oTipoTransacaoBD.desativa(nId)
        if bResultado and isinstance(voTransacao, list) and len(voTransacao) > 0:
            oFachadaSeguranca = FachadaSegurancaBD(sBanco)
            for oTransacao in voTransacao:
                if oTransacao and isinstance(oTransacao, object):
                    if not oFachadaSeguranca.insereTransacao(oTransacao, sBanco):
                        return False
        return bResultado

    def inicializaTransacao(self, nId, nIdTipoTransacao, nIdUsuario, sObjeto, sIp, dDtCadastro, bPublicado, bAtivo):
        oTransacao = Transacao(nId, nIdTipoTransacao, nIdUsuario, sObjeto, sIp, dDtCadastro, bPublicado, bAtivo)
        return oTransacao

    def inicializaTransacaoBD(self, sBanco):
        oTransacaoBD = TransacaoBD(sBanco)
        return oTransacaoBD

    def recuperaTransacao(self, nId, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        oTransacao = oTransacaoBD.recupera(nId)
        return oTransacao

    def recuperaTodosTransacao(self, sBanco, vWhere=None, vOrder=None):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        voObjeto = []
        voObjeto = oTransacaoBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteTransacao(self, nId, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        bResultado = oTransacaoBD.presente(nId)
        return bResultado

    def insereTransacao(self, oTransacao, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        nId = oTransacaoBD.insere(oTransacao)
        return nId

    def alteraTransacao(self, oTransacao, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        bResultado = oTransacaoBD.altera(oTransacao)
        return bResultado

    def excluiTransacao(self, nId, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        bResultado = oTransacaoBD.exclui(nId)
        return bResultado

    def desativaTransacao(self, nId, sBanco):
        oTransacaoBD = self.inicializaTransacaoBD(sBanco)
        bResultado = oTransacaoBD.desativa(nId)
        return bResultado

    def inicializaTransacaoAcesso(self, nId, nIdTipoTransacao, nIdUsuario, sObjeto, sIp, dDtCadastro, bPublicado,
                                  bAtivo):
        oTransacaoAcesso = TransacaoAcesso(nId, nIdTipoTransacao, nIdUsuario, sObjeto, sIp, dDtCadastro, bPublicado,
                                           bAtivo)
        return oTransacaoAcesso

    def inicializaTransacaoAcessoBD(self, sBanco):
        oTransacaoAcessoBD = TransacaoAcessoBD(sBanco)
        return oTransacaoAcessoBD

    def recuperaTransacaoAcesso(self, nId, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        oTransacaoAcesso = oTransacaoAcessoBD.recupera(nId)
        return oTransacaoAcesso

    def recuperaTodosTransacaoAcesso(self, sBanco, vWhere=None, vOrder=None):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        voObjeto = []
        voObjeto = oTransacaoAcessoBD.recuperaTodos(vWhere, vOrder)
        return voObjeto

    def presenteTransacaoAcesso(self, nId, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        bResultado = oTransacaoAcessoBD.presente(nId)
        return bResultado

    def insereTransacaoAcesso(self, oTransacaoAcesso, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        nId = oTransacaoAcessoBD.insere(oTransacaoAcesso)
        return nId

    def alteraTransacaoAcesso(self, oTransacaoAcesso, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        bResultado = oTransacaoAcessoBD.altera(oTransacaoAcesso)
        return bResultado

    def excluiTransacaoAcesso(self, nId, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        bResultado = oTransacaoAcessoBD.exclui(nId)
        return bResultado

    def desativaTransacaoAcesso(self, nId, sBanco):
        oTransacaoAcessoBD = self.inicializaTransacaoAcessoBD(sBanco)
        bResultado = oTransacaoAcessoBD.desativa(nId)
        return bResultado