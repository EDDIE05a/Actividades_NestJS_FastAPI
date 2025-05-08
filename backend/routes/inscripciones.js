const express = require('express');
const router = express.Router();
const db = require('../db');

// Inscribir estudiante en un curso
router.post('/', (req, res) => {
  const { estudiante_id, curso_id } = req.body;
  const sql = 'INSERT INTO inscripciones (estudiante_id, curso_id) VALUES (?, ?)';
  db.query(sql, [estudiante_id, curso_id], (err, result) => {
    if (err) return res.status(500).json({ error: err });
    res.json({ mensaje: 'Estudiante inscrito en curso', id: result.insertId });
  });
});

// Listar cursos por estudiante
router.get('/:estudiante_id', (req, res) => {
  const { estudiante_id } = req.params;
  const sql = `
    SELECT cursos.id, cursos.nombre, cursos.descripcion, cursos.creditos 
    FROM cursos 
    JOIN inscripciones ON cursos.id = inscripciones.curso_id 
    WHERE inscripciones.estudiante_id = ?`;
  db.query(sql, [estudiante_id], (err, result) => {
    if (err) return res.status(500).json({ error: err });
    res.json(result);
  });
});

// Eliminar inscripción
router.delete('/', (req, res) => {
  const { estudiante_id, curso_id } = req.body;
  const sql = 'DELETE FROM inscripciones WHERE estudiante_id = ? AND curso_id = ?';
  db.query(sql, [estudiante_id, curso_id], (err) => {
    if (err) return res.status(500).json({ error: err });
    res.json({ mensaje: 'Inscripción eliminada' });
  });
});

module.exports = router;
