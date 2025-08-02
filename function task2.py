import math
try:
    number = float(input("Enter a number: "))

    if number <= 0:
        print("Please enter a number greater than 0 for square root and logarithm.")
    else:
        square_root = math.sqrt(number)
        natural_log = math.log(number)
        sine_value = math.sin(number)

        print(f"\nResults for number {number}:")
        print(f"Square root: {square_root}")
        print(f"Natural logarithm (log base e): {natural_log}")
        print(f"Sine (in radians): {sine_value}")

except ValueError:
    print("Invalid input! Please enter a numeric value.")
