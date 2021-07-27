def factorial(valor):
    print(valor)
    if valor == 1:
        return 1

    return valor * factorial(valor - 1)
     

def run():
    valor = int(input('Digita un numero: '))
    print(f'El factorial de {valor} es {factorial(valor)}')
    
if __name__ == '__main__':
    run()