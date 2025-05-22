# from fastapi import FastAPI, HTTPExection
# from pydantic import BaseModel
# import mysql.connector

# app = FastAPI()

# db_config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "root",
#     "database": "flask_db"
# }

# #Modelo Pydantic
# class Persona(BaseModel):
#     nombre: str
#     edad: int


# @app.get("/")
# def read_root():
#     return {"mensaje": "API con FastAPI = MySQL"}

# @app.get("/personas")
# def listar_personas():
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, nombre, edad FROM Usuarios")
#     resultados = cursor.fetchall()
#     cursor.close()
#     conn.close()
#     return [{"id": row[0], "nombre": row[1], "edad": row[2]} for row in resultados]


# @app.route("/personas")
# def crear_persona(persona: Persona):
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO Usuarios (nombre, edad) VALUES (%, %)", (persona.nombre, persona.edad))
#     resultados = cursor.fetchall()
#     cursor.close()
#     conn.close()


# @app.get("/personas/{persona_id}")
# def obtener_persona(persona_id: int):
#     conn = mysql.connector.connect(**db_config)
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, nombre, edad FROM Usuarios WHERE id = %", (persona_id))
#     row = cursor.fetchone()
#     cursor.close()
#     conn.close()
#     if row:
#         return {"id": row[0], "nombre": row[1], "edad": row[2]}
#     raise HTTPExeption(status_code=404, detail)


# @app.get("/saludo/{nombre}")
# def saludar(nombre: str):
#     return {"mensaje": f"Hola {nombre}"}


# @app.post("/crear-persona")
# def crear_persona(persona: Persona):
#     return {"mensaje": f"{persona.nombre} registrada con {persona.edad} años