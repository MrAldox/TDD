class CoffeeMachine:
    def __init__(self, vasos=10, cafe=50, azucar=20):
        self.vasos = vasos
        self.cafe = cafe
        self.azucar = azucar
        self.tamanos = {"Pequeño": 3, "Mediano": 5, "Grande": 7}

    def servir_cafe(self, tamano, cucharadas_azucar=0):
        if self.vasos <= 0:
            return "Error: No hay vasos disponibles"
        if tamano not in self.tamanos:
            return "Error: Tamaño de vaso inválido"
        if self.cafe < self.tamanos[tamano]:
            return "Error: No hay café disponible"
        if cucharadas_azucar > self.azucar:
            return "Error: No hay suficiente azúcar"

        self.vasos -= 1
        self.cafe -= self.tamanos[tamano]
        self.azucar -= cucharadas_azucar

        return f"Café servido: {self.tamanos[tamano]} Oz con {cucharadas_azucar} cucharadas de azúcar"

# Pruebas con pytest
def test_seleccion_tamano_vaso():
    machine = CoffeeMachine()
    assert machine.servir_cafe("Pequeño") == "Café servido: 3 Oz con 0 cucharadas de azúcar"
    assert machine.servir_cafe("Mediano") == "Café servido: 5 Oz con 0 cucharadas de azúcar"
    assert machine.servir_cafe("Grande") == "Café servido: 7 Oz con 0 cucharadas de azúcar"

def test_seleccion_azucar():
    machine = CoffeeMachine()
    assert machine.servir_cafe("Mediano", 2) == "Café servido: 5 Oz con 2 cucharadas de azúcar"

def test_error_en_insumos():
    machine = CoffeeMachine(vasos=0, cafe=10, azucar=10)
    assert machine.servir_cafe("Pequeño") == "Error: No hay vasos disponibles"

    machine = CoffeeMachine(vasos=10, cafe=2, azucar=10)
    assert machine.servir_cafe("Mediano") == "Error: No hay café disponible"

    machine = CoffeeMachine(vasos=10, cafe=10, azucar=0)
    assert machine.servir_cafe("Mediano", 1) == "Error: No hay suficiente azúcar"

def test_tamano_invalido():
    machine = CoffeeMachine()
    assert machine.servir_cafe("ExtraGrande") == "Error: Tamaño de vaso inválido"
