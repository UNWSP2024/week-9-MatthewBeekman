with open('numbers.txt', 'w') as file:
    file.write('10\n')
    file.write('20\n')
    file.write('30\n')
    file.write('40\n')
def calculate_total(filename):
    total = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                try:
                    number = int(line.strip())
                    total += number
                except ValueError:
                    print(f"ValueError: Could not convert line to number: '{line.strip()}'")
    except IOError:
        print(f"IOError: Could not read file: {filename}")
    return total
if __name__ == "__main__":
    filename = 'numbers.txt'
    total = calculate_total(filename)
    print(f"The total of the numbers is: {total}")

    # Matthew Beekman
    # Program 3
    # 10/31/2024
