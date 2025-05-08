// backend/models/Inscripcion.js
const db = require('../database');

class Inscripcion {
  static inscribir(estudianteId, cursoId, callback) {
    const sql = 'INSERT INTO inscripciones (estudiante_id, curso_id) VALUES (?, ?)';
    db.query(sql, [estudianteId, cursoId], callback);
  }

  static obtenerCursosPorEstudiante(estudianteId, callback) {
    const sql = `
      SELECT cursos.* FROM cursos
      JOIN inscripciones ON cursos.id = inscripciones.curso_id
      WHERE inscripciones.estudiante_id = ?
    `;
    db.query(sql, [estudianteId], callback);
  }

  static eliminarInscripcion(estudianteId, cursoId, callback) {
    const sql = 'DELETE FROM inscripciones WHERE estudiante_id = ? AND curso_id = ?';
    db.query(sql, [estudianteId, cursoId], callback);
  }
}

module.exports = Inscripcion;
