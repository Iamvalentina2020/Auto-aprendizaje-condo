"""
Modelos y patrones para autos.
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List

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
