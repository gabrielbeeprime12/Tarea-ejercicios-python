# Ejercicio_86

class ContadorParImpar:
    def __init__(self):
        self.pares = 0
        self.impares = 0

    def procesar_numeros(self):
        for i in range(1, 11):
            num = int(input(f"Ingrese el número {i}: "))
            if num % 2 == 0:
                self.pares += 1
            else:
                self.impares += 1

    def mostrar_resultados(self):
        print(f"\nCantidad de pares: {self.pares}")
        print(f"Cantidad de impares: {self.impares}")

app = ContadorParImpar()
app.procesar_numeros()
app.mostrar_resultados()