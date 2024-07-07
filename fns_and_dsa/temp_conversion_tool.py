FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        weather = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").capitalize()

        if weather == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}F is {converted_temperature}C")
        elif weather == 'F':
            converted_temperature = convert_to_fahrenheit(temperature)   
            print(f"{temperature}C is {converted_temperature}F")
        else: 
            print("Invalid weather unit. Please enter 'C' for Celsius to 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()                    
