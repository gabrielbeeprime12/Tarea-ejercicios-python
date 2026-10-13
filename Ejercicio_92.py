# ejercicio_92
import math

class CalculadoraAreas:
    def ejecutar(self):
        while True:
            print("\n--- ÁREAS DE FIGURAS ---")
            print("1. Círculo\n2. Cuadrado\n3. Triángulo\n4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '4':
                break
            elif opcion == '1':
                r = float(input("Ingrese el radio: "))
                print(f"Área del Círculo: {math.pi * r**2:.2f}")
            elif opcion == '2':
                l = float(input("Ingrese el lado: "))
                print(f"Área del Cuadrado: {l * l:.2f}")
            elif opcion == '3':
                b = float(input("Ingrese la base: "))
                h = float(input("Ingrese la altura: "))
                print(f"Área del Triángulo: {(b * h) / 2:.2f}")
            else:
                print("Opción no válida.")

app = CalculadoraAreas()
app.ejecutar()