if __name__ == '__main__':
    N = int(input())
    list=[]
    i=1
    while i<=N:
        entrada=input().split()
        if(entrada[0]=='print'):
            print(list)
        if(entrada[0]=='insert'):
            list.insert(int(entrada[1]),int(entrada[2]))
        if(entrada[0]=='append'):
            list.append(int(entrada[1]))
        if(entrada[0]=='sort'):
            list.sort()
        if(entrada[0]=='pop'):
            list.pop()
        if(entrada[0]=='reverse'):
            list.reverse()
        if(entrada[0]=='remove'):
            list.remove(int(entrada[1]))
        i+=1
