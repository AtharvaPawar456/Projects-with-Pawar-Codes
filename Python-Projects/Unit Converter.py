# Unit Converter

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Test the unit converter
temperature_celsius = float(input("Enter temperature in Celsius: "))
temperature_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
print("Temperature in Fahrenheit:", temperature_fahrenheit)

temperature_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temperature_celsius = fahrenheit_to_celsius(temperature_fahrenheit)
print("Temperature in Celsius:", temperature_celsius)



'''
=================================
Test Case:
=================================

Enter temperature in Celsius: 25
Temperature in Fahrenheit: 77.0
Enter temperature in Fahrenheit: 68
Temperature in Celsius: 20.0

'''