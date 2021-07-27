def run():
    for incremento in range(10):
        if incremento % 2 != 0:
            continue 
        print(f'# {incremento}')
    print('#################')
    for i in range(10):
        print(f'# {i}')
        if i == 5:
            break


if __name__ == '__main__':
    run()