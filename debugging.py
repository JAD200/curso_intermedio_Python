def divisors(num):
    divisors = [i for i in range(1, num + 1) if num %i == 0]

    return divisors

def run():
    while True:
        try:
            num = int(input('Ingrese un numero: '))
            if num < 0:
                raise ValueError('\nPor favor ingrese un numero mayor a cero')
            print(divisors(num))
            print('* * * Termino mi programa * * *')
            break
        except ValueError as ve:
            print(ve)
            print('Debes ingresar un valor valido')


if __name__ == '__main__':
    run()