import random
def write_random_numbers_to_file(filename, count):
    random_numbers = [random.randint(1, 500) for _ in range(count)]
    with open(filename, 'w') as file:
        for number in random_numbers:
            file.write(f"{number}\n")
    print(f"{count} random numbers written to {filename}")
def main():
    while True:
        try:
            count = int(input("Enter the number of random numbers to generate (1-1000): "))
            if 1 <= count <= 1000:
                break
            else:
                print("Please enter a number between 1 and 1000.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    filename = "random_numbers.txt"
    write_random_numbers_to_file(filename, count)
if __name__ == "__main__":
    main()

# Matthew Beekman
# Program 2
# 10/31/2024