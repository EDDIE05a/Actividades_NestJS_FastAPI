// frontend/js/Curso.js
class Curso {
    constructor(nombre, descripcion, creditos) {
      this.nombre = nombre;
      this.descripcion = descripcion;
      this.creditos = creditos;
    }
  
    static async obtenerTodos() {
      const res = await fetch('http://localhost:3000/api/cursos');
      return await res.json();
    }
  
    async guardar() {
      const res = await fetch('http://localhost:3000/api/cursos/crear', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this)
      });
      return await res.json();
    }
  }
  