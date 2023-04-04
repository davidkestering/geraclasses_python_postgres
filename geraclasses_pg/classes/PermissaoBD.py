from classes.PermissaoBDParent import PermissaoBDParent

class PermissaoBD(PermissaoBDParent):
    def __init__(self, sBanco):
        self.pConexao = PermissaoBDParent(sBanco=sBanco)

    def desativaPorGrupoUsuario(self,nIdGrupoUsuario):
        oConexao = self.getConexao()
        sSql = f"update seg_permissao set publicado = 0, ativo = '0' where id_grupo_usuario = '{nIdGrupoUsuario}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()

    def desativaPorTipoTransacao(self,nIdTipoTransacao):
        oConexao = self.getConexao()
        sSql = f"update seg_permissao set publicado = 0, ativo = '0' where id_tipo_transacao = '{nIdTipoTransacao}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()