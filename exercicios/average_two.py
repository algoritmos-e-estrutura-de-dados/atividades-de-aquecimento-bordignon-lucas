a = float(input())
b = float(input())
c = float(input())

gradeAweight = 2
gradeBweight = 3
gradeCweight = 5

media = (((gradeAweight * a) + (gradeBweight * b) + (gradeCweight * c))) / (gradeAweight + gradeBweight + gradeCweight)
print("MEDIA = %0.1f"%media)