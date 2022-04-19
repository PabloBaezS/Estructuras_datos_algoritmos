def chequeodiccionario(diccionario):
    name = diccionario['nombre']
    if name[0] == "C":
            return False
    if diccionario['precio'] > 300:
        return True
    else:
        return False