# módulo app #

from usuarios import registrar_usuario
from recursos import RecursosUsuario
from blockchain import Blockchain, Bloque
from database import conectar_base_datos, insertar_bloque, obtener_bloques, insertar_transaccion, obtener_transacciones, cerrar_conexion
from almacenamiento import comprimir_y_guardar_datos, cargar_y_descomprimir_datos, eliminar_archivo, listar_archivos, mover_archivo
from servidor import app, socketio
import time

def inicializar_recursos(cpu: int = 50, ancho_banda: int = 50):
    """
    Inicializa los recursos asignados a un usuario y devuelve los recursos asignados.
    """
    recursos_usuario = RecursosUsuario(cpu, ancho_banda)
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 100}
    recursos_asignados = recursos_usuario.asignar_recursos(recursos_comunitarios)
    return recursos_asignados

def procesar_transacciones(datos_usuario, blockchain):
    """
    Procesa las transacciones de usuario en la cadena de bloques.
    """
    blockchain.agregar_bloque(datos_usuario)

def gestionar_compresion(datos_usuario, archivo_comprimido):
    """
    Comprime y descomprime los datos del usuario para su almacenamiento.
    """
    comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)
    datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
    return datos_descomprimidos

def main():
    """
    Función principal para ejecutar la aplicación.
    """
    try:
        # Inicializar recursos
        recursos_asignados = inicializar_recursos()

        # Conectar a la base de datos
        conexion = conectar_base_datos()

        # Registrar un nuevo usuario
        registrar_usuario("nombre", "contraseña")

        # Proceso de compresión y almacenamiento
        datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
        archivo_comprimido = "datos_comprimidos.gz"
        comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)
        
        # Listar archivos en el directorio actual
        listar_archivos('.')

        # Cargar y descomprimir datos
        datos_descomprimidos = cargar_y_descomprimir_datos(archivo_comprimido)
        
        # Inicializar blockchain y agregar bloque
        blockchain = Blockchain()
        nuevo_bloque = Bloque(len(blockchain.cadena), time.time(), datos_usuario, blockchain.cadena[-1].hash)
        blockchain.agregar_bloque(nuevo_bloque)

        # Guardar el bloque en la base de datos
        insertar_bloque(conexion, nuevo_bloque)

        # Manejo de transacciones
        insertar_transaccion(conexion, "Usuario1", "Usuario2", 100)
        transacciones = obtener_transacciones(conexion)
        print(f"Transacciones almacenadas: {transacciones}")

        # Cerrar la conexión a la base de datos
        cerrar_conexion(conexion)

        # Iniciar el servidor
        socketio.run(app, debug=True)

    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()

# modulo app #

# from usuarios import registrar_usuario
# from recursos import RecursosUsuario
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from servidor import app, socketio

# def inicializar_recursos(cpu, ancho_banda):
   # return RecursosUsuario(cpu, ancho_banda)

# def conectar_bd():
    # return conectar_base_datos()

# def crear_usuario(nombre, contraseña):
   # registrar_usuario(nombre, contraseña)

# def comprimir_datos(datos, archivo):
    # comprimir_y_guardar_datos(datos, archivo)

# def descomprimir_datos(archivo):
   # return cargar_y_descomprimir_datos(archivo)

# def procesar_transaccion(blockchain, transaccion):
   # blockchain.agregar_bloque(transaccion)

# def iniciar_servidor():
   # socketio.run(app, debug=True)

# def main():
   # """
  #  Función principal para inicializar recursos, conectar a la base de datos,
  #  registrar un usuario, comprimir y almacenar datos, procesar transacciones
   # en la blockchain e iniciar el servidor.
  #  """
   # recursos_usuario = inicializar_recursos(50, 50)
  #  db = conectar_bd()
   # crear_usuario("nombre", "contraseña")

   # datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
   # archivo_comprimido = "datos_comprimidos.gz"
   # comprimir_datos(datos_usuario, archivo_comprimido)

  #  datos_descomprimidos = descomprimir_datos(archivo_comprimido)

   # blockchain = Blockchain()
  #  procesar_transaccion(blockchain, "transaccion_ejemplo")

   # iniciar_servidor()

# if __name__ == "__main__":
  #  main()

# app.py
# from usuarios import registrar_usuario, verificar_credenciales, manejar_accion
# from recursos import RecursosUsuario, MonitoreoRecursos
# from blockchain import Blockchain
# from database import conectar_base_datos
# from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
# from servidor import app, socketio
# from almacenamiento import compress_files, decompress_file

# def main():
   # """
   # Función principal para inicializar recursos, conectar a la base de datos,
    # registrar un usuario, comprimir y almacenar datos, procesar transacciones
   #  en la blockchain e iniciar el servidor.
  #   """
    # Inicializar recursos
   #  recursos_usuario = RecursosUsuario(50, 50)  # Ejemplo de inicialización con 50% de CPU y ancho de banda

    # Conectar a la base de datos
   #  db = conectar_base_datos()

    # Crear un nuevo usuario
    # registrar_usuario("nombre", "contraseña")

    # Ejecutar compresión de datos
   #  datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
   #  archivo_comprimido = "datos_comprimidos.gz"
   #  comprimir_y_guardar_datos(datos_usuario, archivo_comprimido)

    # Almacenar los datos comprimidos en el sistema de almacenamiento
    # compress_files(["datos_comprimidos.gz"], "datos_comprimidos.tar.gz")

    # Cargar los datos desde el sistema de almacenamiento y descomprimirlos
    # decompress_file("datos_comprimidos.tar.gz")
    datos_descomprimidos = cargar_y_descomprimir_datos("datos_comprimidos.gz")

    # Procesar transacción en la blockchain
   #  blockchain = Blockchain()
   #  blockchain.agregar_bloque("transaccion_ejemplo")

    # Iniciar servidor
    # socketio.run(app, debug=True)

# if __name__ == "__main__":
   #  main()
