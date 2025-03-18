def saludo(nombre):
    return f"Hola, {nombre}!"

if __name__ == "__main__":
    nombre = input("¿Cuál es tu nombre? ")
    print(saludo(nombre))