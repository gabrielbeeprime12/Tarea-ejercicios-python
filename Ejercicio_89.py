# ejercicio_89
class ClasificadorNumeros:
    def __init__(self, n):
        self.n = n
        self.positivos = 0
        self.negativos = 0
        self.ceros = 0

    def procesar(self):
        for i in range(1, self.n + 1):
            num = float(input(f"Ingrese el número {i}: "))
            if num > 0:
                self.positivos += 1
            elif num < 0:
                self.negativos += 1
            else:
                self.ceros += 1

    def mostrar(self):
        print(f"\nPositivos: {self.positivos}")
        print(f"Negativos: {self.negativos}")
        print(f"Ceros: {self.ceros}")

n = int(input("Ingrese la cantidad de números: "))
app = ClasificadorNumeros(n)
app.procesar()
app.mostrar()