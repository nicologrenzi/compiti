trovare_il_maggiore_nella_lista(lista):
    max = 0
    for numero in lista:
        if numero > max:
            max = numero
    print('Il numero più grande della lista passata è ' + str(max))

lista = [9, 33, 1, 3, 2, 4, 22]
maggiore_nella_lista(lista)
