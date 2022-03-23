#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

print('\n')
print('EXPOSICION FISICA: BIOMECANICA DEL PARACAIDISMO')
print('')
print('     -*-*-*-*-*-*-*-*-*-*-*-*-*-')
print('     |Problema del paracaidista|')
print('     -*-*-*-*-*-*-*-*-*-*-*-*-*-')

print('')
print('     Language Version : Python 3.XX')
print('     Basado en: rusbel bermudez rivera   ')
print("Por: SARA MARIA CANO | PABLO BAEZ SANTAMARIA")

print('\n')
print('Ingresa tus datos a utilizar para el experimento')
print('')

G = 9.8
t_inicial = 0
v_inicial = 0
idx = 0

resp = 0
m = float(input('Ingresa el valor de la masa del paracaidista en kg: '))
resp2 = int(input("El paracaidista ya abrio el paracaidas? Responde 1: SI | 2: NO  "))
if resp2 == 1:
    c = 5.0
elif resp2 == 2:
    c = 12.5
while resp == 0 or resp == 1:
    print("Deseas modificar el valor del coeficiente de resistencia? 1: SI | 2: NO  ")
    resp = int(input())
    if resp == 1:
        c = float(input('Ingresa el valor del coeficiente de resistencia: '))
        resp = 2

delta_time = float(input('Ingresa el valor del delta a utilizar para los incrementos: '))
t_final = delta_time

last_point = int(input('¿Cuantos segmentos delta quieres analizar?:  ')) * delta_time

#ejes para graficar
x_axys = [t_inicial]
y_axys = [v_inicial]

#Uso del ciclo while
while t_final < last_point:
    v_final = v_inicial
    print('v_{} = {} m/s'.format(idx,round(v_final,4)))
    v_final = v_inicial + (G - ((c/m)*v_inicial)) * (t_final - t_inicial)

    x_axys.append(int(t_final))
    y_axys.append(v_final)
    v_inicial = v_final
    t_inicial = t_final
    t_final += delta_time
    idx += 1

print(x_axys)
print(y_axys)
plt.plot(x_axys,y_axys)
plt.axis([0, 30, 0, 60])
plt.show()