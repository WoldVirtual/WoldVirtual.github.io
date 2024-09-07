// Crear la escena
var scene = new THREE.Scene();

// Crear la isla
var islandGeometry = new THREE.CylinderGeometry(5, 5, 2, 32);
var islandMaterial = new THREE.MeshBasicMaterial({color: 'green'});
var island = new THREE.Mesh(islandGeometry, islandMaterial);
scene.add(island);

// Crear el agua
var waterGeometry = new THREE.PlaneGeometry(20, 20);
var waterMaterial = new THREE.MeshBasicMaterial({color: 'blue', opacity=0.5, transparent: true});
var water = new THREE.Mesh(waterGeometry, waterMaterial);
water.rotation.x = - Math.PI / 2; // Rotar el plano para que sea horizontal
water.position.y = -1; // Colocar el agua debajo de la isla
scene.add(water);

// Configurar la cámara y el renderizador
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 10;

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.getElementById('contenedor3D').appendChild(renderer.domElement);

var animate = function () {
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
};

animate();
