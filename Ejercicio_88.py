# ejercicio_88
class CalculadoraPromedio:
    def __init__(self, n):
        self.n = n
        self.suma = 0.0

    def calcular(self):
        for i in range(1, self.n + 1):
            num = float(input(f"Ingrese el número {i} de {self.n}: "))
            self.suma += num

    def mostrar(self):
        promedio = self.suma / self.n if self.n > 0 else 0
        print(f"\nSuma total: {self.suma}")
        print(f"Promedio: {promedio:.2f}")


n = int(input("¿Cuántos números desea ingresar?: "))
app = CalculadoraPromedio(n)
app.calcular()
app.mostrar()