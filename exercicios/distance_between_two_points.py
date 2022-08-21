import math

x1 = float(input('X1: '))
y1 = float(input('Y2: '))
x2 = float(input('X2: '))
y2 = float(input('Y2: '))

distance = math.sqrt((pow(x2-x1,2)) + (pow(y2-y1,2)))


print('%0.4f'%distance)

# Esse exercicio também ocorreu o mesmo que o exercicio area.py, roda normal aqui porém no beecrowd ele dá runTimeError
# Traceback (most recent call last):
# File "/judge/judge-cd2ecea4e9b245659b8e31d6ae3d7fc6.d/Main.py", line 3, in <module>
# x1 = float(input('X1: '))
# ValueError: could not convert string to float: *******