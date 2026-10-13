# ejercicio_94
class ContadorEdades:
    def __init__(self):
        self.mayores = 0
        self.menores = 0

    def procesar(self):
        while True:
            edad = int(input("Ingrese edad (0 para salir): "))
            if edad == 0:
                break

            if edad >= 18:
                self.mayores += 1
            elif edad > 0:
                self.menores += 1

    def resumen(self):
        print(f"\nMayores de edad (>=18): {self.mayores}")
        print(f"Menores de edad (<18): {self.menores}")


app = ContadorEdades()
app.procesar()
app.resumen()