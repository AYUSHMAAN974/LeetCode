n=int(input())
row=n
arr=[]
for i in range(n):
    for j in range(row-1,0,-1):
        print(" ",end="")
    row-=1
    
    left=0
    pos=1
    newarr=[]
    for k in range(i+1):
        if k>0 and k<i:
            summ=arr[left]+arr[left+1]
            print(summ,end=" ")
            left+=1
            newarr.insert(pos,summ)
            pos+=1
        else:
            print(1,end=' ')
            newarr.append(1)
    arr=newarr
    print()
