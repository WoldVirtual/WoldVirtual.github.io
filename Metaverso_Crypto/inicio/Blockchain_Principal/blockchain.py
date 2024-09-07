import hashlib
import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
        self.crear_bloque_genesis()

    def crear_bloque_genesis(self):
        try:
            genesis_block = self.crear_bloque(0, 'Bloque Génesis', '0')
            self.chain.append(genesis_block)
        except Exception as e:
            print(f"Error al crear el bloque génesis: {e}")

    def crear_bloque(self, index, data, previous_hash):
        try:
            timestamp = str(datetime.datetime.now())
            block = {
                'index': index,
                'timestamp': timestamp,
                'data': data,
                'previous_hash': previous_hash,
                'hash': self.hash_block(index, timestamp, data, previous_hash)
            }
            return block
        except Exception as e:
            print(f"Error al crear el bloque: {e}")
            return None

    def agregar_bloque(self, data):
        try:
            previous_block = self.chain[-1]
            new_block = self.crear_bloque(len(self.chain), data, previous_block['hash'])
            if new_block:
                self.chain.append(new_block)
        except Exception as e:
            print(f"Error al agregar el bloque: {e}")

    def confirmar_conexion_modulos(self, modulos):
        """
        Confirma la conexión de los módulos y agrega un bloque con la información.
        
        Args:
            modulos (list): Lista de nombres de los módulos a confirmar.
        """
        try:
            data = f"Conexión de módulos: {', '.join(modulos)}"
            self.agregar_bloque(data)
        except Exception as e:
            print(f"Error al confirmar la conexión de módulos: {e}")

    def obtener_informacion_cadena(self):
        try:
            informacion = {
                'longitud': len(self.chain),
                'bloques': [block for block in self.chain],
            }
            return informacion
        except Exception as e:
            print(f"Error al obtener la información de la cadena: {e}")
            return None

    def hash_block(self, index, timestamp, data, previous_hash):
        try:
            block_string = f"{index}{timestamp}{data}{previous_hash}"
            return hashlib.sha256(block_string.encode()).hexdigest()
        except Exception as e:
            print(f"Error al hashear el bloque: {e}")
            return None

    def validar_cadena(self):
        try:
            for i in range(1, len(self.chain)):
                current_block = self.chain[i]
                previous_block = self.chain[i - 1]
                if current_block['previous_hash'] != previous_block['hash']:
                    return False
                if current_block['hash'] != self.hash_block(current_block['index'], current_block['timestamp'], current_block['data'], previous_block['hash']):
                    return False
            return True
        except Exception as e:
            print(f"Error al validar la cadena: {e}")
            return False

    def imprimir_cadena(self):
        try:
            for block in self.chain:
                print(block)
        except Exception as e:
            print(f"Error al imprimir la cadena: {e}")

    def agregar_bloque_isla_virtual(self, ubicacion):
        """
        Agrega un bloque con la información de la isla virtual 3D y su ubicación.
        
        Args:
            ubicacion (str): Ubicación de la isla virtual 3D.
        """
        try:
            data = f"Isla Virtual 3D creada en la ubicación {ubicacion}"
            self.agregar_bloque(data)
            return data
        except Exception as e:
            print(f"Error al agregar el bloque de la isla virtual: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    try:
        blockchain = Blockchain()
        blockchain.confirmar_conexion_modulos(['usuarios', 'recursos', 'database', 'compresion', 'servidor'])
        blockchain.imprimir_cadena()
    except Exception as e:
        print(f"Error en el uso del ejemplo: {e}")
        
