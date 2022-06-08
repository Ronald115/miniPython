from antlr4 import *

class Tablas():
    def __init__(self):
        self.tabla = []
        self.nivelActual = -1
    def openScope(self):
        self.nivelActual += 1

    def closeScope(self):

        toPop = []
        for i in range(0, len(self.tabla)):
            if self.tabla[i].nivel == self.nivelActual:
                toPop.append(i)

        for t in toPop[::-1]:
            self.tabla.pop(t)

        self.nivelActual -= 1

    def buscar(self, nombre):
        temp = None
        for i in range(0, len(self.tabla)):
            if self.tabla[i].tok.text == nombre:
                temp = self.tabla[i]
                break

        return temp

    def buscarEnNivelActual(self, nombre):
        found = False
        for i in range(0, len(self.tabla)):
            if (self.tabla[i].tok.text == nombre) and self.tabla[i].nivel == self.nivelActual:
                found = True
                break

        return found

