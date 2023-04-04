import os
from datetime import datetime

# CONSTANTES BANCO
# DADOS BASICOS DO SISTEMA
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
BANCO = "LOCAL"
# BANCO = "BANCO"
ACESSO_NEGADO = "Você não tem permissão para acessar esta área."
ACESSO_NEGADO_TRANSACAO = "ACESSO NEGADO"
ACESSO_PERMITIDO_TRANSACAO = "ACESSO PERMITIDO"
ACESSO_TENTATIVA = "TENTATIVA NAO REALIZADA"
IP_USUARIO = os.environ.get('REMOTE_ADDR')
IP_SERVIDOR = (os.environ.get('SERVER_ADDR') or os.environ.get('LOCAL_ADDR') or "SEM IP")
DATAHORA = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# LOCAL
# CAMINHO = '../../../../../admin/'
CAMINHO = '../../../../../'
SITE = '../../../../../admin/'
# CAMINHO = '../../../../../NovoPainelPadraoComNovoLog/'
# SITE = '../../../../../NovoPainelPadraoComNovoLog/'

# ONLINE
# CAMINHO = '../../../../'

# IDS PADROES DO SISTEMA
ID_USUARIO_SISTEMA = 0
GRUPO_ADMINISTRADOR = 1
ALTERAR_SENHA = 11
ACESSO_LOGIN = 2
ACESSO_LOGOUT = 3
ID_USUARIO = 0  # Alterar esta linha para obter o ID do usuário a partir da sessão

# Verifica se a sessão do Flask contém o ID do usuário e atualiza a constante ID_USUARIO
# with app.app_context():
#     if 'oUsuario' in session and session['oUsuario'].getIdUsuario() != "":
#         ID_USUARIO = session['oUsuario'].getIdUsuario()