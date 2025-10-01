# MODELO: Auto y patrones
from abc import ABC, abstractmethod
from typing import List, Dict, Any

class AutoMemento:
    """Patrón Memento para guardar el estado de un Auto."""
    def __init__(self, estado: Dict[str, Any]):
        self.estado = estado.copy()

class Auto(ABC):
    """Clase base para autos. Utiliza Template Method."""
    def __init__(self, marca: str, modelo: str, color: str):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    def descripcion(self) -> str:
        return f"{self.marca} {self.modelo} ({self.color})"
    @abstractmethod
    def precio(self) -> float:
        pass
    def crear_memento(self) -> AutoMemento:
        return AutoMemento(self.__dict__)
    def restaurar_memento(self, memento: AutoMemento):
        self.__dict__.update(memento.estado)

class Sedan(Auto):
    def precio(self) -> float:
        return 20000.0

class SUV(Auto):
    def precio(self) -> float:
        return 30000.0

# DECORATOR para agregar características
class AutoDecorator(Auto):
    def __init__(self, auto: Auto):
        self.auto = auto
    def descripcion(self) -> str:
        return self.auto.descripcion()
    def precio(self) -> float:
        return self.auto.precio()

class SunroofDecorator(AutoDecorator):
    def descripcion(self) -> str:
        return self.auto.descripcion() + " + Sunroof"
    def precio(self) -> float:
        return self.auto.precio() + 1200.0

class SportPackageDecorator(AutoDecorator):
    def descripcion(self) -> str:
        return self.auto.descripcion() + " + Sport Package"
    def precio(self) -> float:
        return self.auto.precio() + 2500.0

# BUILDER para construcción flexible
class AutoBuilder:
    """Builder para crear autos siguiendo SOLID."""
    def __init__(self):
        self.marca = ""
        self.modelo = ""
        self.color = ""
        self.tipo = "sedan"
        self.decoradores: List[str] = []
    def set_marca(self, marca: str):
        self.marca = marca
        return self
    def set_modelo(self, modelo: str):
        self.modelo = modelo
        return self
    def set_color(self, color: str):
        self.color = color
        return self
    def set_tipo(self, tipo: str):
        self.tipo = tipo
        return self
    def add_decorador(self, decorador: str):
        self.decoradores.append(decorador)
        return self
    def build(self) -> Auto:
        if self.tipo == "sedan":
            auto = Sedan(self.marca, self.modelo, self.color)
        elif self.tipo == "suv":
            auto = SUV(self.marca, self.modelo, self.color)
        else:
            raise ValueError("Tipo de auto no soportado")
        for decorador in self.decoradores:
            if decorador == "sunroof":
                auto = SunroofDecorator(auto)
            elif decorador == "sport":
                auto = SportPackageDecorator(auto)
        return auto

# CONTROLADOR: CRUD para autos
class AutoController:
    """Controlador para manejar operaciones CRUD de autos."""
    def __init__(self):
        self.autos: Dict[int, Auto] = {}
        self.next_id = 1
        self.historial: Dict[int, List[AutoMemento]] = {}

    def crear_auto(self, datos: Dict[str, Any]) -> int:
        """
        Crea un auto usando el builder. Ejemplo de datos:
        {
            "marca": "Toyota",
            "modelo": "Corolla",
            "color": "Rojo",
            "tipo": "sedan",
            "decoradores": ["sunroof", "sport"]
        }
        """
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
        """Devuelve los datos del auto para la UI web."""
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
        """Lista todos los autos registrados."""
        return [self.obtener_auto(auto_id) for auto_id in self.autos]

    def actualizar_auto(self, auto_id: int, datos: Dict[str, Any]) -> bool:
        """Actualiza los datos de un auto y guarda el memento."""
        auto = self.autos.get(auto_id)
        if not auto:
            return False
        for key, value in datos.items():
            if hasattr(auto, key):
                setattr(auto, key, value)
        self.historial[auto_id].append(auto.crear_memento())
        return True

    def eliminar_auto(self, auto_id: int) -> bool:
        """Elimina un auto del sistema."""
        if auto_id in self.autos:
            del self.autos[auto_id]
            del self.historial[auto_id]
            return True
        return False

    def restaurar_auto(self, auto_id: int, version: int) -> bool:
        """Restaura el estado anterior de un auto usando memento."""
        historial = self.historial.get(auto_id)
        auto = self.autos.get(auto_id)
        if not historial or not auto or version >= len(historial):
            return False
        auto.restaurar_memento(historial[version])
        return True

# DOCUMENTACIÓN PARA UI WEB (React)
"""
Sugerencia de endpoints para la UI web:

POST /autos           -> crear_auto(datos)
GET /autos            -> listar_autos()
GET /autos/<id>       -> obtener_auto(id)
PUT /autos/<id>       -> actualizar_auto(id, datos)
DELETE /autos/<id>    -> eliminar_auto(id)
POST /autos/<id>/restore/<version> -> restaurar_auto(id, version)

La UI puede consumir estos métodos usando fetch/Axios en React.
"""
def main():
    print("Hello from backend!")


if __name__ == "__main__":
    main()
