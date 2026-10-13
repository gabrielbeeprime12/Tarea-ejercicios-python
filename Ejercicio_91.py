# ejercicio_91
class Calculadora:
    def ejecutar(self):
        while True:
            print("\n--- CALCULADORA ---")
            print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '5':
                print("Saliendo de la calculadora...")
                break

            if opcion in ['1', '2', '3', '4']:
                a = float(input("Ingrese primer número: "))
                b = float(input("Ingrese segundo número: "))

                if opcion == '1': print(f"Resultado: {a + b}")
                elif opcion == '2': print(f"Resultado: {a - b}")
                elif opcion == '3': print(f"Resultado: {a * b}")
                elif opcion == '4':
                    print(f"Resultado: {a / b}" if b != 0 else "Error: División por cero")
            else:
                print("Opción inválida.")

app = Calculadora()
app.ejecutar()