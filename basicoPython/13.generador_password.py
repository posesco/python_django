import random

def generar_pass():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Y', 'Z']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'x', 'y', 'z']
    simbols = ['＃','＄', '％', '＆', '＊', '？', '＠', '～', '(', ')']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    caracteres = mayus + minus + simbols 
    password = []

    for i in range(20):
        caracter_random = random.choice(caracteres)
        password.append(caracter_random)

    password = ''.join(password)

    return password

def run():
    password = generar_pass()
    print(f'Tu password es: {password}')
    
if __name__ == '__main__':
    run()