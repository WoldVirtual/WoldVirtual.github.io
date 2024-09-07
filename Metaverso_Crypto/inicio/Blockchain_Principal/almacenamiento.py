import os
import tarfile
import pythreejs as p3
from IPython.display import display
import psutil  # Para verificar la RAM disponible

storage_path = '/workspaces/WoldVirtual.github.io/Metaverso_Crypto/inicio/Blockchain_Principal/Almacenamiento'

def compress_files(files, output_filename):
    output_filepath = os.path.join(storage_path, output_filename)
    
    for file in files:
        if not os.path.isfile(file):
            print(f"Advertencia: El archivo {file} no existe y no será incluido en la compresión.")
    
    try:
        with tarfile.open(output_filepath, 'w:gz') as tar:
            for file in files:
                if os.path.isfile(file):
                    tar.add(file, arcname=os.path.basename(file))
        print(f'Archivos comprimidos en {output_filename}, guardado en {output_filepath}')
    except Exception as e:
        print(f"Error al comprimir archivos: {e}")

def decompress_file(input_filename):
    input_filepath = os.path.join(storage_path, input_filename)
    
    if not os.path.isfile(input_filepath):
        print(f"Error: El archivo {input_filepath} no existe.")
        return
    
    try:
        with tarfile.open(input_filepath, 'r:gz') as tar:
            tar.extractall(path=storage_path)
        print(f'Archivos descomprimidos en {storage_path}')
    except Exception as e:
        print(f"Error al descomprimir archivos: {e}")

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
        ram_disponible = psutil.virtual_memory().available / (1024 ** 2)
        if ram_disponible < 200:
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
        water.position.y = -1
        self.scene.add(water)

    def mostrar(self):
        display(self.renderer)

# Ejemplo de uso
if __name__ == '__main__':
    files_to_compress = ['archivo1.txt', 'archivo2.txt']
    compress_files(files_to_compress, 'archivos_comprimidos.tar.gz')
    decompress_file('archivos_comprimidos.tar.gz')
    
    isla = IslaVirtual3D()
    isla.mostrar()
    
