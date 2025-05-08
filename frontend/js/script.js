const estudianteSelect = document.getElementById('estudiante');
const cursoSelect = document.getElementById('curso');
const listaCursos = document.getElementById('lista-cursos');

async function cargarEstudiantesYCursos() {
  const estudiantes = await fetch('/api/estudiantes').then(res => res.json());
  const cursos = await fetch('/api/cursos').then(res => res.json());

  estudiantes.forEach(e => {
    estudianteSelect.innerHTML += `<option value="${e.id}">${e.nombre}</option>`;
  });

  cursos.forEach(c => {
    cursoSelect.innerHTML += `<option value="${c.id}">${c.nombre}</option>`;
  });

  estudianteSelect.addEventListener('change', cargarCursosInscritos);
  cargarCursosInscritos(); // Mostrar los cursos del primer estudiante al cargar
}

async function inscribir() {
  const estudiante_id = estudianteSelect.value;
  const curso_id = cursoSelect.value;

  await fetch('/api/inscripciones', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ estudiante_id, curso_id })
  });

  cargarCursosInscritos();
}

async function cargarCursosInscritos() {
  const estudiante_id = estudianteSelect.value;
  const cursos = await fetch(`/api/inscripciones/${estudiante_id}`).then(res => res.json());

  listaCursos.innerHTML = '';
  cursos.forEach(c => {
    listaCursos.innerHTML += `<li class="list-group-item">${c.nombre} - ${c.descripcion} (${c.creditos} créditos)</li>`;
  });
}

cargarEstudiantesYCursos();
