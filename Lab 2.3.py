#Student ID: 1201201432
#Student Name: Joyce Hu Xin Yi

temp = float(input("Enter Temperature: "))
unit = input("Enter unit('C' for Celsius or 'F' for Fahrenheit): ")

if unit == 'C' or unit == 'c' :
    newTemp = 9 / 5 * temp + 32
    print("Temperature in Fahrenheit =", newTemp)
elif unit == 'F' or unit == 'f' :
    newTemp = 5 / 9 * (temp - 32)
    print("Temperature in Celsius =", newTemp)
else :
    print("Unknown unit", unit)