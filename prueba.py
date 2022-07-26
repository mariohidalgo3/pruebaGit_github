def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de moneda 💰

1 - Pesos colombianos
2 - Pesos chilenos
3 - Pesos mexicanos

Elige una opcion: """

opcion = input(menu) #recuerda lo que ingresa el usuario es siempre texto

if opcion == "1":
    conversor("colombianos", 3875)
elif opcion == "2":
    conversor("chilenos", 924.90)
elif opcion == "3":
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción valida, por favor")
