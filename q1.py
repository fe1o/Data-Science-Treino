def amp():
    listLen = int(input("List lenght: "))
    lista = []  # Evite usar "list" como nome de variável, pois sobrescreve a função built-in list()
    x = 0
    
    while x < listLen:  # Simplificado: x < listLen em vez de x <= (listLen - 1)
        numero = int(input("List number: "))
        lista.append(numero)  # Adiciona o número ao final da lista
        x += 1
    
    print("The amplitude of the list is: ", max(lista) - min(lista))  # Para ver o resultado
amp()