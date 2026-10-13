# ejercicio_96
class CajaRegistradora:
    def __init__(self):
        self.total = 0.0

    def iniciar_venta(self):
        while True:
            producto = input("Nombre del producto (o 'finalizar' para terminar): ")
            if producto.lower() == 'finalizar':
                break
            precio = float(input(f"Precio de {producto}: "))
            self.total += precio

    def mostrar_total(self):
        print(f"\n--- Total a pagar: ${self.total:.2f} ---")

app = CajaRegistradora()
app.iniciar_venta()
app.mostrar_total()