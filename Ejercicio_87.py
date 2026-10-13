# ejercicio_87
class MayorMenor:
    def __init__(self):
        self.mayor = None
        self.menor = None

    def procesar(self):
        for i in range(1, 11):
            num = float(input(f"Ingrese el número {i}: "))
            if self.mayor is None or num > self.mayor:
                self.mayor = num
            if self.menor is None or num < self.menor:
                self.menor = num

    def mostrar(self):
        print(f"\nEl número mayor es: {self.mayor}")
        print(f"El número menor es: {self.menor}")

app = MayorMenor()
app.procesar()
app.mostrar()