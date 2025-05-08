// backend/index.js
const express = require('express');
const cors = require('cors');
const app = express();
const path = require('path');

app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../frontend')));

app.use('/api/estudiantes', require('./routes/estudiantes'));
app.use('/api/cursos', require('./routes/cursos'));
app.use('/api/inscripciones', require('./routes/inscripciones'));


app.listen(3000, () => {
  console.log('Servidor backend corriendo en http://localhost:3000');
});
