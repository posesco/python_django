def manipularTexto(nombre):
    print(f'Tu nombre en mayusculas {nombre.upper()}')
    print(f'Tu nombre en minusculas {nombre.lower()}')
    print(f'Tu nombre como nombre {nombre.capitalize()}')
    print(f'Tu nombre sin espacios {nombre.strip()}')
    print(f'Tu nombre tiene {len(nombre)} caracteres')
    for acrostico in nombre:
        print(acrostico)

manipularTexto(str(input('Digita tu nombre: ')))