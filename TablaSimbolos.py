from antlr4 import *


class TablaSimbolos():

    def __init__(self):
        self.tabla = []
        self.nivelActual = -1

    class Identificador():
        def __init__(self, tok, decl, nivel):
            self.tok = tok
            self.nivel = nivel
            self.declCtx = decl

        def getNivel(self):
            return self.nivel

    def insertar(self, id, decl):
        i = self.Identificador(id, decl, self.nivelActual)
        self.tabla.insert(0, i)

    def buscar(self, nombre):
        temp = None

        for i in range(0,len(self.tabla)):
            if self.tabla[i].tok.text == nombre:
                temp = self.tabla[i]
                break

        return temp

    def openScope(self):
        self.nivelActual += 1

    def closeScope(self):

        toPop = []
        for i in range(0,len(self.tabla)):
            if self.tabla[i].nivel == self.nivelActual:
                toPop.append(i)

        for t in toPop[::-1]:
            self.tabla.pop(t)

        self.nivelActual -= 1

    def imprimir(self):
        print("----- INICIO TABLA ------")

        for i in range(0, len(self.tabla)):
            s = self.tabla[i]
            print("Nombre: " + s.tok.text + " - " + str(s.nivel))
        
        print("----- FIN TABLA ------")