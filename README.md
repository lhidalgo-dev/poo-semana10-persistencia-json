# Restaurante App — Semana 10

**Estudiante:** Leython Josue Hidalgo Valdez  
**Asignatura:** Programacion Orientada a Objetos  
**Tema:** Manejo de archivos, excepciones y persistencia JSON  

---

## Descripcion del sistema

Aplicacion de consola que administra productos y usuarios de un restaurante. Desde la Semana 10 los productos se conservan en un archivo JSON, de modo que al cerrar y volver a ejecutar el programa la informacion sigue disponible sin necesidad de volver a ingresarla.

---

## Estructura del proyecto

```text
restaurante_app/
|
|-- datos/
|   `-- productos.json
|
|-- modelos/
|   |-- __init__.py
|   |-- producto.py
|   `-- usuario.py
|
|-- servicios/
|   |-- __init__.py
|   |-- archivo_servicio.py
|   `-- restaurante.py
|
|-- main.py
`-- README.md
```

La carpeta `datos/` no representa una nueva capa de la arquitectura. Es unicamente la ubicacion donde se guarda `productos.json`.

---

## Responsabilidades de cada componente

- **`modelos/producto.py`**: clase `Producto` con validaciones de codigo, nombre, precio y categoria. Incluye `convertir_a_diccionario()` para preparar el objeto antes de guardarlo en JSON.
- **`modelos/usuario.py`**: clase `Usuario` con validaciones de identificacion, nombre y rol. Su informacion permanece en memoria durante la ejecucion.
- **`servicios/restaurante.py`**: clase `Restaurante` que administra las colecciones de productos y usuarios, y expone las operaciones de registro, busqueda, actualizacion y eliminacion.
- **`servicios/archivo_servicio.py`**: clase `ArchivoServicio` que centraliza la lectura y escritura de `datos/productos.json` usando `with open()`, `json.load()` y `json.dump()`.
- **`main.py`**: crea los servicios, carga los productos al iniciar, coordina el menu y solicita el guardado despues de cada operacion que modifique la coleccion.

---

## Persistencia con JSON

### Como funciona productos.json

El archivo almacena una lista de diccionarios. Cada diccionario representa un objeto `Producto` con sus cuatro campos: `codigo`, `nombre`, `precio` y `categoria`. Durante la ejecucion el programa trabaja exclusivamente con objetos; el archivo solo interviene al inicio y al guardar cambios.

### Flujo de carga

```text
Inicio de la aplicacion
        |
main.py crea ArchivoServicio
        |
Se intenta leer datos/productos.json
        |
json.load() recupera la lista de diccionarios
        |
Cada registro valido se convierte en Producto(...)
        |
Los objetos se entregan a Restaurante
        |
El menu trabaja normalmente con objetos Producto
```

### Flujo de guardado

```text
Usuario registra, actualiza o elimina un producto
        |
main.py solicita la operacion al servicio Restaurante
        |
Restaurante modifica la coleccion en memoria
        |
Los objetos Producto se convierten a diccionarios
        |
ArchivoServicio utiliza json.dump()
        |
Se actualiza datos/productos.json
```

---

## Excepciones controladas

| Excepcion | Situacion |
|---|---|
| `FileNotFoundError` | `productos.json` no existe en el primer inicio; el programa arranca con lista vacia |
| `json.JSONDecodeError` | El archivo existe pero su contenido no es JSON valido |
| `PermissionError` | No hay permisos suficientes para leer o escribir el archivo |
| `KeyError` | Un registro del JSON no contiene alguna de las claves esperadas; el registro se omite |
| `ValueError` | Datos invalidos en campos de `Producto` o precio no numerico; el registro se omite |

No se utilizan capturas genericas ni `except: pass`. Cada excepcion responde a una situacion concreta del programa.

---

## Categorias validas de producto

`entrada`, `plato_principal`, `postre`, `bebida`, `complemento`

---

## Instrucciones para ejecutar

Desde la carpeta `restaurante_app`, ejecutar:

```bash
python main.py
```

El programa carga automaticamente los productos guardados en `datos/productos.json`. Si el archivo no existe, inicia con la lista vacia.

---

## Menu principal

```
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Buscar usuario
8. Actualizar usuario
9. Eliminar usuario
10. Listar usuarios
11. Listar categorias activas
0. Salir
```

---

## Comprobacion de persistencia realizada

1. Se ejecuto `main.py` y se registraron tres productos desde el menu.
2. Se verifico que `datos/productos.json` contenia los registros correctamente escritos.
3. Se cerro completamente el programa.
4. Se ejecuto nuevamente `main.py` y se listo los productos: los tres registros anteriores aparecieron sin necesidad de volver a ingresarlos.
5. Se actualizo el precio de un producto, se cerro el programa y se volvio a ejecutar: el cambio persistio correctamente.
6. Se elimino un producto, se cerro el programa y se volvio a ejecutar: el producto eliminado ya no aparecio en la lista.

---

## Uso de estructuras de datos

- **`list`**: `Restaurante` utiliza listas para almacenar productos y usuarios durante la ejecucion.
- **`tuple`**: `main.py` define las opciones del menu como tupla, ya que no cambian durante la ejecucion.
- **`dict`**: `main.py` relaciona cada opcion con su funcion correspondiente; `convertir_a_diccionario()` produce el diccionario que se guarda en JSON.
- **`set`**: `Restaurante` mantiene el conjunto de categorias activas para responder consultas sin recorrer toda la lista cada vez.
