from classes.GrupoUsuario import GrupoUsuario
from classes.Conexao import Conexao

class GrupoUsuarioBDParent(Conexao):
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return Conexao.getConexao(self.pConexao)

    def recupera(self, nId):
        oConexao = self.getConexao()
        sSql = f"select * from seg_grupo_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            oGrupoUsuario = GrupoUsuario(oReg.id,oConexao.unescapeString(oReg.nm_grupo_usuario),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            return oGrupoUsuario
        return False

    def presente(self, nId):
        oConexao = self.getConexao()
        sSql = f"select id from seg_grupo_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            return len(oReg) > 0
        return 0

    def insere(self, oGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"insert into seg_grupo_usuario (nm_grupo_usuario,dt_cadastro,publicado,ativo) values ('{oConexao.escapeString(oGrupoUsuario.getNmGrupoUsuario())}','{oGrupoUsuario.getDtCadastro()}','{oGrupoUsuario.getPublicado()}','{oGrupoUsuario.getAtivo()}')"
        oConexao.execute(sSql)
        nId = oConexao.getLastId()
        if nId:
            return nId
        return oConexao.getConsulta()

    def altera(self, oGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"update seg_grupo_usuario set nm_grupo_usuario = '{oConexao.escapeString(oGrupoUsuario.getNmGrupoUsuario())}', dt_cadastro = '{oGrupoUsuario.getDtCadastro()}', publicado = '{oGrupoUsuario.getPublicado()}', ativo = '{oGrupoUsuario.getAtivo()}' where id = '{oGrupoUsuario.getId()}'"
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
                sSql = "SELECT * FROM seg_grupo_usuario WHERE "
                sSql = (sSql + sSql2)[:-5]
            else:
                sSql = "SELECT * FROM seg_grupo_usuario "
        else:
            sSql = "SELECT * FROM seg_grupo_usuario "

        if sOrder:
            sSql += " ORDER BY " + sOrder

        oConexao.execute(sSql)
        voObjeto = []
        while oReg := oConexao.fetchObject():
            oGrupoUsuario = GrupoUsuario(oReg.id,oConexao.unescapeString(oReg.nm_grupo_usuario),oReg.dt_cadastro,oReg.publicado,oReg.ativo)
            voObjeto.append(oGrupoUsuario)
            del oGrupoUsuario
        return voObjeto

    def exclui(self, nId):
        oConexao = self.getConexao()
        sSql = f"delete from seg_grupo_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativa(self, nId):
        oConexao = self.getConexao()
        sSql = f"update seg_grupo_usuario set ativo = '0' where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()