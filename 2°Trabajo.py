class TorreHanoiConPilas:
    def __init__(self, n):
        self.n = n
        self.pila_A = [7,5,3]
        self.pila_B = []
        self.pila_C = []
        self.origen = "A"
        self.auxiliar = "B"
        self.destino = "C"

    def mover_disco(self, origen, destino):
        disco = origen.pop()
        destino.append(disco)
        print(f"Mover disco {disco} de la pila {origen} a la pila {destino}")

    def resolver(self, n, origen, auxiliar, destino):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.resolver(n-1, origen, destino, auxiliar)
            self.mover_disco(origen, destino)
            self.resolver(n-1, auxiliar, origen, destino)

    def resolver_torre_hanoi(self):
        self.resolver(self.n, self.pila_A, self.pila_B, self.pila_C)

n = 3  # Número de discos
torre_hanoi = TorreHanoiConPilas(n)
torre_hanoi.resolver_torre_hanoi()
