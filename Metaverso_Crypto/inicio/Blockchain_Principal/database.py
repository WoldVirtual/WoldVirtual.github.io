import psycopg2
from psycopg2 import sql
from blockchain import Blockchain

blockchain = Blockchain()

def conectar_base_datos():
    """
    Conecta a la base de datos PostgreSQL y devuelve la conexión.

    Returns:
        conexion: Objeto de conexión a la base de datos.
    """
    try:
        conexion = psycopg2.connect(
            database="tu_base_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="tu_host",
            port="tu_puerto"
        )
        print("Conexión a la base de datos establecida.")
        return conexion
    except psycopg2.DatabaseError as e:
        print(f"Error en la conexión a la base de datos: {e}")
        return None

def obtener_usuarios(conexion):
    """
    Obtiene todos los usuarios de la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.

    Returns:
        list: Lista de usuarios.
    """
    try:
        with conexion.cursor() as cursor:
            cursor.execute(sql.SQL("SELECT * FROM {}").format(sql.Identifier('usuarios')))
            resultados = cursor.fetchall()
            return resultados
    except psycopg2.DatabaseError as e:
        print(f"Error al obtener usuarios: {e}")
        return []

def cerrar_conexion(conexion):
    """
    Cierra la conexión a la base de datos.

    Args:
        conexion: Objeto de conexión a la base de datos.
    """
    if conexion:
        conexion.close()
        print("Conexión cerrada.")

def registrar_isla_virtual(conexion, ubicacion):
    """
    Registra la información de la isla virtual 3D en la base de datos y agrega un bloque a la blockchain.

    Args:
        conexion: Objeto de conexión a la base de datos.
        ubicacion (str): Ubicación de la isla virtual 3D.
    """
    try:
        with conexion.cursor() as cursor:
            cursor.execute(
                sql.SQL("INSERT INTO {} (ubicacion) VALUES (%s)").format(sql.Identifier('islas_virtuales')),
                [ubicacion]
            )
            conexion.commit()
            print(f"Isla virtual 3D registrada en la ubicación {ubicacion}.")
            
            # Agregar un bloque a la blockchain
            blockchain.agregar_bloque(f"Isla virtual 3D registrada en la ubicación {ubicacion}")
    except psycopg2.DatabaseError as e:
        print(f"Error al registrar la isla virtual 3D: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    conexion = conectar_base_datos()
    if conexion:
        usuarios = obtener_usuarios(conexion)
        for usuario in usuarios:
            print(usuario)
        
        registrar_isla_virtual(conexion, "100 x 100")
        
        cerrar_conexion(conexion)
