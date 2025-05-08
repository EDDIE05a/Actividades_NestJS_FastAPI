// backend/routes/estudiantes.js
const express = require('express');
const router = express.Router();
const Estudiante = require('../models/Estudiante');

router.post('/crear', (req, res) => {
  const { nombre, correo } = req.body;
  Estudiante.crear(nombre, correo, (err, result) => {
    if (err) return res.status(500).json({ error: err });
    res.json({ id: result.insertId, nombre, correo });
  });
});

router.get('/', (req, res) => {
  Estudiante.obtenerTodos((err, rows) => {
    if (err) return res.status(500).json({ error: err });
    res.json(rows);
  });
});

module.exports = router;
