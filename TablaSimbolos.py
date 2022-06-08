from antlr4 import *
from Tablas import Tablas

class TablaSimbolos(Tablas):
    class Identificador():
        def __init__(self, tok, decl, nivel):
            self.tok = tok
            self.nivel = nivel
            self.declCtx = decl


    def insertar(self, id, decl):
        i = self.Identificador(id, decl, self.nivelActual)
        self.tabla.insert(0, i)

    def imprimir(self):
        print("----- INICIO TABLA SIMBOLOS------")
        for i in range(0, len(self.tabla)):
            s = self.tabla[i]
            print("Nombre: " + s.tok.text + " - " + str(s.nivel))

        print("----- FIN TABLA SIMBOLOS------")