numeros = list(map(str, input().split(" ")))
m = numeros[0]
n=numeros[1]
palabrasr = list(map(str, input().split(" ")))
palabrasn = list(map(str, input().split(" ")))
contador =0
if m<n:
    print("No")
else:
    for i in palabrasr:
        for j in palabrasn:
            if i==j:
                contador+=1
                break
if contador == len(palabrasn):
    print("Si")
else:
    print("No")