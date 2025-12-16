class UsuarioService:
    """
    Capa de negocio para la gestión de usuarios.
    """

    def __init__(self, db, auth):
        self.db = db
        self.auth = auth

    def crear_usuario(self, username, password):
        """
        POST: Crea un usuario nuevo aplicando seguridad a la contraseña.
        """
        salt = self.auth.generar_salt()
        password_hash = self.auth.generar_hash(password, salt)

        self.db.insertar("""
        INSERT INTO usuarios (username, password_hash, salt)
        VALUES (?, ?, ?)
        """, (username, password_hash, salt))


class IndicadorService:
    """
    Capa de negocio para los indicadores económicos.
    """

    def __init__(self, db):
        self.db = db

    def registrar_indicador(self, indicador):
        """
        POST: Guarda un indicador económico en la base de datos.
        """
        self.db.insertar("""
        INSERT INTO indicadores
        (nombre, fecha_indicador, valor, fecha_consulta, usuario, proveedor)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            indicador.nombre,
            indicador.fecha_indicador,
            indicador.valor,
            indicador.fecha_consulta,
            indicador.usuario,
            indicador.proveedor
        ))

    def actualizar_valor(self, id_indicador, nuevo_valor):
        """
        PUT: Actualiza el valor de un indicador existente.
        """
        self.db.ejecutar("""
        UPDATE indicadores SET valor = ? WHERE id = ?
        """, (nuevo_valor, id_indicador))

    def eliminar_indicador(self, id_indicador):
        """
        DELETE: Elimina un indicador desde la base de datos.
        """
        self.db.ejecutar("""
        DELETE FROM indicadores WHERE id = ?
        """, (id_indicador,))
