def count_names_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            file.write('Matthew')
            names = file.readlines()
            names = [name.strip() for name in names if name.strip()]
            return len(names)
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return 0
if __name__ == "__main__":
    file_path = 'names.txt'
    number_of_names = count_names_in_file(file_path)
    print(f"The number of names in '{file_path}' is: {number_of_names}")

# Matthew Beekman
# Program 1
# 10/31/2024