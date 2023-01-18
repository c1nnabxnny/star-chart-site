import './style.css'
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';

//* Set up the viewing window with scene, camera, and renderer

const scene = new THREE.Scene();

const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);

const renderer = new THREE.WebGL1Renderer({
  canvas: document.querySelector('#background')
})

//sets the render to the same amount of pixels as the screen it's being viewed on
renderer.setPixelRatio( window.devicePixelRatio );
//makes the render full screen by setting the render size to the window size
renderer.setSize(window.innerWidth, window.innerHeight);

camera.position.setZ(30);

renderer.render(scene, camera);

const stars = []
for (let i=0; i<10; i++) {
  const pointGeometry = new THREE.SphereGeometry(2, 2, 2);
  const pointMaterial = new THREE.MeshBasicMaterial({color: 0xFF6347, wireframe: true});
  const star = new THREE.Mesh(pointGeometry, pointMaterial);

  star.position.set(i, i, i);
  stars.push(star)
  scene.add(star);
}

const controls = new OrbitControls(camera, renderer.domElement);

//animates the scene once per frame
function animate(){
  requestAnimationFrame(animate);
    stars.forEach(star =>{
    star.rotation.x += 0.01;
    star.rotation.y += 0.01;
  });

  controls.update;

  renderer.render(scene, camera);
}

animate();

//changes the size of the canvas when the screen is resized
function onWindowResize() {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize( window.innerWidth, window.innerHeight );
}
window.addEventListener( 'resize', onWindowResize, false );