import requests

class IndicadorEconomico:
    def __init__(self):
        # Servicio externo público
        self.url_base = "https://mindicador.cl/api"
        self.proveedor = "mindicador.cl"

    def obtener_indicador(self, codigo_indicador):
        """
        Consulta un indicador económico desde un servicio externo.
        La respuesta se recibe en formato JSON y se deserializa.
        """
        try:
            response = requests.get(
                f"{self.url_base}/{codigo_indicador}",
                timeout=5
            )

            # Se valida que la respuesta sea correcta
            response.raise_for_status()

            data = response.json()

            # Se extrae solo la información necesaria
            return {
                "nombre": data["nombre"],
                "fecha": data["serie"][0]["fecha"],
                "valor": data["serie"][0]["valor"]
            }

        except requests.exceptions.Timeout:
            print("Tiempo de espera agotado al consultar la API.")
        except requests.exceptions.RequestException as error:
            print("Error al consumir la API:", error)

        return None

