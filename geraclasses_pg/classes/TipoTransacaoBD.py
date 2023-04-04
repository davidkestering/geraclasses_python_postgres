from classes.TipoTransacaoBDParent import TipoTransacaoBDParent

class TipoTransacaoBD(TipoTransacaoBDParent):
    def __init__(self, sBanco):
        self.pConexao = TipoTransacaoBDParent(sBanco=sBanco)

    def desativaPorCategoria(self, nIdCategoria):
        oConexao = self.getConexao()
        sSql = f"update seg_tipo_transacao set publicado = 0, ativo = '0' where id_categoria_tipo_transacao = '{nIdCategoria}'"
        oConexao.execute(sSql)
        return oConexao.getConsulta()