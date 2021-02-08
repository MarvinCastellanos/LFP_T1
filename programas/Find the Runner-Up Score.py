if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    aux=-100
    aux2=-100
    for dato in arr:
        if (dato>=aux and dato is not aux):
            aux2=aux
            aux=dato
        elif(dato>aux2 and dato is not aux):
                aux2=dato
    print(aux2)
                