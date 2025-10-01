"""
Punto de entrada principal para FastAPI.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.auto_routes import router as auto_router

app = FastAPI()

# Habilitar CORS para permitir peticiones desde React (localhost:5173)
app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],  # Puedes poner ["http://localhost:5173"] para mayor seguridad
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(auto_router)

# Puedes ejecutar el backend con:
# uvicorn app.main:app --reload

"""
Documentación rápida para la UI web (React):

- POST /autos           -> crear auto
- GET /autos            -> listar autos
- GET /autos/{id}       -> obtener auto
- PUT /autos/{id}       -> actualizar auto
- DELETE /autos/{id}    -> eliminar auto
- POST /autos/{id}/restore/{version} -> restaurar estado

La UI puede consumir estos endpoints usando fetch/Axios.
"""
