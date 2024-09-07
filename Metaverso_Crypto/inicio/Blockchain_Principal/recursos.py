class RecursosUsuario:
    def __init__(self, porcentaje_cpu, porcentaje_ancho_banda):
        self.porcentaje_cpu = porcentaje_cpu
        self.porcentaje_ancho_banda = porcentaje_ancho_banda

    def asignar_recursos(self, recursos_comunitarios):
        """
        Asigna recursos a un usuario basado en los recursos comunitarios.

        Args:
            recursos_comunitarios (dict): Recursos disponibles en la comunidad.

        Returns:
            dict: Recursos asignados al usuario.
        """
        try:
            recursos_asignados = {
                'cpu': recursos_comunitarios['cpu'] * (self.porcentaje_cpu / 100),
                'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.porcentaje_ancho_banda / 100),
            }
            return recursos_asignados
        except KeyError as e:
            print(f"Error al asignar recursos: clave no encontrada {e}")
            return {}
        except Exception as e:
            print(f"Error al asignar recursos: {e}")
            return {}

class MonitoreoRecursos:
    def __init__(self):
        self.recursos_usuarios = {}

    def actualizar_recursos(self, nombre_usuario, uso_cpu, uso_ancho_banda):
        """
        Actualiza el uso de recursos de un usuario.

        Args:
            nombre_usuario (str): Nombre del usuario.
            uso_cpu (float): Porcentaje de uso de CPU.
            uso_ancho_banda (float): Porcentaje de uso de ancho de banda.
        """
        try:
            self.recursos_usuarios[nombre_usuario] = {
                'uso_cpu': uso_cpu,
                'uso_ancho_banda': uso_ancho_banda
            }
        except Exception as e:
            print(f"Error al actualizar recursos: {e}")

    def obtener_informacion(self):
        """
        Obtiene la información de uso de recursos de todos los usuarios.

        Returns:
            dict: Información de uso de recursos.
        """
        try:
            return self.recursos_usuarios
        except Exception as e:
            print(f"Error al obtener información de recursos: {e}")
            return {}

    @staticmethod
    def inicializar():
        """
        Inicializa los recursos.
        """
        try:
            print("Recursos inicializados")
        except Exception as e:
            print(f"Error al inicializar recursos: {e}")

    def asignar_recursos_isla_virtual(self, nombre_usuario, recursos_comunitarios):
        """
        Asigna recursos específicos para la isla virtual 3D a un usuario.

        Args:
            nombre_usuario (str): Nombre del usuario.
            recursos_comunitarios (dict): Recursos disponibles en la comunidad.

        Returns:
            dict: Recursos asignados al usuario para la isla virtual 3D.
        """
        try:
            recursos_asignados = {
                'cpu': recursos_comunitarios['cpu'] * (self.recursos_usuarios[nombre_usuario]['uso_cpu'] / 100),
                'ancho_banda': recursos_comunitarios['ancho_banda'] * (self.recursos_usuarios[nombre_usuario]['uso_ancho_banda'] / 100),
            }
            print(f"Recursos asignados para la isla virtual 3D a {nombre_usuario}: {recursos_asignados}")
            return recursos_asignados
        except KeyError as e:
            print(f"Error al asignar recursos para la isla virtual: clave no encontrada {e}")
            return {}
        except Exception as e:
            print(f"Error al asignar recursos para la isla virtual: {e}")
            return {}

# Ejemplo de uso
if __name__ == "__main__":
    recursos_comunitarios = {'cpu': 100, 'ancho_banda': 1000}
    usuario = RecursosUsuario(50, 50)
    recursos_asignados = usuario.asignar_recursos(recursos_comunitarios)
    print(f"Recursos asignados: {recursos_asignados}")

    monitoreo = MonitoreoRecursos()
    monitoreo.actualizar_recursos("usuario1", 30, 200)
    print(f"Información de recursos: {monitoreo.obtener_informacion()}")
    MonitoreoRecursos.inicializar()

    # Asignar recursos específicos para la isla virtual 3D
    recursos_isla_virtual = monitoreo.asignar_recursos_isla_virtual("usuario1", recursos_comunitarios)
    print(f"Recursos asignados para la isla virtual 3D: {recursos_isla_virtual}")
