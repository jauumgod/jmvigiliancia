from ..models.usuarios import Usuarios

def create_user(usuario, senha):

    db = Usuarios.query.add()

    return True

