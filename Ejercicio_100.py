# ejercicio_100
import math


class MenuMatematico:
    def ejecutar(self):
        while True:
            print("\n--- MENÚ MATEMÁTICO ---")
            print(
                "1. Calcular Factorial\n2. Tabla de Multiplicar\n3. Verificar Paridad\n4. Calcular Cuadrado\n5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '5':
                print("¡Hasta luego!")
                break

            if opcion in ['1', '2', '3', '4']:
                num = int(input("Ingrese un número entero: "))

                if opcion == '1':
                    print(
                        f"El factorial de {num} es: {math.factorial(num)}" if num >= 0 else "No existe factorial de negativos.")
                elif opcion == '2':
                    for i in range(1, 11):
                        print(f"{num} x {i} = {num * i}")
                elif opcion == '3':
                    es_par = "Par" if num % 2 == 0 else "Impar"
                    print(f"El número {num} es {es_par}.")
                elif opcion == '4':
                    print(f"El cuadrado de {num} es: {num ** 2}")
            else:
                print("Opción inválida.")


app = MenuMatematico()
app.ejecutar()