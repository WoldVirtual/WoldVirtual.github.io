import hashlib
from blockchain import Blockchain

# Diccionario para almacenar usuarios y contraseñas
usuarios = {}
blockchain = Blockchain()

def registrar_usuario(username, password):
    """
    Registra un nuevo usuario con una contraseña encriptada.

    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.

    Raises:
        ValueError: Si el usuario ya existe.
    """
    try:
        if username in usuarios:
            raise ValueError("El usuario ya existe.")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        usuarios[username] = hashed_password
        print(f"Usuario {username} registrado con éxito.")
        blockchain.agregar_bloque(f"Usuario {username} registrado")
    except ValueError as e:
        print(f"Error al registrar usuario: {e}")
    except Exception as e:
        print(f"Error inesperado al registrar usuario: {e}")

def verificar_credenciales(username, password):
    """
    Verifica las credenciales del usuario.

    Args:
        username (str): Nombre de usuario.
        password (str): Contraseña del usuario.

    Returns:
        bool: True si las credenciales son correctas, False en caso contrario.
    """
    try:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return usuarios.get(username) == hashed_password
    except Exception as e:
        print(f"Error al verificar credenciales: {e}")
        return False

def manejar_accion(usuario, accion):
    """
    Maneja las acciones del usuario.

    Args:
        usuario (str): Nombre del usuario.
        accion (str): Acción a realizar.

    Raises:
        ValueError: Si la acción no es reconocida.
    """
    try:
        acciones = {
            "explorar": f"Bienvenido/a {usuario} al entorno de exploración.",
            "intercambiar": f"Realizando intercambio para {usuario}.",
            "isla_virtual": f"Usuario {usuario} está cargando la isla virtual 3D."
        }
        accion_mensaje = acciones.get(accion, "Acción no reconocida.")
        print(accion_mensaje)
        if accion == "isla_virtual":
            blockchain.agregar_bloque(f"Usuario {usuario} cargó la isla virtual 3D en la ubicación 100 x 100")
        if accion_mensaje == "Acción no reconocida.":
            raise ValueError(accion_mensaje)
    except ValueError as e:
        print(f"Error al manejar acción: {e}")
    except Exception as e:
        print(f"Error inesperado al manejar acción: {e}")

# Ejemplo de uso
if __name__ == "__main__":
    try:
        registrar_usuario("nombre", "contraseña")
        if verificar_credenciales("nombre", "contraseña"):
            manejar_accion("nombre", "explorar")
            manejar_accion("nombre", "isla_virtual")
        else:
            print("Credenciales incorrectas.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Error inesperado: {e}")
                                                 
