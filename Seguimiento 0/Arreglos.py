def chequeoarreglo(arreglos):
    if len(arreglos) >= 1 and arreglos[0] == arreglos[len(arreglos)-1]:
        return True
    else:
        return False