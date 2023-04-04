from classes.CategoriaTipoTransacao import CategoriaTipoTransacao
from classes.Conexao import Conexao

class CategoriaTipoTransacaoBDParent(Conexao):
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return Conexao.getConexao(self.pConexao)

    def recupera(self, nId):
        oConexao = self.getConexao()
        sSql = f"select * from seg_categoria_tipo_transacao where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            oCategoriaTipoTransacao = CategoriaTipoTransacao(oReg.id,oConexao.unescapeString(oReg.descricao),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            return oCategoriaTipoTransacao
        return False

    def presente(self, nId):
        oConexao = self.getConexao()
        sSql = f"select id from seg_categoria_tipo_transacao where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            return len(oReg) > 0
        return 0

    def insere(self, oCategoriaTipoTransacao):
        oConexao = self.getConexao()
        sSql = f"insert into seg_categoria_tipo_transacao (descricao,dt_cadastro,publicado,ativo) values ('{oConexao.escapeString(oCategoriaTipoTransacao.getDescricao())}','{oCategoriaTipoTransacao.getDtCadastro()}','{oCategoriaTipoTransacao.getPublicado()}','{oCategoriaTipoTransacao.getAtivo()}')"
        oConexao.execute(sSql)
        nId = oConexao.getLastId()
        if nId:
            return nId
        return oConexao.getConsulta()

    def altera(self, oCategoriaTipoTransacao):
        oConexao = self.getConexao()
        sSql = f"update seg_categoria_tipo_transacao set descricao = '{oConexao.escapeString(oCategoriaTipoTransacao.getDescricao())}', dt_cadastro = '{oCategoriaTipoTransacao.getDtCadastro()}', publicado = '{oCategoriaTipoTransacao.getPublicado()}', ativo = '{oCategoriaTipoTransacao.getAtivo()}' where id = '{oCategoriaTipoTransacao.getId()}'"
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
                sSql = "SELECT * FROM seg_categoria_tipo_transacao WHERE "
                sSql = (sSql + sSql2)[:-5]
            else:
                sSql = "SELECT * FROM seg_categoria_tipo_transacao "
        else:
            sSql = "SELECT * FROM seg_categoria_tipo_transacao "

        if sOrder:
            sSql += " ORDER BY " + sOrder

        oConexao.execute(sSql)
        voObjeto = []
        while oReg := oConexao.fetchObject():
            oCategoriaTipoTransacao = CategoriaTipoTransacao(oReg.id,oConexao.unescapeString(oReg.descricao),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            voObjeto.append(oCategoriaTipoTransacao)
            del oCategoriaTipoTransacao
        return voObjeto

    def exclui(self, nId):
        oConexao = self.getConexao()
        sSql = f"delete from seg_categoria_tipo_transacao where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativa(self, nId):
        oConexao = self.getConexao()
        sSql = f"update seg_categoria_tipo_transacao set ativo = '0' where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()