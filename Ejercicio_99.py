# ejercicio_99
class Demografia:
    def __init__(self, total):
        self.total = total
        self.ninos = 0        # 0 - 12
        self.adolescentes = 0 # 13 - 17
        self.adultos = 0      # 18 - 59
        self.mayores = 0      # 60+

    def procesar(self):
        for i in range(1, self.total + 1):
            edad = int(input(f"Edad persona {i}: "))
            if edad <= 12: self.ninos += 1
            elif edad <= 17: self.adolescentes += 1
            elif edad <= 59: self.adultos += 1
            else: self.mayores += 1

    def resultados(self):
        print(f"\nNiños (0-12): {self.ninos}")
        print(f"Adolescentes (13-17): {self.adolescentes}")
        print(f"Adultos (18-59): {self.adultos}")
        print(f"Adultos Mayores (60+): {self.mayores}")

n = int(input("Número de personas a registrar: "))
app = Demografia(n)
app.procesar()
app.resultados()