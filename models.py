class Usuario:
    """
    Modelo que representa un usuario del sistema.
    No contiene lógica, solo estructura de datos.
    """

    def __init__(self, username, password_hash, salt):
        self.username = username
        self.password_hash = password_hash
        self.salt = salt


class Indicador:
    """
    Modelo que representa un indicador económico.
    Se utiliza para transportar datos dentro del sistema.
    """

    def __init__(self, nombre, fecha_indicador, valor, fecha_consulta, usuario, proveedor):
        self.nombre = nombre
        self.fecha_indicador = fecha_indicador
        self.valor = valor
        self.fecha_consulta = fecha_consulta
        self.usuario = usuario
        self.proveedor = proveedor
