class AnalizadorSecuencia:
    def __init__(self):
        self.pares = 0
        self.impares = 0
        self.positivos = 0
        self.negativos = 0

    def evaluar(self):
        while True:
            num = int(input("Ingrese un número (0 para finalizar): "))
            if num == 0:
                break

            if num % 2 == 0:
                self.pares += 1
            else:
                self.impares += 1

            if num > 0:
                self.positivos += 1
            elif num < 0:
                self.negativos += 1

    def informe(self):
        print(f"\nPares: {self.pares} | Impares: {self.impares}")
        print(f"Positivos: {self.positivos} | Negativos: {self.negativos}")


app = AnalizadorSecuencia()
app.evaluar()
app.informe()