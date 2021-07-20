fibonacci_cache = {}


def fibonacci(valor):

    if valor in fibonacci_cache:
        return fibonacci_cache[valor]
    if valor == 0 or valor == 1:
        return 1

    n_valor = fibonacci(valor - 1) + fibonacci(valor - 2)
    fibonacci_cache[valor] = n_valor
    return n_valor


def run():
    for valor in range(1, 1001):
        print(f'{valor} : {fibonacci(valor)}')


if __name__ == '__main__':
    run()
