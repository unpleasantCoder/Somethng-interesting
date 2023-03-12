def bla(*mas):
    n=len(mas)
    fin=[]
    i=0
    for j in range(len(mas[i])):
        k=0
        for b in range(n):
            if b!=i and (mas[i][j] in mas[b]):
                k+=1
                mas[b].remove(mas[i][j])
        if k==(n-1):
            fin.append(mas[i][j])
    print(fin)
bla([1,2,4,'hi'],[1,2,3,4,'hi'],[1,2,3,7,'hi'])