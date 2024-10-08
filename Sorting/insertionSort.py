def insertionSort(n,arr):
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            temp=arr[j-1]
            arr[j-1]=arr[j]
            arr[j]=temp
            j=j-1
    print(arr)
n=int(input())
arr=[]
for i in range(n):
    a=int(input())
    arr.append(a)
insertionSort(n,arr)
