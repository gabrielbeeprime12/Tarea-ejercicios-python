# ejercicio_98
class SistemaNotas:
    def __init__(self):
        self.aprobados = 0
        self.reprobados = 0

    def evaluar_grupo(self):
        for i in range(1, 11):
            nota = float(input(f"Ingrese nota del alumno {i} (0-10): "))
            if nota >= 6.0:  # Nota mínima de aprobación
                self.aprobados += 1
            else:
                self.reprobados += 1

    def reporte(self):
        print(f"\n--- ESTADÍSTICAS ---")
        print(f"Aprobados: {self.aprobados} ({(self.aprobados/10)*100}%)")
        print(f"Reprobados: {self.reprobados} ({(self.reprobados/10)*100}%)")

app = SistemaNotas()
app.evaluar_grupo()
app.reporte()