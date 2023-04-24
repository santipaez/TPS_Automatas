class AFN:
    def __init__(self, estados, simbolos, transiciones, estado_inicial, estados_finales):
        self.estados = estados
        self.simbolos = simbolos
        self.transiciones = transiciones
        self.estado_inicial = estado_inicial
        self.estados_finales = estados_finales

    def acepta(self, cadena):
        estados_actuales = set([self.estado_inicial])
        for simbolo in cadena:
            estados_siguientes = set()
            for estado_actual in estados_actuales:
                if (estado_actual, simbolo) in self.transiciones:
                    estados_siguientes |= set(
                        self.transiciones[(estado_actual, simbolo)])
            estados_actuales = estados_siguientes
        return len(estados_actuales & self.estados_finales) > 0


estados = {0, 1, 2}
simbolos = {'a', 'b'}
transiciones = {(0, 'a'): {0, 1}, (0, 'b'): {0, 1}, (1, 'a'): {
    2}, (1, 'b'): {2}, (2, 'a'): {2}, (2, 'b'): {2}}
estado_inicial = 0
estados_finales = {0, 1, 2}

afn = AFN(estados, simbolos, transiciones, estado_inicial, estados_finales)

cadena = input("Introduce una cadena: ")
if afn.acepta(cadena):
    print("La cadena es aceptada por el AFN.")
else:
    print("La cadena no es aceptada por el AFN.")
