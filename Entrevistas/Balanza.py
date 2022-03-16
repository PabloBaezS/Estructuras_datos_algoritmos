#Divide el arreglo
def sumaGrupos(nums : list, meta1 : int, meta2 : int):
    if len(nums) == 0:
        return True
    cont = 0
    list1 = []
    list2 = []
    while cont < len(nums):
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
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
nums.sort()
print(sumaGrupos(nums, sumaGruposAux(nums), sumaGruposAux2(nums)))