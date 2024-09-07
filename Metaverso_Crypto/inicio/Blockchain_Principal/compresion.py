import json
import gzip
from blockchain import Blockchain

blockchain = Blockchain()

def comprimir_y_guardar_datos(datos, archivo_salida):
    """
    Comprime y guarda los datos en un archivo.

    Args:
        datos (dict): Datos a comprimir.
        archivo_salida (str): Ruta del archivo de salida.
    """
    try:
        # Serializar y comprimir los datos
        datos_serializados = json.dumps(datos).encode('utf-8')
        datos_comprimidos = gzip.compress(datos_serializados)
        
        # Guardar los datos comprimidos en el archivo
        with open(archivo_salida, 'wb') as archivo:
            archivo.write(datos_comprimidos)
        
        print(f"Datos comprimidos y guardados en {archivo_salida}")
        
        # Agregar un bloque a la blockchain
        blockchain.agregar_bloque(f"Datos comprimidos guardados en {archivo_salida}")
    except Exception as e:
        print(f"Error al comprimir y guardar datos: {e}")

def cargar_y_descomprimir_datos(archivo_entrada):
    """
    Carga y descomprime los datos de un archivo.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada.

    Returns:
        dict: Datos descomprimidos.
    """
    try:
        # Leer y descomprimir los datos del archivo
        with open(archivo_entrada, 'rb') as archivo:
            datos_comprimidos = archivo.read()
        datos_descomprimidos = gzip.decompress(datos_comprimidos)
        
        # Agregar un bloque a la blockchain
        blockchain.agregar_bloque(f"Datos descomprimidos desde {archivo_entrada}")
        
        return json.loads(datos_descomprimidos)
    except Exception as e:
        print(f"Error al cargar y descomprimir datos: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    datos = {"nombre": "ejemplo", "valor": 123}
    archivo = "datos_comprimidos.gz"
    
    comprimir_y_guardar_datos(datos, archivo)
    datos_cargados = cargar_y_descomprimir_datos(archivo)
    print(datos_cargados)
