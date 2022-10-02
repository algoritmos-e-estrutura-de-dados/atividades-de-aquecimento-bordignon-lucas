import math

a = float(input())
b = float(input())
c = float(input()) 
pi = 3.14159;

triangulo = (a * c)/2  
circulo = pi * math.pow(c,2)
trapezio = ((a + b)/2) * c
quadrado = b * b
retangulo = a * b



print('TRIANGULO: %0.3f'%triangulo)
print('CIRCULO: %0.3f'%circulo)
print('TRAPEZIO: %0.3f'%trapezio)
print('QUADRADO: %0.3f'%quadrado)
print('RETANGULO: %0.3f'% retangulo)

# Professor, esse exercicio roda normal aqui no vsCode, porém esse mesmo codigo quando vou dar submit nele no beecrowd, dá um runTimeError
# ValueError: could not convert string to float: *******
# Tentei procurar por soluções a respeito desse erro e fazer alterações no codigo, mas não consegui resolver esse problema no site.