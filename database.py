import sqlite3

class Database:
    """
    Clase que se encarga de toda la comunicación con la base de datos.
    Centraliza las operaciones para evitar duplicar código.
    """

    def __init__(self, db_name="indicadores.db"):
        # Se establece la conexión con la base de datos SQLite
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def insertar_usuario(self, username, password_hash, salt):
        """
        Inserta un nuevo usuario en la base de datos.
        Se almacena el hash de la contraseña y su salt asociada.
        """
        self.cursor.execute("""
            INSERT INTO usuarios (username, password_hash, salt)
            VALUES (?, ?, ?)
        """, (username, password_hash, salt))
        self.connection.commit()  # Confirma los cambios en la base de datos

    def obtener_usuario(self, username):
        """
        Obtiene los datos de un usuario específico.
        Se utiliza durante el proceso de autenticación.
        """
        self.cursor.execute("""
            SELECT username, password_hash, salt
            FROM usuarios
            WHERE username = ?
        """, (username,))
        return self.cursor.fetchone()  # Retorna una fila o None

    def insertar_indicador(self, nombre, fecha_indicador, valor, fecha_consulta, usuario, proveedor):
        """
        Guarda en la base de datos un indicador económico consultado.
        """
        self.cursor.execute("""
            INSERT INTO indicadores
            (nombre_indicador, fecha_indicador, valor, fecha_consulta, usuario, proveedor)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nombre, fecha_indicador, valor, fecha_consulta, usuario, proveedor))
        self.connection.commit()
