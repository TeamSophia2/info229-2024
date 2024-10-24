from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir el frontend React (cambia el puerto si es diferente)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todas las cabeceras
)

# Modelo para el comentario
class Comment(BaseModel):
    username: str
    comment: str

# Lista de comentarios inicial
comments = [
    {"username": "Matthieu", "comment": "Este es un comentario inicial."},
    {"username": "Luis", "comment": "¡Me encanta esta aplicación!"}
]

# Ruta de inicio (sirve HTML)
@app.get("/", response_class=HTMLResponse)
async def get_home():
    return """
    <html>
        <head>
            <title>Plataforma de Comentarios</title>
        </head>
        <body style="text-align: center; font-family: Arial, sans-serif; margin-top: 50px;">
            <h1>¡Bienvenido a la Plataforma de Comentarios!</h1>
            <p>Este es un servidor API creado con FastAPI.</p>
            <p>Puedes ver los comentarios o agregar los tuyos a través de nuestra API.</p>
            <p>Visita la <a href="/comments">ruta de comentarios</a> para ver todos los comentarios disponibles.</p>
            <p>También puedes hacer una petición POST a <code>/comments</code> para agregar nuevos comentarios.</p>
            <p>Explora la <a href="/docs">documentación interactiva de la API aquí</a>.</p>
        </body>
    </html>
    """

# Ruta GET para obtener todos los comentarios
@app.get("/comments", response_model=List[Comment])
async def get_comments():
    return comments

# Ruta POST para agregar un comentario
@app.post("/comments", response_model=Comment)
async def post_comment(comment: Comment):
    new_comment = {"username": comment.username, "comment": comment.comment}
    comments.append(new_comment)
    return new_comment

# Ejecuta con: uvicorn nombre_archivo:app --reload
