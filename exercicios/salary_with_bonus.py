empName = (input())
fixedSalary = float(input())
salesMade = float(input())

totalSalary = fixedSalary + (15/100 * salesMade)

print("TOTAL = R$ %0.2f" %totalSalary)