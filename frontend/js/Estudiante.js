// frontend/js/Estudiante.js
class Estudiante {
    constructor(nombre, correo) {
      this.nombre = nombre;
      this.correo = correo;
    }
  
    static async obtenerTodos() {
      const res = await fetch('http://localhost:3000/api/estudiantes');
      return await res.json();
    }
  
    async guardar() {
      const res = await fetch('http://localhost:3000/api/estudiantes/crear', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(this)
      });
      return await res.json();
    }
  }
  