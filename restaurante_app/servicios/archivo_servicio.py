import json
from pathlib import Path

from modelos.producto import Producto


class ArchivoServicio:
    def __init__(self, ruta_productos: str = "datos/productos.json") -> None:
        self._ruta_productos = Path(ruta_productos)

    def cargar_productos(self) -> list[Producto]:
        try:
            with open(self._ruta_productos, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("El archivo de productos no contiene un formato JSON valido.")
            return []
        except PermissionError:
            print("No hay permisos suficientes para leer el archivo de productos.")
            return []

        if not isinstance(datos, list):
            print("El archivo de productos debe contener una lista de registros.")
            return []

        productos: list[Producto] = []
        for registro in datos:
            if not isinstance(registro, dict):
                print("Se encontro un registro con formato invalido y fue omitido.")
                continue

            try:
                producto = Producto(
                    registro["codigo"],
                    registro["nombre"],
                    registro["precio"],
                    registro["categoria"],
                )
                productos.append(producto)
            except KeyError:
                print("Se encontro un registro incompleto y fue omitido.")
            except ValueError as error:
                print(f"Se encontro un producto con datos invalidos: {error}")

        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        datos = [producto.convertir_a_diccionario() for producto in productos]

        try:
            self._ruta_productos.parent.mkdir(parents=True, exist_ok=True)
            with open(self._ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print("No hay permisos suficientes para guardar el archivo de productos.")
            return False
