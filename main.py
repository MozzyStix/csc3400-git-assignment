import calculator

def main():
    while True:
        print("\nCalculator ->")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("0. Exit")

        choice = input("Enter choice (0-6): ")

        if choice == "0":
            break

        try:
            if choice in ["1", "2", "3", "4", "5"]:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == "1":
                    print(calculator.add(x, y))
                elif choice == "2":
                    print(calculator.subtract(x, y))
                elif choice == "3":
                    print(calculator.multiply(x, y))
                elif choice == "4":
                    print(calculator.divide(x, y))
                elif choice == "5":
                    print(calculator.power(x, y))

            elif choice == "6":
                x = float(input("Enter number: "))
                print(calculator.square_root(x))

            else:
                print("Invalid choice, please try again.")

        except ValueError as e:
            print("Error: ", e)

if __name__ == "__main__":
    main()