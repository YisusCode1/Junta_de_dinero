import random
import datetime


class JuntaDeDinero:
    def __init__(self, num_personas, aporte):
        if not 3 <= num_personas <= 20:
            raise ValueError(
                "La cantidad de participantes debe estar entre 3 y 20.")

        if not 50 <= aporte <= 500:
            raise ValueError("El monto a aportar debe estar entre 50 y 500.")

        self.num_personas = num_personas
        self.aporte = aporte
        self.total_aportado = num_personas * aporte
        print(f"La cantidad total a aportar es: {self.total_aportado} soles")

        self.meses = num_personas
        self.participantes = {
            i: self.total_aportado for i in range(1, num_personas + 1)}
        self.ganadores = set()

        self.ejecutar_junta()

    def ejecutar_junta(self):

        for _ in range(self.meses):
            if not self.participantes:
                break
            ganador = self.sortear()
            self.ganadores.add(ganador)

        if len(self.ganadores) < self.num_personas:
            self.verificar_pago_mensual()

        return list(self.ganadores)

    def sortear(self):
        ganador = random.choice(list(self.participantes.keys()))
        del self.participantes[ganador]
        return ganador

    def devolver_colateral(self):
        for participante, colateral in self.participantes.items():
            print(
                f"Se devuelve el colateral de {colateral} soles al participante {participante}.")

    def verificar_pago_mensual(self):
        for participante, colateral in self.participantes.items():
            if participante not in self.ganadores:
                if colateral < self.aporte:
                    del self.participantes[participante]
                else:
                    self.participantes[participante] -= self.aporte


# Ejemplo de uso
if __name__ == "__main__":
    junta = JuntaDeDinero(num_personas=10, aporte=100)
