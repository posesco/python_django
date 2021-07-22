def division(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(f'Este es el error: {e}')
        return lista


lista = list(range(10))
divisor = 0

print(division(lista, divisor))