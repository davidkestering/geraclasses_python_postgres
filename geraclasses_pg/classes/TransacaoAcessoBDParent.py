from classes.TransacaoAcesso import TransacaoAcesso
from classes.Conexao import Conexao

class TransacaoAcessoBDParent(Conexao):
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return Conexao.getConexao(self.pConexao)

    def recupera(self, nId):
        oConexao = self.getConexao()
        sSql = f"select * from seg_transacao_acesso where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            oTransacaoAcesso = TransacaoAcesso(oReg.id,oReg.id_tipo_transacao,oReg.id_usuario,oConexao.unescapeString(oReg.objeto),oConexao.unescapeString(oReg.ip),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            return oTransacaoAcesso
        return False

    def presente(self, nId):
        oConexao = self.getConexao()
        sSql = f"select id from seg_transacao_acesso where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            return len(oReg) > 0
        return 0

    def insere(self, oTransacaoAcesso):
        oConexao = self.getConexao()
        sSql = f"insert into seg_transacao_acesso (id_tipo_transacao,id_usuario,objeto,ip,dt_cadastro,publicado,ativo) values ('{oTransacaoAcesso.getIdTipoTransacao()}','{oTransacaoAcesso.getIdUsuario()}','{oConexao.escapeString(oTransacaoAcesso.getObjeto())}','{oConexao.escapeString(oTransacaoAcesso.getIp())}','{oTransacaoAcesso.getDtCadastro()}','{oTransacaoAcesso.getPublicado()}','{oTransacaoAcesso.getAtivo()}')"
        oConexao.execute(sSql)
        nId = oConexao.getLastId()
        if nId:
            return nId
        return oConexao.getConsulta()

    def altera(self, oTransacaoAcesso):
        oConexao = self.getConexao()
        sSql = f"update seg_transacao_acesso set id_tipo_transacao = '{oTransacaoAcesso.getIdTipoTransacao()}', id_usuario = '{oTransacaoAcesso.getIdUsuario()}', objeto = '{oConexao.escapeString(oTransacaoAcesso.getObjeto())}', ip = '{oConexao.escapeString(oTransacaoAcesso.getIp())}', dt_cadastro = '{oTransacaoAcesso.getDtCadastro()}', publicado = '{oTransacaoAcesso.getPublicado()}', ativo = '{oTransacaoAcesso.getAtivo()}' where id = '{oTransacaoAcesso.getId()}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def recuperaTodos(self, vWhere, sOrder):
        oConexao = self.getConexao()
        if isinstance(vWhere, list) and len(vWhere) > 0:
            sSql2 = ""
            for sWhere in vWhere:
                if sWhere != "":
                    sSql2 += sWhere + " AND "
            if sSql2 != "":
                sSql = "SELECT * FROM seg_transacao_acesso WHERE "
                sSql = (sSql + sSql2)[:-5]
            else:
                sSql = "SELECT * FROM seg_transacao_acesso "
        else:
            sSql = "SELECT * FROM seg_transacao_acesso "

        if sOrder:
            sSql += " ORDER BY " + sOrder

        oConexao.execute(sSql)
        voObjeto = []
        while oReg := oConexao.fetchObject():
            oTransacaoAcesso = TransacaoAcesso(oReg.id,oReg.id_tipo_transacao,oReg.id_usuario,oConexao.unescapeString(oReg.objeto),oConexao.unescapeString(oReg.ip),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            voObjeto.append(oTransacaoAcesso)
            del oTransacaoAcesso
        return voObjeto

    def exclui(self, nId):
        oConexao = self.getConexao()
        sSql = f"delete from seg_transacao_acesso where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativa(self, nId):
        oConexao = self.getConexao()
        sSql = f"update seg_transacao_acesso set ativo = '0' where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()