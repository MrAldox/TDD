"""
Pruebas unitarias para CoffeeMachine desarrolladas con pytest.
"""
import pytest
from src.coffee_machine import CoffeeMachine


@pytest.fixture
def default_machine() -> CoffeeMachine:
    """Fixture que provee una máquina de café con valores por defecto."""
    return CoffeeMachine(vasos=10, cafe=50, azucar=20)


class TestCoffeeMachineSuccessCases:
    """Pruebas para los flujos exitosos de servicio de café."""

    def test_seleccion_tamano_pequeno(self, default_machine: CoffeeMachine):
        resultado = default_machine.servir_cafe("Pequeño")
        assert resultado == "Café servido: 3 Oz con 0 cucharadas de azúcar"

    def test_seleccion_tamano_mediano(self, default_machine: CoffeeMachine):
        resultado = default_machine.servir_cafe("Mediano")
        assert resultado == "Café servido: 5 Oz con 0 cucharadas de azúcar"

    def test_seleccion_tamano_grande(self, default_machine: CoffeeMachine):
        resultado = default_machine.servir_cafe("Grande")
        assert resultado == "Café servido: 7 Oz con 0 cucharadas de azúcar"

    def test_servicio_con_azucar(self, default_machine: CoffeeMachine):
        resultado = default_machine.servir_cafe("Mediano", cucharadas_azucar=2)
        assert resultado == "Café servido: 5 Oz con 2 cucharadas de azúcar"

    def test_actualizacion_inventario(self, default_machine: CoffeeMachine):
        default_machine.servir_cafe("Grande", cucharadas_azucar=3)
        assert default_machine.vasos == 9
        assert default_machine.cafe == 43
        assert default_machine.azucar == 17


class TestCoffeeMachineValidationAndErrors:
    """Pruebas para validaciones de inventario y errores de entrada."""

    def test_error_sin_vasos(self):
        machine = CoffeeMachine(vasos=0, cafe=10, azucar=10)
        assert machine.servir_cafe("Pequeño") == "Error: No hay vasos disponibles"

    def test_error_tamano_invalido(self, default_machine: CoffeeMachine):
        assert default_machine.servir_cafe("ExtraGrande") == "Error: Tamaño de vaso inválido"

    def test_error_sin_cafe_suficiente(self):
        machine = CoffeeMachine(vasos=10, cafe=2, azucar=10)
        assert machine.servir_cafe("Mediano") == "Error: No hay café disponible"

    def test_error_sin_azucar_suficiente(self):
        machine = CoffeeMachine(vasos=10, cafe=20, azucar=1)
        assert machine.servir_cafe("Mediano", cucharadas_azucar=3) == "Error: No hay suficiente azúcar"
