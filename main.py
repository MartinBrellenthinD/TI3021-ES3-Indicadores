import requests
from datetime import datetime
from database import Database
from usuario import Usuario
from indicador import IndicadorEconomico

# Se inicializa la base de datos
db = Database()

def registrar_usuario():
    """
    Permite registrar un usuario nuevo en el sistema.
    La contraseña se almacena de forma segura.
    """
    username = input("Usuario: ")
    password = input("Contraseña: ")

    salt = Usuario.generar_salt()
    password_hash = Usuario.generar_hash(password, salt)

    db.insertar_usuario(username, password_hash, salt)
    print("Usuario registrado correctamente.")

def login():
    """
    Permite autenticar a un usuario verificando su contraseña.
    """
    username = input("Usuario: ")
    password = input("Contraseña: ")

    usuario = db.obtener_usuario(username)
    if usuario:
        _, hash_guardado, salt = usuario
        if Usuario.verificar_password(password, salt, hash_guardado):
            print("Autenticación exitosa.")
            return username

    print("Credenciales incorrectas.")
    return None

def consultar_indicador(usuario):
    """
    Consulta un indicador económico desde la API externa
    y permite guardarlo en la base de datos.
    """
    indicador = input("Indicador (uf, ipc, utm, dolar, euro): ")
    fecha = input("Fecha (dd-mm-aaaa): ")

    url = f"https://mindicador.cl/api/{indicador}/{fecha}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la petición fue exitosa

        data = response.json()
        serie = data['serie'][0]

        indicador_obj = IndicadorEconomico.desde_json(indicador, serie)

        guardar = input("¿Desea guardar el indicador? (s/n): ")
        if guardar.lower() == 's':
            db.insertar_indicador(
                indicador_obj.nombre,
                indicador_obj.fecha,
                indicador_obj.valor,
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                usuario,
                "mindicador.cl"
            )
            print("Indicador almacenado correctamente.")

    except Exception as e:
        print("Error al consultar el indicador:", e)

# Menú principal del programa
opcion = input("1. Registrar\n2. Login\nSeleccione opción: ")

if opcion == "1":
    registrar_usuario()
elif opcion == "2":
    usuario_autenticado = login()
    if usuario_autenticado:
        consultar_indicador(usuario_autenticado)
