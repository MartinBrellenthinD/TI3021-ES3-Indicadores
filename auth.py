import hashlib
import os

class AuthService:
    """
    Clase encargada de la seguridad de contraseñas.
    Aplica hash seguro y validación.
    """

    @staticmethod
    def generar_salt():
        """
        Genera una salt aleatoria para cada usuario.
        """
        return os.urandom(16)

    @staticmethod
    def generar_hash(password, salt):
        """
        Genera el hash de una contraseña usando PBKDF2 + SHA256.
        """
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt,
            100000
        ).hex()

    @staticmethod
    def verificar(password, salt, hash_guardado):
        """
        Verifica si la contraseña ingresada coincide con el hash almacenado.
        """
        return AuthService.generar_hash(password, salt) == hash_guardado
