def imprimir_mensaje (mensaje):
    print('Mensaje especial: ')
    print(f'Escogiste la opcion {mensaje} ')
    print('Estoy aprendiendo a usar funciones! ')

opcion = int(input('Elige un opcion (1 , 2 o 3): '))
if opcion ==1:
    imprimir_mensaje(opcion)
elif opcion ==2:
    imprimir_mensaje(opcion)
elif opcion ==3:
    imprimir_mensaje(opcion)
else:
    print('La cagaste')    

def suma(a, b):
    print(f'Se suman dos numeros {a} + {b}')
    resultado = a + b
    return resultado

sumatoria = suma(12, 21)
print(sumatoria)

