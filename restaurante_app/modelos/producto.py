class Producto:
    def __init__(self, codigo: str, nombre: str, precio: float, categoria: str) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El codigo no puede estar vacio.")
        self._codigo = valor.strip().upper()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if not isinstance(valor, (int, float)):
            raise ValueError("El precio debe ser un valor numerico.")
        if valor <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = round(float(valor), 2)

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La categoria no puede estar vacia.")
        self._categoria = valor.strip().lower()

    @staticmethod
    def validar_codigo(codigo: str) -> str:
        if not codigo or not codigo.strip():
            raise ValueError("El codigo no puede estar vacio.")
        limpio = codigo.strip().upper()
        if not limpio.isalnum():
            raise ValueError("El codigo solo puede contener letras y numeros.")
        return limpio

    @staticmethod
    def validar_precio(valor: str) -> float:
        try:
            numero = float(valor)
        except ValueError:
            raise ValueError("El precio ingresado no es un numero valido.")
        if numero <= 0:
            raise ValueError("El precio debe ser mayor a cero.")
        return round(numero, 2)

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "precio": self.precio,
            "categoria": self.categoria,
        }

    def __str__(self) -> str:
        return (
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | Categoria: {self.categoria}"
        )
