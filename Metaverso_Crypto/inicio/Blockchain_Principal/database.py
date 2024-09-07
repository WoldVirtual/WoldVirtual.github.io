import mysql.connector
from blockchain import Blockchain

blockchain = Blockchain()

def conectar_base_datos():
    try:
        conexion = mysql.connector.connect(
            host="tu_host",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_datos"
        )
        print("Conexión a la base de datos establecida.")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error en la conexión a la base de datos: {e}")
        blockchain.agregar_bloque(f"Error en la conexión a la base de datos: {e}")
        return None

def obtener_usuarios(conexion):
    try:
        cursor = conexion.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()
        cursor.close()
        return resultados
    except mysql.connector.Error as e:
        print(f"Error al obtener usuarios: {e}")
        blockchain.agregar_bloque(f"Error al obtener usuarios: {e}")
        return []

def cerrar_conexion(conexion):
    if conexion:
        try:
            conexion.close()
            print("Conexión cerrada.")
        except mysql.connector.Error as e:
            print(f"Error al cerrar la conexión: {e}")
            blockchain.agregar_bloque(f"Error al cerrar la conexión: {e}")

def registrar_isla_virtual(conexion, ubicacion):
    try:
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO islas_virtuales (ubicacion) VALUES (%s)", (ubicacion,))
        conexion.commit()
        cursor.close()
        print(f"Isla virtual 3D registrada en la ubicación {ubicacion}.")
        blockchain.agregar_bloque(f"Isla virtual 3D registrada en la ubicación {ubicacion}")
    except mysql.connector.Error as e:
        print(f"Error al registrar la isla virtual 3D: {e}")
        blockchain.agregar_bloque(f"Error al registrar la isla virtual 3D: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    conexion = conectar_base_datos()
    if conexion:
        usuarios = obtener_usuarios(conexion)
        for usuario in usuarios:
            print(usuario)
        
        registrar_isla_virtual(conexion, "100 x 100")
        cerrar_conexion(conexion)
