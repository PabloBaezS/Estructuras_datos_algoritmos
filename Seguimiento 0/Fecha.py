class Fecha:
    def __init__(self, d, m, a):
        self.d = d
        self.m = m
        self.a = a

    def string(self):
        return str(self.d) + "-" + str(self.m) + "-" + str(self.a)

    def comparar(self, fecha2):
        f1 = self.d + self.m * 100 + self.a * 1000
        f2 = fecha2.d + fecha2.m * 100 + fecha2.a * 1000
        if f1 == f2:
            return "iguales"
        elif f1 < f2:
            return "antes"
        else:
            return "despues"


d, m, a = map(int, input().split())
f1 = Fecha(d, m, a)

d, m, a = map(int, input().split())
f2 = Fecha(d, m, a)

print(f1.string())
print(f1.comparar(f2))