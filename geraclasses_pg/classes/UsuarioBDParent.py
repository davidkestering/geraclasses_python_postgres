from classes.Usuario import Usuario
from classes.Conexao import Conexao

class UsuarioBDParent(Conexao):
    def __init__(self, sBanco):
        self.pConexao = Conexao(sServidor=sBanco)

    def getConexao(self):
        return Conexao.getConexao(self.pConexao)

    def recupera(self, nId):
        oConexao = self.getConexao()
        sSql = f"select * from seg_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            oUsuario = Usuario(oReg.id, oReg.id_grupo_usuario, oConexao.unescapeString(oReg.nm_usuario), oConexao.unescapeString(oReg.login), oReg.senha, oConexao.unescapeString(oReg.email), oReg.logado, oReg.dt_cadastro, oReg.publicado, oReg.ativo)
            return oUsuario
        return False

    def presente(self, nId):
        oConexao = self.getConexao()
        sSql = f"select id from seg_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        oReg = oConexao.fetchObject()
        if oReg:
            return len(oReg) > 0
        return 0

    def insere(self, oUsuario):
        oConexao = self.getConexao()
        sSql = f"insert into seg_usuario (id_grupo_usuario, nm_usuario, login, senha, email, logado, dt_cadastro, publicado, ativo) values ('{oUsuario.getIdGrupoUsuario()}', '{oConexao.escapeString(oUsuario.getNmUsuario())}', '{oConexao.escapeString(oUsuario.getLogin())}', '{oUsuario.getSenha()}', '{oConexao.escapeString(oUsuario.getEmail())}', '{oUsuario.getLogado()}', '{oUsuario.getDtCadastro()}', '{oUsuario.getPublicado()}', '{oUsuario.getAtivo()}')"
        oConexao.execute(sSql)
        if oConexao.getErro() is None:
            oUsuario.setId(oConexao.getLastId())
            return True
        return False

    def altera(self, oUsuario):
        oConexao = self.getConexao()
        sSql = f"update seg_usuario set id_grupo_usuario = '{oUsuario.getIdGrupoUsuario()}', nm_usuario = '{oConexao.escapeString(oUsuario.getNmUsuario())}', login = '{oConexao.escapeString(oUsuario.getLogin())}', senha = '{oUsuario.getSenha()}', email = '{oConexao.escapeString(oUsuario.getEmail())}', logado = '{oUsuario.getLogado()}', dt_cadastro = '{oUsuario.getDtCadastro()}', publicado = '{oUsuario.getPublicado()}', ativo = '{oUsuario.getAtivo()}' where id = '{oUsuario.getId()}'"
        oConexao.execute(sSql)
        return oConexao.getErro() is None

    def recuperaTodos(self, vWhere=None, sOrder=None):
        oConexao = self.getConexao()
        if vWhere!=None:
            sSql2 = ""
            for sWhere in vWhere:
                if sWhere != "":
                    sSql2 += sWhere + " AND "
            if sSql2 != "":
                sSql = f"SELECT * FROM seg_usuario WHERE {sSql2[:-5]}"
            else:
                sSql = "SELECT * FROM seg_usuario "
        else:
            sSql = "SELECT * FROM seg_usuario "
        if sOrder!=None:
            sSql += " ORDER BY " + sOrder
        oConexao.execute(sSql)
        voObjeto = []
        while True:
            oReg = oConexao.fetchObject()
            if not oReg:
                break
            oUsuario = Usuario(oReg.id, oReg.id_grupo_usuario, oConexao.unescapeString(oReg.nm_usuario),
                               oConexao.unescapeString(oReg.login), oReg.senha,
                               oConexao.unescapeString(oReg.email), oReg.logado, oReg.dt_cadastro, oReg.publicado,
                               oReg.ativo)
            voObjeto.append(oUsuario)
            del oUsuario
        return voObjeto

    def exclui(self, nId):
        oConexao = self.getConexao()
        sSql = f"delete from seg_usuario where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativa(self, nId):
        oConexao = self.getConexao()
        sSql = f"update seg_usuario set ativo = '0' where id = '{nId}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()