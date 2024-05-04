class Bloque:
    def __init__(self, inicio, fin, parrafo):
        self.inicio = inicio
        self.fin = fin
        self.parrafo = parrafo

    def __str__(self):
        return self.inicio + " " +self.fin + " " + self.parrafo