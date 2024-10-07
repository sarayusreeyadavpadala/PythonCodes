def selectionSort(n,a):
    for i in range(n-1):
        min=i
        for j in range(i,n):
            if a[j]<a[min]:
                temp=a[min]
                a[min]=a[j]
                a[j]=temp
    print(a)
n=int(input())
arr=[]
for i in range(n):
    b=int(input())
    arr.append(b)
selectionSort(n,arr)
