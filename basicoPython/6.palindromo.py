def palindromo(palabra):
    palabra = palabra.replace (' ','')
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False


def run():
    palabra = input('Escribe un palabra: ')
    esPalindromo = palindromo(palabra)
    if esPalindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run() 