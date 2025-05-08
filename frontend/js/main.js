// frontend/js/main.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-estudiante');
    const lista = document.getElementById('lista-estudiantes');
  
    const cargarEstudiantes = async () => {
      const estudiantes = await Estudiante.obtenerTodos();
      lista.innerHTML = '';
      estudiantes.forEach(est => {
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.textContent = `${est.nombre} (${est.correo})`;
        lista.appendChild(li);
      });
    };
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const nombre = document.getElementById('nombre').value;
      const correo = document.getElementById('correo').value;
      const estudiante = new Estudiante(nombre, correo);
      await estudiante.guardar();
      form.reset();
      cargarEstudiantes();
    });
  
    cargarEstudiantes();
  });
  