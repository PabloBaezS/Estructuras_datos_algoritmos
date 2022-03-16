# Funcion que lee cada input y los agrega en un arreglo
caracteres = [str(x) for x in input().split()]
nuevoCaracteres = [i.replace('"', '') for i in caracteres] # remove quote from each element


def permutar(start, end=[]):
    if len(start) == 0:
        print("" . join(end))
    else:
        for i in range(len(start)):
            permutar(start[:i] + start[i + 1:], end + start[i:i + 1])


permutar(caracteres, end=[])