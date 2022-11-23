def selectionSort(array, size):
	
	for i in range(size):
		minj = i

		for j in range(i + 1, size):

			if array[j] < array[minj]:
				minj = j
		(array[i], array[minj]) = (array[minj], array[i])

arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('Sorted Array:')
print(arr)
