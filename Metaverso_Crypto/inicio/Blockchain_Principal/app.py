from usuarios import registrar_usuario
from recursos import RecursosUsuario
from blockchain import Blockchain
from database import conectar_base_datos
from compresion import comprimir_y_guardar_datos, cargar_y_descomprimir_datos
from servidor import app, socketio
from almacenamiento import IslaVirtual3D
from flask import render_template

blockchain = Blockchain()

def inicializar_recursos(cpu, ancho_banda):
    return RecursosUsuario(cpu, ancho_banda)

def conectar_bd():
    return conectar_base_datos()

def crear_usuario(nombre, contraseña):
    registrar_usuario(nombre, contraseña)

def comprimir_datos(datos, archivo):
    comprimir_y_guardar_datos(datos, archivo)

def descomprimir_datos(archivo):
    return cargar_y_descomprimir_datos(archivo)

def procesar_transaccion(blockchain, transaccion):
    blockchain.agregar_bloque(transaccion)

def iniciar_servidor():
    socketio.run(app, debug=True)

def mostrar_isla_virtual():
    isla = IslaVirtual3D()
    isla.mostrar()
    ubicacion = "100 x 100"
    data = blockchain.agregar_bloque_isla_virtual(ubicacion)
    return data

@app.route('/')
def index():
    data = mostrar_isla_virtual()
    return render_template('index.html', data=data)

def main():
    """
    Función principal para inicializar recursos, conectar a la base de datos,
    registrar un usuario, comprimir y almacenar datos, procesar transacciones
    en la blockchain, mostrar la isla virtual 3D e iniciar el servidor.
    """
    recursos_usuario = inicializar_recursos(50, 50)
    db = conectar_bd()
    crear_usuario("nombre", "contraseña")

    datos_usuario = {"nombre": "nombre", "datos": "datos_ejemplo"}
    archivo_comprimido = "datos_comprimidos.gz"
    comprimir_datos(datos_usuario, archivo_comprimido)

    datos_descomprimidos = descomprimir_datos(archivo_comprimido)

    blockchain = Blockchain()
    procesar_transaccion(blockchain, "transaccion_ejemplo")

    iniciar_servidor()

if __name__ == "__main__":
    main()
    
