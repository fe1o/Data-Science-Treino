def vert():
    wrd = str(input("Digite a palavra a ser verticalizada: "))
    print("|Verticalizando|")
    print("----------------")
    for n in range(0, len(wrd)):
        #strings podem ser tratados como listas, logo conseguimos printar na tela usando o formato de lista
        print(wrd[n])

vert()