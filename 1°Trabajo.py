class CRUD:
    def __init__(self):
        self.arreglo = []

    def Menu(self):
        Opcion = int(input("Elija una Opcion:\n  1.Crear\n  2.Mostrar\n  3.Actualizar\n  4.Eliminar\n  5.Salir\n"))
        if Opcion == 1:
            self.create()
        if Opcion == 2:
            self.read()
        if Opcion == 3:
            self.update()
        if Opcion == 4:
            self.delete()
        if Opcion != 5:
            self.Menu()
    def create(self):
        objeto = input("De que quiere su torta\n")
        self.arreglo.append(objeto)
    def read(self):
        print(self.arreglo)
    def update(self):
        inciso = int(input("Que espacio quiere cambiar\n"))
        valor = input("Que quiere poner a cabio\n")
        self.arreglo[inciso-1] = valor
    def delete(self):
        inciso = int(input("Que espacio quiere eliminar\n"))
        self.arreglo.pop(inciso-1)
ejemplo = CRUD()
ejemplo.Menu()

