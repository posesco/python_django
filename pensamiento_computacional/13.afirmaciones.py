def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, 'No se permiten string vacios'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(f'Este es el error: {e}')

    return primeras_letras


lista = ['Tales', 'Otra cosa', "", 545, 'Ya mero']
print(primera_letra(lista))
