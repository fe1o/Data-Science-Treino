def wgh():
    peso = int(input("Pe$o da carga: "))
    if peso <= 10:
        print("O valor será de R$ 50,00")
    elif peso >= 11 and peso <= 20:
        print("O valor será de R$ 80,00")
    else:
        print("Peso acima do limite, a carga não será aceita.")

wgh()