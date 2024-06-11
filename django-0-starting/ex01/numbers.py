def ft_print_file():
    try:
        with open("numbers.txt", "r") as file:
            content = file.read().strip()
            num_list = content.split(",")
            for num in num_list:
                print(num)
    except FileNotFoundError:
        print("Error: El archivo 'numbers.txt' no se encontró.")
    except IOError:
        print("Error: Error al leer el archivo.")

if __name__ == '__main__':
    ft_print_file()