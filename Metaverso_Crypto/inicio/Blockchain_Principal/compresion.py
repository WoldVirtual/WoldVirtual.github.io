import json
import gzip
from blockchain import Blockchain
import pythreejs as p3
import psutil  # Para verificar la RAM disponible

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

class IslaVirtual3D:
    def __init__(self):
        self.scene = p3.Scene()
        self.camera = p3.PerspectiveCamera(position=[10, 10, 10], up=[0, 1, 0], children=[
            p3.DirectionalLight(color='white', position=[3, 5, 1], intensity=0.5)
        ])
        self.renderer = p3.Renderer(camera=self.camera, scene=self.scene, controls=[p3.OrbitControls(controlling=self.camera)])
        self.crear_isla()
        self.crear_agua()

    def crear_isla(self):
        # Verificar la RAM disponible
        ram_disponible = psutil.virtual_memory().available / (1024 ** 2)  # Convertir a MB
        if ram_disponible < 200:  # Ajustar según sea necesario
            print("Advertencia: RAM disponible baja, creando isla con menos detalles.")
            island_geometry = p3.CylinderGeometry(radiusTop=5, radiusBottom=5, height=2, radialSegments=8)
        else:
            island_geometry = p3.CylinderGeometry(radiusTop=5, radiusBottom=5, height=2)
        
        island_material = p3.MeshBasicMaterial(color='green')
        island = p3.Mesh(geometry=island_geometry, material=island_material)
        self.scene.add(island)

    def crear_agua(self):
        water_geometry = p3.PlaneGeometry(width=20, height=20)
        water_material = p3.MeshBasicMaterial(color='blue', opacity=0.5, transparent=True)
        water = p3.Mesh(geometry=water_geometry, material=water_material)
        water.position.y = -1  # Colocar el agua debajo de la isla
        self.scene.add(water)

    def mostrar(self):
        display(self.renderer)

# Ejemplo de uso
if __name__ == "__main__":
    datos = {"nombre": "ejemplo", "valor": 123}
    archivo = "datos_comprimidos.gz"
    
    comprimir_y_guardar_datos(datos, archivo)
    datos_cargados = cargar_y_descomprimir_datos(archivo)
    print(datos_cargados)
    
    # Mostrar la isla virtual 3D
    isla = IslaVirtual3D()
    isla.mostrar()
