
from math import pi

figure = input()

area = 0

if figure == 'square' :
    a = float(input())
    area = a * a

elif figure == 'rectangle' :
    a = float(input())
    b = float(input())
    area = a * b

elif figure == 'circle' :
    r = float(input())
    area = pi * (r ** 2)

elif figure == 'triangle' :
    a = float(input())
    b = float(input())
    area = (a * b)/2

else:
    print("Невалиден тип фигура!")

print(f'{area:.3f}')
