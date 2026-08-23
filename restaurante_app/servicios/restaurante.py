from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    def __init__(self, productos_iniciales: list[Producto] | None = None) -> None:
        self._productos: list[Producto] = productos_iniciales.copy() if productos_iniciales else []
        self._usuarios: list[Usuario] = []
        self._categorias_activas: set[str] = set()
        self._actualizar_categorias()

    def _actualizar_categorias(self) -> None:
        self._categorias_activas = {p.categoria for p in self._productos}

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = productos.copy()
        self._actualizar_categorias()

    def registrar_producto(self, producto: Producto) -> bool:
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        self._categorias_activas.add(producto.categoria)
        return True

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip().upper()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nuevo_precio: float,
        nueva_categoria: str,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        producto.nombre = nuevo_nombre
        producto.precio = nuevo_precio
        producto.categoria = nueva_categoria
        self._actualizar_categorias()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        self._actualizar_categorias()
        return True

    def listar_productos(self) -> list[str]:
        return [str(p) for p in self._productos]

    def listar_objetos_productos(self) -> list[Producto]:
        return self._productos.copy()

    def contar_productos(self) -> int:
        return len(self._productos)

    def obtener_categorias_unicas(self) -> set[str]:
        return self._categorias_activas.copy()

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self.buscar_usuario(usuario.identificacion) is not None:
            return False
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Usuario | None:
        identificacion = identificacion.strip()
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def actualizar_usuario(self, identificacion: str, nuevo_nombre: str, nuevo_rol: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        usuario.nombre = nuevo_nombre
        usuario.rol = nuevo_rol
        return True

    def eliminar_usuario(self, identificacion: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        self._usuarios.remove(usuario)
        return True

    def listar_usuarios(self) -> list[str]:
        return [str(u) for u in self._usuarios]
