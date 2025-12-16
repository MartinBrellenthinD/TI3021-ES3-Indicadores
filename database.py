import sqlite3

class Database:
    """
    Clase encargada de manejar la conexión a la base de datos
    y todas las operaciones relacionadas con ella.
    """

    def __init__(self, db_name="indicadores.db"):
        # Se crea la conexión a la base de datos SQLite
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

        # Al iniciar la aplicación, se crean automáticamente las tablas
        self.crear_tablas()

    def crear_tablas(self):
        """
        Crea las tablas necesarias si no existen.
        Esto evita tener que ejecutar scripts SQL manualmente.
        """
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            salt BLOB NOT NULL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS indicadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            fecha_indicador TEXT NOT NULL,
            valor REAL NOT NULL,
            fecha_consulta TEXT NOT NULL,
            usuario TEXT NOT NULL,
            proveedor TEXT NOT NULL
        )
        """)
        self.connection.commit()

    def insertar(self, query, params):
        """
        Método genérico para operaciones tipo POST (INSERT).
        """
        self.cursor.execute(query, params)
        self.connection.commit()

    def ejecutar(self, query, params):
        """
        Método genérico para operaciones PUT (UPDATE) y DELETE.
        """
        self.cursor.execute(query, params)
        self.connection.commit()

    def obtener(self, query, params=()):
        """
        Método para obtener información desde la base de datos (GET).
        """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()


