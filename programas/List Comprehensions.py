if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    vector=[]
    aux=[]
    i=1
    
    i=0
    j=0
    k=0
    while(i<=x):
        while(j<=y):
            while(k<=z):
                if((i+j+k) is not n):
                    aux.append(i)
                    aux.append(j)
                    aux.append(k)
                    vector.append(aux)
                    aux=[]
                k+=1
            j+=1
            k=0
        i+=1
        j=0
    print(vector)
                
   
