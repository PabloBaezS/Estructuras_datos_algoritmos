def sumaGrupos(numsOk: list,mult5: list, mult3: list, meta1: int, meta2: int):
    if len(numsOk) == 0:
        return True
    cont = 0
    list1 = []
    list2 = []
    while cont < len(numsOk):
        if meta1 == meta2:
            return True
        else:
            return False


def sumaGruposAux(nums) -> int:
    result = 0
    cont = 0
    while cont < len(nums):
        result = result + nums[cont]
        cont += 2
    return result


def sumaGruposAux2(nums) -> int:
    result = 0
    cont = 1
    while cont < len(nums):
        result = result + nums[cont]
        cont += 2
    return result


n = int(input())
numsOk = [0] * n
for i in range(n):
    numsOk[i] = int(input())
numsOk.sort()
cont = 0
numsOk = []
mult5 = []
mult3 = []
while cont < len(numsOk):
    if numsOk[cont] % 5 == 0 and cont < len(numsOk):
        mult5.insert(0, numsOk[cont])
        cont += 1
    if numsOk[cont] % 3 == 0 and cont < len(numsOk):
        mult3.insert(0, numsOk[cont])
        cont += 1
    else:
        numsOk.insert(0, numsOk[cont])
        cont += 1
mult5.sort()
mult3.sort()
print(mult5)

