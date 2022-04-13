# Python 3.10.2 UTF-8
# Copyright (c) 2022, Noa Velasco

if __name__ == '__main__':
    # N = int(input())
    # with open('./listcmd.txt', 'r', encoding='utf-8') as f:
    with open('listcmd.txt', 'r', encoding='utf-8') as f:
        lectura = f.read().splitlines()

    def sorting(lista):
        lista.sort()
        return lista

    def popping(lista):
        lista.pop()
        return lista

    def reversing(lista):
        lista.reverse()
        return lista

    def appending(lista, elem):
        lista.append(int(elem))
        return lista

    def removing(lista, elem):
        lista.remove(int(elem))
        return lista

    def inserting(lista, ind, elem):
        lista.insert(int(ind), int(elem))
        return lista

    def printing(lista):
        print(lista)

    list_out = []

    for l in lectura:
        temp = l.split(" ")
        if temp[0] == "insert":
            inserting(list_out, temp[1], temp[2])
        elif temp[0] == "remove":
            removing(list_out, temp[1])
        elif temp[0] == "print":
            printing(list_out)
        elif temp[0] == "append":
            appending(list_out, temp[1])
        elif temp[0] == "sort":
            sorting(list_out)
        elif temp[0] == "pop":
            popping(list_out)
        elif temp[0] == "reverse":
            reversing(list_out)
