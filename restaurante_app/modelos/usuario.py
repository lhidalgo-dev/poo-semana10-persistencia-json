class Usuario:
    def __init__(self, identificacion: str, nombre: str, rol: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.rol = rol

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("La identificacion no puede estar vacia.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacio.")
        self._nombre = valor.strip()

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:
        roles_permitidos = {"administrador", "cajero", "cocinero"}
        if not valor or not valor.strip():
            raise ValueError("El rol no puede estar vacio.")
        normalizado = valor.strip().lower()
        if normalizado not in roles_permitidos:
            raise ValueError(
                f"Rol '{valor}' no valido. Opciones: administrador, cajero, cocinero."
            )
        self._rol = normalizado

    def __str__(self) -> str:
        return (
            f"ID: {self.identificacion} | Nombre: {self.nombre} | Rol: {self.rol}"
        )
