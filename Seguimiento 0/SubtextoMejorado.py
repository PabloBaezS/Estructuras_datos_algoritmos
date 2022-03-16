texto1 = str(input())
inicial = int(input())
final = int(input())
largo = int(len(texto1))
if final > largo:
    print("Error")
elif inicial > final:
    print("Error2")
else:
    final = texto1[inicial:final+1]
    print(final)