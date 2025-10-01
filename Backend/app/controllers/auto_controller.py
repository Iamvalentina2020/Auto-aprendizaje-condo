"""
Controlador para manejar operaciones CRUD de autos.
"""
from typing import Dict, Any, List
from app.models.auto import Auto, AutoBuilder, AutoMemento

class AutoController:
    """Controlador para manejar operaciones CRUD de autos."""
    def __init__(self):
        self.autos: Dict[int, Auto] = {}
        self.next_id = 1
        self.historial: Dict[int, List[AutoMemento]] = {}

    def crear_auto(self, datos: Dict[str, Any]) -> int:
        builder = AutoBuilder()
        builder.set_marca(datos.get("marca", ""))
        builder.set_modelo(datos.get("modelo", ""))
        builder.set_color(datos.get("color", ""))
        builder.set_tipo(datos.get("tipo", "sedan"))
        for decorador in datos.get("decoradores", []):
            builder.add_decorador(decorador)
        auto = builder.build()
        auto_id = self.next_id
        self.autos[auto_id] = auto
        self.historial[auto_id] = [auto.crear_memento()]
        self.next_id += 1
        return auto_id

    def obtener_auto(self, auto_id: int) -> Dict[str, Any]:
        auto = self.autos.get(auto_id)
        if not auto:
            return {"error": "Auto no encontrado"}
        return {
            "id": auto_id,
            "descripcion": auto.descripcion(),
            "precio": auto.precio(),
            "marca": auto.marca,
            "modelo": auto.modelo,
            "color": auto.color
        }

    def listar_autos(self) -> List[Dict[str, Any]]:
        return [self.obtener_auto(auto_id) for auto_id in self.autos]

    def actualizar_auto(self, auto_id: int, datos: Dict[str, Any]) -> bool:
        auto = self.autos.get(auto_id)
        if not auto:
            return False
        for key, value in datos.items():
            if hasattr(auto, key):
                setattr(auto, key, value)
        self.historial[auto_id].append(auto.crear_memento())
        return True

    def eliminar_auto(self, auto_id: int) -> bool:
        if auto_id in self.autos:
            del self.autos[auto_id]
            del self.historial[auto_id]
            return True
        return False

    def restaurar_auto(self, auto_id: int, version: int) -> bool:
        historial = self.historial.get(auto_id)
        auto = self.autos.get(auto_id)
        if not historial or not auto or version >= len(historial):
            return False
        auto.restaurar_memento(historial[version])
        return True
