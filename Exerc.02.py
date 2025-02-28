def somar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista.pop() + somar_lista(lista)