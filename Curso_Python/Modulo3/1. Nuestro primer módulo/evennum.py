# Calculo de numeros pares
import sys


def find_even_numbers(n):
    arr = []
    for i in range(n+1):
        if i % 2 == 0:
            arr.append(i)
    return arr


if __name__ == "__main__":
    print(find_even_numbers(int(sys.argv[1])))
