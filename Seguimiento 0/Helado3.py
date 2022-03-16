tempActual = int(input())
edad = int(input())
if(tempActual > 27 and edad >= 18):
    money = int(input())
    if(money > 5):
        print("Comprar helado cerveza")
    else:
        print("Lo sentimos estas pobre")
else:
    print("Lo sentimos juventud")