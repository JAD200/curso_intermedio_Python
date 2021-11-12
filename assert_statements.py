def divisors(num):
    divisors = [i for i in range(1, num + 1) if num %i == 0]
    return divisors

def run():
    num = input('Ingrese un numero: ')
    assert num.isdecimal(), 'Debes ingresar un numero mayor a cero'
    # assert num.isnumeric(), 'Debes ingresar un numero'
    print(divisors(int(num)))
    print('* * * Termino mi programa * * *')


if __name__ == '__main__':
    run()