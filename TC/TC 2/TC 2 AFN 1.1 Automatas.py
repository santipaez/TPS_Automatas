# AFN: (a|b)*

def AFN(cadena):
    estado = "A" # estado inicial
    for simbolo in cadena:
        if simbolo == "a":
            estado = "B" # transición con a
        elif simbolo == "b":
            estado = "C" # transición con b
        else:
            return False # entrada inválida
    return True # estado final

print(AFN("ab")) #True
print(AFN("bbbb")) #True
print(AFN("abaac")) #False
print(AFN("abcaab")) #False