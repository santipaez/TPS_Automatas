# AFD: (a|b)*

def AFD(cadena):
    estado = "A" # estado inicial y final
    for simbolo in cadena:
        if simbolo == "a":
            estado = "A" # transición con a
        elif simbolo == "b":
            estado = "A" # transición con b
        else:
            return False # entrada inválida
    return True # estado final

print(AFD("ab")) #True
print(AFD("baa")) #True
print(AFD("abaac")) #False
print(AFD("abcaab")) #False