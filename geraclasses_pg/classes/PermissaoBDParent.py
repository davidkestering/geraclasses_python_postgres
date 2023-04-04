from classes.Permissao import Permissao
from classes.Conexao import Conexao

class PermissaoBDParent(Conexao):
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return Conexao.getConexao(self.pConexao)

    def recupera(self, nIdTipoTransacao, nIdGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"select * from seg_permissao where id_tipo_transacao = '{nIdTipoTransacao}' and id_grupo_usuario = '{nIdGrupoUsuario}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            oPermissao = Permissao(oReg.id_tipo_transacao, oReg.id_grupo_usuario, oReg.dt_cadastro, oReg.publicado,
                                   oReg.ativo)
            return oPermissao
        return False

    def presente(self, nIdTipoTransacao, nIdGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"select id_tipo_transacao,id_grupo_usuario from seg_permissao where id_tipo_transacao = '{nIdTipoTransacao}' and id_grupo_usuario = '{nIdGrupoUsuario}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            return len(oReg) > 0
        return 0

    def insere(self, oPermissao):
        oConexao = self.getConexao()
        sSql = f"insert into seg_permissao (id_tipo_transacao,id_grupo_usuario,dt_cadastro,publicado,ativo) values ('{oPermissao.getIdTipoTransacao()}','{oPermissao.getIdGrupoUsuario()}','{oPermissao.getDtCadastro()}','{oPermissao.getPublicado()}','{oPermissao.getAtivo()}')"
        oConexao.execute(sSql)
        nId = oConexao.getLastId()
        if nId:
            return nId
        return oConexao.getConsulta()

    def altera(self, oPermissao):
        oConexao = self.getConexao()
        sSql = f"update seg_permissao set dt_cadastro = '{oPermissao.getDtCadastro()}', publicado = '{oPermissao.getPublicado()}', ativo = '{oPermissao.getAtivo()}' where id_tipo_transacao = '{oPermissao.getIdTipoTransacao()}' and id_grupo_usuario = '{oPermissao.getIdGrupoUsuario()}'"
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
                sSql = "SELECT * FROM seg_permissao WHERE "
                sSql = (sSql + sSql2)[:-5]
            else:
                sSql = "SELECT * FROM seg_permissao "
        else:
            sSql = "SELECT * FROM seg_permissao "

        if sOrder:
            sSql += " ORDER BY " + sOrder

        oConexao.execute(sSql)
        voObjeto = []
        while oReg := oConexao.fetchObject():
            oPermissao = Permissao(oReg.id_tipo_transacao,oReg.id_grupo_usuario,oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            voObjeto.append(oPermissao)
            del oPermissao
        return voObjeto

    def exclui(self, nIdTipoTransacao, nIdGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"delete from seg_permissao where id_tipo_transacao = '{nIdTipoTransacao}' and id_grupo_usuario = '{nIdGrupoUsuario}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativa(self, nIdTipoTransacao, nIdGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"update seg_permissao set ativo = '0' where id_tipo_transacao = '{nIdTipoTransacao}' and id_grupo_usuario = '{nIdGrupoUsuario}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()