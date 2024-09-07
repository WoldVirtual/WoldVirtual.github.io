import pythreejs as p3
from IPython.display import display
import psutil  # Para verificar la RAM disponible

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
        ram_disponible = psutil.virtual_memory().available / (1024 ** 2)  # Convertir a MB
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
        water.position.y = -1  # Colocar el agua debajo de la isla
        self.scene.add(water)

    def mostrar(self):
        display(self.renderer)

# Ejemplo de uso
if __name__ == '__main__':
    isla = IslaVirtual3D()
    isla.mostrar()
