#10/10/23
class Arbol(object):
    def __init__(self):
        self.der = None
        self.izq = None
        self.dato = None

raiz = Arbol()
raiz.dato = 'Raiz'
raiz.izq = Arbol()
raiz.izq.dato = 'Izquierda'
raiz.der = Arbol()
raiz.der.dato = 'Derecha'

raiz.izq.izq = Arbol()
raiz.izq.izq.dato = 'Izquierda 2'
raiz.izq.der = Arbol()
raiz.izq.der.dato = 'Izquierda - Derecha'