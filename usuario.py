import hashlib
import os

class Usuario:
    """
    Clase responsable de la seguridad de las contraseñas.
    Aplica hash y validación segura.
    """

    @staticmethod
    def generar_salt():
        """
        Genera una salt aleatoria para reforzar la seguridad del hash.
        """
        return os.urandom(16)

    @staticmethod
    def generar_hash(password, salt):
        """
        Genera el hash de una contraseña usando PBKDF2 con SHA256.
        """
        return hashlib.pbkdf2_hmac(
            'sha256',          # Algoritmo de hash utilizado
            password.encode(), # La contraseña se transforma a bytes
            salt,              # Salt única para cada usuario
            100000             # Número de iteraciones para mayor seguridad
        ).hex()

    @staticmethod
    def verificar_password(password, salt, hash_guardado):
        """
        Verifica si la contraseña ingresada coincide con el hash almacenado.
        """
        hash_verificado = Usuario.generar_hash(password, salt)
        return hash_verificado == hash_guardado
