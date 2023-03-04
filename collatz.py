# El programa de Collatz, tema 3
# La verdad, me ha costado mucho este ejercicio porque no caía en como usar el valor retornado como valor introductorio
# Lo que si que estoy bastante orgulloso de lo limpio y claro que ha quedado (a mi opinión)

# Define la función de Collatz
def collatz(numero):
    if numero % 2 == 0:
        print(numero // 2)
        return numero // 2
    else:
        print(3 * numero + 1)
        return 3 * numero + 1

# Toma el Input del usuario y si no es entero devuelve un error y vuelve a pedir que introduzcas el valor
while True:
    try:
        numero = int(input())
        break
    except ValueError:
        print("Por favor, introduce un número entero")

# Hasta que el valor no sea 1, reproduce Collatz
while numero != 1:
    numero = collatz(numero)