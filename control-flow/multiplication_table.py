try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")