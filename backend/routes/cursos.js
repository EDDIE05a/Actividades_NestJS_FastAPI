// backend/routes/cursos.js
const express = require('express');
const router = express.Router();
const Curso = require('../models/Curso');

// Crear curso
router.post('/crear', (req, res) => {
  const { nombre, descripcion, creditos } = req.body;
  Curso.crear(nombre, descripcion, creditos, (err, result) => {
    if (err) return res.status(500).json({ error: err });
    res.json({ id: result.insertId, nombre, descripcion, creditos });
  });
});

// Obtener todos los cursos
router.get('/', (req, res) => {
  Curso.obtenerTodos((err, rows) => {
    if (err) return res.status(500).json({ error: err });
    res.json(rows);
  });
});

module.exports = router;
