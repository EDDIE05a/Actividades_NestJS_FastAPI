// backend/models/Estudiante.js
const db = require('../database');

class Estudiante {
  static crear(nombre, correo, callback) {
    const sql = 'INSERT INTO estudiantes (nombre, correo) VALUES (?, ?)';
    db.query(sql, [nombre, correo], callback);
  }

  static obtenerTodos(callback) {
    db.query('SELECT * FROM estudiantes', callback);
  }
}

module.exports = Estudiante;
