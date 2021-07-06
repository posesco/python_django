def run():
    LIMITE = 1048576

    contador = 0
    potencia = 2**contador
    while potencia <= LIMITE:
        print(f'2 potencia {contador} es igual a {potencia}')
        contador = contador+1
        potencia = 2**contador
    return True


if __name__ == '__main__':
    run()