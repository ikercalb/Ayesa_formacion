
n=4
resultado = 1

for i in range(n):
    for j in range(i+1):
        print(resultado**j)
    resultado += 1