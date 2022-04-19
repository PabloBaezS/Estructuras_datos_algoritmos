def arreglo(arr1,arr2):
    arr = []
    for x in arr1:
        if x in arr2:
            if x not in arr:
                arr.append(x)
    arr.sort()
    return arr