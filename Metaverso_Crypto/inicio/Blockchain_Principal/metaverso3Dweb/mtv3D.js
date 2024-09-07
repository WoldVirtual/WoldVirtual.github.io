// Crear la escena
const scene = new THREE.Scene();

// Crear la isla
const islandGeometry = new THREE.CylinderGeometry(5, 5, 2, 32);
const islandMaterial = new THREE.MeshBasicMaterial({ color: 'green' });
const island = new THREE.Mesh(islandGeometry, islandMaterial);
scene.add(island);

// Crear el agua
const waterGeometry = new THREE.PlaneGeometry(20, 20);
const waterMaterial = new THREE.MeshBasicMaterial({ color: 'blue', opacity: 0.5, transparent: true });
const water = new THREE.Mesh(waterGeometry, waterMaterial);
water.rotation.x = -Math.PI / 2; // Rotar el plano para que sea horizontal
water.position.y = -1; // Colocar el agua debajo de la isla
scene.add(water);

// Configurar la cámara y el renderizador
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 10;

const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('contenedor3D').appendChild(renderer.domElement);

// Función de animación
const animate = function () {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
};

animate();
