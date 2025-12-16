from database import Database
from auth import AuthService
from services import UsuarioService, IndicadorService
from models import Indicador
from datetime import datetime
import requests
import getpass  # Librería para ocultar la contraseña al escribirla

# Inicialización de las capas del sistema
db = Database()
auth = AuthService()
usuario_service = UsuarioService(db, auth)
indicador_service = IndicadorService(db)

def menu():
    """
    Muestra el menú principal del sistema.
    """
    print("\n1. Crear usuario (POST)")
    print("2. Consultar indicador y guardar (POST)")
    print("3. Actualizar indicador (PUT)")
    print("4. Eliminar indicador (DELETE)")
    print("5. Salir")

while True:
    menu()
    opcion = input("Seleccione opción: ")

    if opcion == "1":
        # Registro de usuario
        usuario = input("Usuario: ")

        # La contraseña NO se muestra en pantalla al escribirla
        password = getpass.getpass("Contraseña: ")

        usuario_service.crear_usuario(usuario, password)
        print("Usuario creado correctamente.")

    elif opcion == "2":
        # Consulta de indicador económico
        indicador = input("Indicador (uf, ipc, utm, dolar, euro): ")
        fecha = input("Fecha (dd-mm-aaaa): ")

        url = f"https://mindicador.cl/api/{indicador}/{fecha}"
        data = requests.get(url).json()['serie'][0]

        indicador_obj = Indicador(
            indicador,
            data['fecha'],
            data['valor'],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "admin",
            "mindicador.cl"
        )

        indicador_service.registrar_indicador(indicador_obj)
        print("Indicador registrado.")

    elif opcion == "3":
        # Actualización de indicador (PUT)
        id_ind = input("ID del indicador: ")
        nuevo_valor = input("Nuevo valor: ")
        indicador_service.actualizar_valor(id_ind, nuevo_valor)
        print("Indicador actualizado.")

    elif opcion == "4":
        # Eliminación de indicador (DELETE)
        id_ind = input("ID del indicador: ")
        indicador_service.eliminar_indicador(id_ind)
        print("Indicador eliminado.")

    elif opcion == "5":
        # Salida del sistema
        print("Saliendo del sistema...")
        break
