from collections import deque

dq = deque()


def editor(n):
    S = ""
    dq.append(S)
    while n != 0:
        entrada = input()
        operacion = int(entrada[0])
        if operacion == 1:
            c = entrada[2:]
            dq.append(dq[-1] + c)

        elif operacion == 2:
            c = int(entrada[2])
            s = dq[-1]
            S = s[:-c]
            dq.append(S)

        elif operacion == 3:
            c = int(entrada[2:])
            s = dq[-1]
            print(s[c - 1])


        elif operacion == 4:
            dq.pop()

        n -= 1
    return ""


a = int(input())

print(editor(a))