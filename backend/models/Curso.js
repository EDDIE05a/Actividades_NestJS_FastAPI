// backend/models/Curso.js
const db = require('../database');

class Curso {
  static crear(nombre, descripcion, creditos, callback) {
    const sql = 'INSERT INTO cursos (nombre, descripcion, creditos) VALUES (?, ?, ?)';
    db.query(sql, [nombre, descripcion, creditos], callback);
  }

  static obtenerTodos(callback) {
    db.query('SELECT * FROM cursos', callback);
  }
}

module.exports = Curso;
