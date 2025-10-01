"""
Rutas de FastAPI para autos. Expone el CRUD para la UI web.
"""
from fastapi import APIRouter, HTTPException
from app.controllers.auto_controller import AutoController
from app.schemas.auto_schema import AutoCreateSchema, AutoUpdateSchema, AutoResponseSchema
from typing import List

router = APIRouter()
auto_controller = AutoController()

@router.post("/autos", response_model=int)
def crear_auto(auto: AutoCreateSchema):
    """Crea un auto nuevo."""
    auto_id = auto_controller.crear_auto(auto.dict())
    return auto_id

@router.get("/autos", response_model=List[AutoResponseSchema])
def listar_autos():
    """Lista todos los autos."""
    return auto_controller.listar_autos()

@router.get("/autos/{auto_id}", response_model=AutoResponseSchema)
def obtener_auto(auto_id: int):
    """Obtiene un auto por ID."""
    auto = auto_controller.obtener_auto(auto_id)
    if "error" in auto:
        raise HTTPException(status_code=404, detail=auto["error"])
    return auto

@router.put("/autos/{auto_id}", response_model=bool)
def actualizar_auto(auto_id: int, auto: AutoUpdateSchema):
    """Actualiza un auto."""
    return auto_controller.actualizar_auto(auto_id, auto.dict(exclude_unset=True))

@router.delete("/autos/{auto_id}", response_model=bool)
def eliminar_auto(auto_id: int):
    """Elimina un auto."""
    return auto_controller.eliminar_auto(auto_id)

@router.post("/autos/{auto_id}/restore/{version}", response_model=bool)
def restaurar_auto(auto_id: int, version: int):
    """Restaura el estado anterior de un auto."""
    return auto_controller.restaurar_auto(auto_id, version)
