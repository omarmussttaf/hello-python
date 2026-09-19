def calculate_average(a , b , c):
    average = (a + b + c) / 3
    return average

a = float(input("ENTER FIRST NUMBER: "))
b = float(input("ENTER SECOND NUMBER: "))
c = float(input("ENTER THIRD NUMBER: "))

result = calculate_average(a , b , c)
print("the average of the three numbers is", result)