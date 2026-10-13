# ejercicio_97
class Banco:
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    def menu(self):
        while True:
            print("\n--- MENÚ BANCARIO ---")
            print("1. Consultar Saldo\n2. Depositar\n3. Retirar\n4. Salir")
            op = input("Opción: ")

            if op == '1':
                print(f"Saldo actual: ${self.saldo:.2f}")
            elif op == '2':
                monto = float(input("Monto a depositar: "))
                if monto > 0:
                    self.saldo += monto
                    print("Depósito exitoso.")
            elif op == '3':
                monto = float(input("Monto a retirar: "))
                if 0 < monto <= self.saldo:
                    self.saldo -= monto
                    print("Retiro exitoso.")
                else:
                    print("Fondos insuficientes o monto no válido.")
            elif op == '4':
                print("Gracias por utilizar nuestros servicios.")
                break

app = Banco(100.0) # Saldo inicial $100
app.menu()