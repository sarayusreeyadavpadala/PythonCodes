def bubbleSort(n,arr):
    for i in range(n-1):
        swap=0
        for j in range(1,n):
            if arr[j-1]>arr[j]:
                temp=arr[j]
                arr[j]=arr[j-1]
                arr[j-1]=temp
                swap=1
        if swap==0:
            break
    print(arr)
n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
bubbleSort(n,arr)
