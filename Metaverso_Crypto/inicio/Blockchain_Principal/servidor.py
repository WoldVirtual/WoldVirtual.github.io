from flask import Flask, render_template_string, redirect, url_for
from flask_socketio import SocketIO
from blockchain import Blockchain
from almacenamiento import IslaVirtual3D

# Inicializar la aplicación Flask y SocketIO
app = Flask(__name__)
socketio = SocketIO(app)
blockchain = Blockchain()

# Plantilla HTML para la interfaz web
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metaverso Crypto 3D</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f9f9f9; }
        .header { background-color: #4CAF50; color: white; padding: 15px 0; text-align: center; }
        .nav { display: flex; justify-content: center; background-color: #333; }
        .nav a { color: white; padding: 14px 20px; text-decoration: none; text-align: center; }
        .nav a:hover { background-color: #ddd; color: black; }
        .container { margin: 20px auto; padding: 20px; max-width: 800px; background-color: #fff; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); }
        .section { margin-bottom: 20px; }
        h1, h2 { margin-top: 0; }
        .button { background-color: #4CAF50; border: none; color: white; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 4px; }
        .button:hover { background-color: #45a049; }
    </style>
</head>
<body>
    <div class="header"><h1>Metaverso Crypto 3D</h1></div>
    <div class="nav">
        <a href="{{ url_for('index') }}">Inicio</a>
        <a href="{{ url_for('usuarios') }}">Usuarios</a>
        <a href="{{ url_for('recursos') }}">Recursos</a>
        <a href="{{ url_for('blockchain') }}">Blockchain</a>
        <a href="{{ url_for('database') }}">Base de Datos</a>
        <a href="{{ url_for('compresion') }}">Compresión</a>
        <a href="{{ url_for('servidor') }}">Servidor</a>
        <a href="{{ url_for('isla_virtual') }}">Isla Virtual "World Central 3D"</a>
    </div>
    <div class="container">
        <div id="home" class="section">
            <h2>Metaverso Crypto 3D descentralizado</h2>
            <p>Próximamente en esta página principal, se darán más detalles sobre el proyecto...</p>
            <button class="button">Más Información</button>
        </div>
        <!-- Secciones adicionales aquí -->
    </div>
    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
    <script>
        const socket = io();
        document.getElementById('sendButton').addEventListener('click', () => {
            const audioData = document.getElementById('audioInput').value;
            socket.emit('audio_stream', audioData);
        });
        socket.on('audio_stream', (data) => {
            console.log('Received audio data:', data);
        });
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """
    Renderiza la plantilla HTML para la página principal.
    """
    return render_template_string(html_template)

@app.route('/isla_virtual')
def isla_virtual():
    """
    Renderiza la isla virtual 3D y agrega una transacción a la blockchain.
    """
    isla = IslaVirtual3D()
    isla.mostrar()
    blockchain.agregar_bloque("Isla Virtual 3D cargada en la ubicación 100 x 100")
    return redirect(url_for('index'))

# @socketio.on('audio_stream')
# def handle_audio(data):
#     """
#     Maneja el evento de transmisión de audio.
#     """
#     socketio.emit('audio_stream', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)
