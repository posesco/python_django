from functools import reduce
my_list = [i for i in range(1, 11)]
odd = list(filter(lambda x: x%2 !=0, my_list))
squares = list(map(lambda x: x**2, my_list))
all_multiple = reduce(lambda x, y: x*y, my_list)
print(f'Numeros Primos: {odd}')
print(f'Numeros Cuadrados: {squares}')
print(f'Numeros Multiplicados: {all_multiple}')