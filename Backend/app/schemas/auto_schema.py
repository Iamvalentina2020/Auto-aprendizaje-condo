"""
Esquemas para validación y serialización de datos de autos (usando Pydantic).
"""
from pydantic import BaseModel
from typing import List, Optional

class AutoCreateSchema(BaseModel):
    marca: str
    modelo: str
    color: str
    tipo: str = "sedan"
    decoradores: Optional[List[str]] = []

class AutoUpdateSchema(BaseModel):
    marca: Optional[str]
    modelo: Optional[str]
    color: Optional[str]

class AutoResponseSchema(BaseModel):
    id: int
    descripcion: str
    precio: float
    marca: str
    modelo: str
    color: str
