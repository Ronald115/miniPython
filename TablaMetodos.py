from antlr4 import *
from Tablas import Tablas


class TablaMetodos(Tablas):

    class Identificador():
        def __init__(self, tok, decl, nivel, args):
            self.tok = tok
            self.nivel = nivel
            self.declCtx = decl
            self.args = args

        def getArgs(self):
            args = []
            for a in self.args:
                args.append(a.getText())
            return args

        def setArgs(self, args):
            self.args = args

    def insertar(self, id, decl, args):
        met = self.buscarEnNivelActual(id.text)
        if not met:
            ident = self.Identificador(id, decl, self.nivelActual, args)
            self.tabla.insert(0, ident)
        else:
            self.buscar(id.text).setArgs(args)

    def imprimir(self):
        print("----- INICIO TABLA METODOS ------")
        for i in range(0, len(self.tabla)):
            ident = self.tabla[i]
            print("Nombre: " + ident.tok.text + " - " + str(ident.nivel) + " args: " + str(ident.getArgs()))
        print("----- FIN TABLA METODOS ------")
