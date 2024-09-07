from usuarios import registrar_usuario
from recursos import RecursosUsuario
from database import conectar_base_datos, registrar_isla_virtual, cerrar_conexion
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
from blockchain import Blockchain
from almacenamiento import IslaVirtual3D
from flask import render_template

blockchain = Blockchain()

def inicializar_recursos():
    try:
        return RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda
    except Exception as e:
        print(f"Error al inicializar recursos: {e}")
        return None

def conectar_bd():
    try:
        return conectar_base_datos()
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_usuario(nombre, contraseña):
    try:
        registrar_usuario(nombre, contraseña)
    except Exception as e:
        print(f"Error al crear usuario: {e}")

def comprimir_datos(datos, archivo):
    try:
        comprimir_y_guardar_datos(datos, archivo)
    except Exception as e:
        print(f"Error al comprimir datos: {e}")

def descomprimir_datos(archivo):
    try:
        return cargar_y_descomprimir_datos(archivo)
    except Exception as e:
        print(f"Error al descomprimir datos: {e}")
        return None

def procesar_transaccion(blockchain, transaccion):
    try:
        blockchain.agregar_bloque(transaccion)
    except Exception as e:
        print(f"Error al procesar transacción: {e}")

def iniciar_servidor():
    try:
        socketio.run(app, debug=True)
    except Exception as e:
        print(f"Error al iniciar el servidor: {e}")

def mostrar_isla_virtual():
    try:
        isla = IslaVirtual3D()
        isla.mostrar()
        ubicacion = "100 x 100"
        data = blockchain.agregar_bloque_isla_virtual(ubicacion)
        return data
    except Exception as e:
        print(f"Error al mostrar la isla virtual: {e}")
        return None

@app.route('/')
def index():
    conexion = conectar_bd()
    if conexion:
        try:
            registrar_isla_virtual(conexion, "100 x 100")
        except Exception as e:
            print(f"Error al registrar la isla virtual: {e}")
        finally:
            cerrar_conexion(conexion)
    data = mostrar_isla_virtual()
    return render_template('index.html', data=data)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain, mostrar la isla virtual 3D e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos()
    if recursos_usuario is None:
        print("Error crítico: No se pudieron inicializar los recursos.")
        return

    db = conectar_bd()
    if db is None:
        print("Error crítico: No se pudo conectar a la base de datos.")
        return

    crear_usuario("nombre", "contraseña")

    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    datos_descomprimidos = descomprimir_datos(archivo_comprimido)
    if datos_descomprimidos is None:
        print("Error crítico: No se pudieron descomprimir los datos.")
        return

    blockchain = Blockchain()
    procesar_transaccion(blockchain, "transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
