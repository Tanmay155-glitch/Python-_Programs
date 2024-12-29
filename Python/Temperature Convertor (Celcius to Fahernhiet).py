def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Temperature in Fahrenheit: {fahrenheit}")

if __name__ == "__main__":
    main()