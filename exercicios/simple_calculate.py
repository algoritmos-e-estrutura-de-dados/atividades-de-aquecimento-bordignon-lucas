linha = input().split(' ')
linhatwo = input().split(' ')

productOneCode, unitsProductOne, productOneUnitPrice = linha
productTwoCode, unitsProductTwo, productTwoUnitPrice = linhatwo

calculo = (float(productOneUnitPrice) * int(unitsProductOne)) + (float(productTwoUnitPrice) * int(unitsProductTwo))

print("VALOR A PAGAR: R$ %0.2f"%calculo)