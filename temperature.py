#def celsius_to_fahrenheit(celsius):
#    fahrenheit = (celsius * 9/5) + 32
#    return fahrenheit

#celsius = float(input("Enter temperature in celsius"))

#result = celsius_to_fahrenheit(celsius)
#print("temperature in fahrenheit is", result)


#def celsius_to_fehrenheit(celsius):
    #fehrenheit = (celsius * 9/5) +32
   # return fehrenheit

#celsius = float(input("enter temperature in celsius: "))
#result = celsius_to_fehrenheit(celsius)
#print("temperature in fehrenheit is", result)

def calculate_average(a , b , c):
    average = (a + b + c) / 3
    return average

a = float(input("ENTER FIRST NUMBER: "))
b = float(input("ENTER SECOND NUMBER: "))
c = float(input("ENTER THIRD NUMBER: "))

result = calculate_average(a , b , c)
print("the average of the three numbers is", result)