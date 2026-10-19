"""
Módulo CoffeeMachine
Implementación de máquina de café con inventario desarrollada con TDD.
"""
from typing import Dict


class CoffeeMachine:
    """
    Simulador de máquina de café.
    Controla inventario de vasos, café (onzas) y azúcar (cucharadas).
    """

    SIZES: Dict[str, int] = {
        "Pequeño": 3,
        "Mediano": 5,
        "Grande": 7
    }

    def __init__(self, vasos: int = 10, cafe: int = 50, azucar: int = 20) -> None:
        """
        Inicializa la máquina con los insumos especificados.
        """
        self.vasos = vasos
        self.cafe = cafe
        self.azucar = azucar

    def servir_cafe(self, tamano: str, cucharadas_azucar: int = 0) -> str:
        """
        Despacha un café según el tamaño y cantidad de azúcar solicitados,
        actualizando los insumos disponibles.

        Args:
            tamano: 'Pequeño', 'Mediano' o 'Grande'.
            cucharadas_azucar: Cantidad de cucharadas de azúcar deseadas (default: 0).

        Returns:
            str: Mensaje de confirmación del café servido o mensaje descriptivo de error.
        """
        if self.vasos <= 0:
            return "Error: No hay vasos disponibles"

        if tamano not in self.SIZES:
            return "Error: Tamaño de vaso inválido"

        oz_necesarias = self.SIZES[tamano]
        if self.cafe < oz_necesarias:
            return "Error: No hay café disponible"

        if cucharadas_azucar > self.azucar:
            return "Error: No hay suficiente azúcar"

        self.vasos -= 1
        self.cafe -= oz_necesarias
        self.azucar -= cucharadas_azucar

        return f"Café servido: {oz_necesarias} Oz con {cucharadas_azucar} cucharadas de azúcar"
