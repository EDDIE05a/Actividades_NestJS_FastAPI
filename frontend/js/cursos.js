// frontend/js/cursos.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-curso');
    const lista = document.getElementById('lista-cursos');
  
    const cargarCursos = async () => {
      const cursos = await Curso.obtenerTodos();
      lista.innerHTML = '';
      cursos.forEach(curso => {
        const li = document.createElement('li');
        li.className = 'list-group-item';
        li.innerHTML = `<strong>${curso.nombre}</strong> - ${curso.descripcion} (${curso.creditos} créditos)`;
        lista.appendChild(li);
      });
    };
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const nombre = document.getElementById('nombre').value;
      const descripcion = document.getElementById('descripcion').value;
      const creditos = parseInt(document.getElementById('creditos').value);
      const curso = new Curso(nombre, descripcion, creditos);
      await curso.guardar();
      form.reset();
      cargarCursos();
    });
  
    cargarCursos();
  });
  