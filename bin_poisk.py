# import random
# n=random.randint(6,10)
# b=[0]*n
# for i in range(len(b)):
#     b[i]=random.randint(0,20)
# b=sorted(b)
b=[1, 50, 100,300] 
left=0
# isk=b[random.randint(0,n)]
b=list(set(b))
print(b)
isk=int(input())
right=len(b)
flg=False
while flg==False:
    c=(left+right)//2
    if b[c]>isk:
        right =c
    elif b[c]==isk:
        print(c+1)
        flg=True
    else:
        left =c
