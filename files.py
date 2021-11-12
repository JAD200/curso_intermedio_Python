def read():
    numbers = []
    # Encoding='utf-8 is for characters in spanish'
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)


def write():
    names = ["Facundo", "Gregorio", "Marta", "Susana", "Jose", "Rocío"]
    with open('./files/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print(names)


def run():
    write()


if __name__ == '__main__':
    run()