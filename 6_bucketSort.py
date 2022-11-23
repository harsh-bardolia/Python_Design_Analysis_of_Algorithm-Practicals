# def bucketSort(array):
#     bucket = []

#     # Create empty buckets
#     for i in range(len(array)):
#         bucket.append([])

#     # Insert elements into their respective buckets
#     for j in array:
#         index_b = int(10 * j)
#         bucket[index_b].append(j)

#     # Sort the elements of each bucket
#     for i in range(len(array)):
#         bucket[i] = sorted(bucket[i])

#     # Get the sorted elements
#     k = 0
#     for i in range(len(array)):
#         for j in range(len(bucket[i])):
#             array[k] = bucket[i][j]
#             k += 1
#     return array


# array = [.42, .32, .33, .52, .37, .47, .51]
# print("Sorted Array in descending order is")
# print(bucketSort(array))



# Another Way :
def bucket_sort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length):
        insertion_sort(buckets[i])
 
    result = []
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        j -= 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = temp
 
 
alist = [45,62,10,23,78,94,56,41,66,13]
sorted_list = bucket_sort(alist)
print('Sorted list: ', end='')
print(sorted_list)