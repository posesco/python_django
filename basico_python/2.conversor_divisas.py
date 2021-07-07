def conversor(tipo_pesos, valor_dolar):
    pesos = float(input (f'Ingrese la cantidad de pesos {tipo_pesos}: '))
    dolares = round(pesos / valor_dolar, 2)
    return dolares
    
menu = """
Bienvenidos al conversor de monedas :)

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """
opcion = int(input(menu))


if opcion == 1:
    resultado = conversor ('Colombianos', 3875)
    print(f'Tiene $ {resultado} USD')
elif opcion ==2:
    resultado = conversor ('Argentinos', 65)
    print(f'Tiene $ {resultado} USD')
elif opcion == 3:
    resultado = conversor ('Mexicanos', 24)
    print(f'Tiene $ {resultado} USD')
else:
    print('Opcion no valida!!')
