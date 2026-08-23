from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante import Restaurante

OPCIONES_MENU = (
    ("1", "Registrar producto"),
    ("2", "Buscar producto"),
    ("3", "Actualizar producto"),
    ("4", "Eliminar producto"),
    ("5", "Listar productos"),
    ("6", "Registrar usuario"),
    ("7", "Buscar usuario"),
    ("8", "Actualizar usuario"),
    ("9", "Eliminar usuario"),
    ("10", "Listar usuarios"),
    ("11", "Listar categorias activas"),
    ("0", "Salir"),
)


def pedir_texto(mensaje: str) -> str:
    return input(mensaje).strip()


def mostrar_menu() -> None:
    print("\n===== RESTAURANTE APP =====")
    for numero, descripcion in OPCIONES_MENU:
        print(f"{numero}. {descripcion}")


def guardar_productos(archivo_servicio: ArchivoServicio, restaurante: Restaurante) -> None:
    guardado = archivo_servicio.guardar_productos(restaurante.listar_objetos_productos())
    if not guardado:
        print("Los cambios no pudieron guardarse en el archivo.")


def registrar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Registrar producto ---")
    codigo_raw = pedir_texto("Codigo: ")
    nombre = pedir_texto("Nombre: ")
    precio_raw = pedir_texto("Precio: ")
    categoria = pedir_texto("Categoria: ")

    try:
        codigo = Producto.validar_codigo(codigo_raw)
        precio = Producto.validar_precio(precio_raw)
        producto = Producto(codigo, nombre, precio, categoria)
        registrado = restaurante.registrar_producto(producto)

        if registrado:
            print("Producto registrado correctamente.")
            guardar_productos(archivo_servicio, restaurante)
        else:
            print("El codigo ya se encuentra registrado.")
    except ValueError as error:
        print(error)


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")
    codigo = pedir_texto("Codigo del producto: ")
    producto = restaurante.buscar_producto(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto)


def actualizar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Actualizar producto ---")
    codigo = pedir_texto("Codigo del producto: ")

    if restaurante.buscar_producto(codigo) is None:
        print("Producto no encontrado.")
        return

    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nuevo_precio_raw = pedir_texto("Nuevo precio: ")
    nueva_categoria = pedir_texto("Nueva categoria: ")

    try:
        nuevo_precio = Producto.validar_precio(nuevo_precio_raw)
        actualizado = restaurante.actualizar_producto(
            codigo, nuevo_nombre, nuevo_precio, nueva_categoria
        )

        if actualizado:
            print("Producto actualizado correctamente.")
            guardar_productos(archivo_servicio, restaurante)
        else:
            print("Producto no encontrado.")
    except ValueError as error:
        print(error)


def eliminar_producto(restaurante: Restaurante, archivo_servicio: ArchivoServicio) -> None:
    print("\n--- Eliminar producto ---")
    codigo = pedir_texto("Codigo del producto: ")
    eliminado = restaurante.eliminar_producto(codigo)

    if eliminado:
        print("Producto eliminado correctamente.")
        guardar_productos(archivo_servicio, restaurante)
    else:
        print("Producto no encontrado.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de productos ---")
    productos = restaurante.listar_productos()

    if len(productos) == 0:
        print("No hay productos registrados.")
        return

    for indice, descripcion in enumerate(productos):
        print(f"{indice + 1}. {descripcion}")

    print(f"\nTotal de productos: {restaurante.contar_productos()}")


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")
    identificacion = pedir_texto("Identificacion: ")
    nombre = pedir_texto("Nombre: ")
    rol = pedir_texto("Rol (administrador / cajero / cocinero): ")

    try:
        usuario = Usuario(identificacion, nombre, rol)
        registrado = restaurante.registrar_usuario(usuario)

        if registrado:
            print("Usuario registrado correctamente.")
        else:
            print("La identificacion ya se encuentra registrada.")
    except ValueError as error:
        print(error)


def buscar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Buscar usuario ---")
    identificacion = pedir_texto("Identificacion del usuario: ")
    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("Usuario no encontrado.")
    else:
        print(usuario)


def actualizar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Actualizar usuario ---")
    identificacion = pedir_texto("Identificacion del usuario: ")

    if restaurante.buscar_usuario(identificacion) is None:
        print("Usuario no encontrado.")
        return

    nuevo_nombre = pedir_texto("Nuevo nombre: ")
    nuevo_rol = pedir_texto("Nuevo rol (administrador / cajero / cocinero): ")

    try:
        actualizado = restaurante.actualizar_usuario(identificacion, nuevo_nombre, nuevo_rol)

        if actualizado:
            print("Usuario actualizado correctamente.")
        else:
            print("Usuario no encontrado.")
    except ValueError as error:
        print(error)


def eliminar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Eliminar usuario ---")
    identificacion = pedir_texto("Identificacion del usuario: ")
    eliminado = restaurante.eliminar_usuario(identificacion)

    if eliminado:
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de usuarios ---")
    usuarios = restaurante.listar_usuarios()

    if len(usuarios) == 0:
        print("No hay usuarios registrados.")
        return

    for indice, descripcion in enumerate(usuarios):
        print(f"{indice + 1}. {descripcion}")


def listar_categorias_activas(restaurante: Restaurante) -> None:
    print("\n--- Categorias con productos registrados ---")
    categorias = restaurante.obtener_categorias_unicas()

    if len(categorias) == 0:
        print("No hay categorias activas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def ejecutar_menu() -> None:
    ruta_productos = Path(__file__).resolve().parent / "datos" / "productos.json"
    archivo_servicio = ArchivoServicio(str(ruta_productos))
    restaurante = Restaurante(archivo_servicio.cargar_productos())

    opciones: dict = {
        "1": lambda: registrar_producto(restaurante, archivo_servicio),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante, archivo_servicio),
        "4": lambda: eliminar_producto(restaurante, archivo_servicio),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante),
        "7": lambda: buscar_usuario(restaurante),
        "8": lambda: actualizar_usuario(restaurante),
        "9": lambda: eliminar_usuario(restaurante),
        "10": lambda: listar_usuarios(restaurante),
        "11": lambda: listar_categorias_activas(restaurante),
    }

    while True:
        mostrar_menu()
        opcion = pedir_texto("Seleccione una opcion: ")

        if opcion == "0":
            print("Gracias por usar Restaurante App.")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("Opcion invalida.")
        else:
            accion()


if __name__ == "__main__":
    ejecutar_menu()
