def accesodiscoteca(edad, dinero, nombre):
    if edad >= 18 and dinero >= 100 and nombre != "jimmy":
        acceso = True
    else:
        acceso = False
    return acceso