
def algoSort(arr,n):
    
    for i in range(1,n):
        key = arr[i]
        j= i -1
        
        while j>=0 and (key < arr[j]):
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] =key
        

arr = [64,3,34,8,25,12,22]
n =len(arr)

algoSort(arr,n)

print('Sorted Array ',arr)