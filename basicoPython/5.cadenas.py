def manipular_texto(nombre):
    print(f'Tu nombre en mayusculas {nombre.upper()}')
    print(f'Tu nombre en minusculas {nombre.lower()}')
    print(f'Tu nombre como nombre {nombre.capitalize()}')
    print(f'Tu nombre sin espacios {nombre.strip()}')
    print(f'Tu nombre tiene {len(nombre)} caracteres')
    for acrostico in nombre:
        print(acrostico)

    return nombre    

nombre = manipular_texto(str(input('Digita tu nombre: ')))
print(nombre[0:3])
print(nombre[:3])
print(nombre[3:])
print(nombre[1:7:2])
print(nombre[::])
print(nombre[::-1])
if nombre[::] == nombre[::-1]:
    print(f'La palabra {nombre} es un palindromo')
else:
    print('Es una palabra corriente')