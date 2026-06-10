
choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    celsius = int(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit is:", fahrenheit)

elif choice == 2:
    fahrenheit = int(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius is:", celsius)

else:
    print("Invalid choice")
