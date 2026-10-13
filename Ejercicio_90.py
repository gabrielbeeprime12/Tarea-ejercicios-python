#ejercicio_90
class TablaMultiplicar:
    def generar_tabla(self, numero):
        print(f"\n--- Tabla del {numero} ---")
        for i in range(1, 11):
            print(f"{numero} x {i} = {numero * i}")

    def iniciar(self):
        while True:
            num = int(input("\nIngrese un número para ver su tabla: "))
            self.generar_tabla(num)

            continuar = input("¿Desea consultar otra tabla? (s/n): ").lower()
            if continuar != 's':
                print("¡Hasta luego!")
                break


app = TablaMultiplicar()
app.iniciar()