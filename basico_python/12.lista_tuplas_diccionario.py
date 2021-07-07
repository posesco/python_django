def run():
    lista = [1, 2, 3, 4, True, False, 'texto']
    tupla = (1, 2, 3, 4, True, False, 'texto')
    diccionario = {
        'llave1' : lista,
        'llave2' : tupla,
        'llave3' : 3,
        'llave4' : 4,
    }
    for vuelta in diccionario.keys():
        print(vuelta)

    for vuelta in diccionario.values():
        print(vuelta)

    for vuelta in diccionario.items():
        print(vuelta)
if __name__ == '__main__':
    run()