# ejercicio_93
class RegistroNotas:
    def __init__(self):
        self.notas = []

    def registrar(self):
        while True:
            entrada = input("Ingrese nota (o 'fin' para terminar): ")
            if entrada.lower() == 'fin':
                break
            try:
                nota = float(entrada)
                self.notas.append(nota)
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def mostrar_estadisticas(self):
        if not self.notas:
            print("No se ingresaron notas.")
            return

        promedio = sum(self.notas) / len(self.notas)
        print(f"\nNotas registradas: {len(self.notas)}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Nota Mayor: {max(self.notas)}")
        print(f"Nota Menor: {min(self.notas)}")


app = RegistroNotas()
app.registrar()
app.mostrar_estadisticas()
