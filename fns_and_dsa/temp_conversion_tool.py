FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR ) + 32

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def main():
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit?(C/F):").upper()
    if unit == "C":
        fahrenheit = convert_to_fahrenheit(temp)
        print(f"{temp}°C {fahrenheit}°F")
    elif unit == "F":
        celsius = convert_to_celsius(temp)
        print(f"{temp}°C is {celsius}°C")
    else:
        print("Invalid input, please enter C or F")
if __name__ == "__main__":
    main()

