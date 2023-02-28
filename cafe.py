# Este NO es un ejercicio del libro, pero se me ocurrió y me pareció una buena idea para practicar y revisar funciones
# Sé que podría hacerse mucho mejor, pero lo estoy haciendo con muchas distracciones y por practicar más que nada
# Pregunta cuánto café quieres y te dice cuantas cucharadas de café y azúcar echar, las medidas no son reales

# Define la función que luego usaremos para las medidas de azúcar en base a cuánto café se eche
def azucar(cafe):
    if cafe == 1:
        print("Vamos a echar poco café, y por tanto poco azúcar.\nMás exactamente, una cucharada.")
    elif cafe == 2:
        print("Vamos a echar una medida normal, por lo que sería una cucharada y media de azúcar.")
    elif cafe == 3:
        print("Vamos a echar bastante café, así que mejor echar dos cucharadas de azúcar.")

# Pregunta y selección
print("Buenos días, cuánto café quieres hoy?")
print("Selecciona (1) para poco, (2) para medio y (3) para mucho")
cafe = int(input())
while True: #Loop para que si el valor no es 1, 2 o 3, vuelva a pedirlo y no crashee 
    if cafe <= 0:
        print("Por favor, introduce un valor válido")
        cafe = int(input())
    elif cafe > 3:
        print("Por favor introduce un valor válido")
        cafe = int(input())
    else:
        break

# Elige el texto en base a la elección y aplica la función del azucar definida al principio del programa
if cafe == 1:
    print("Hagamos poco entonces, echa una cucharada de café")
    azucar(cafe)
elif cafe == 2:
    print("Hagamos una cantidad media, echa cucharada y media de café")
    azucar(cafe)
elif cafe == 3:
    print("Vamos a hacer bastante, echa dos cucharadas de café")
    azucar(cafe)