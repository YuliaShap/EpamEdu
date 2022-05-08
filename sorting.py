#Bubble Sort
def bubble_sort(arr):
    count = 0
    need_iteration = 'true'
    while need_iteration == 'true':
        need_iteration = 'false'
        for i in range(len(arr)):
            for j in range(0, len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    need_iteration = 'true'
                    count +=1
    print("The number of permutations is", count)

library_num = [124,235,456,123,756,476,285,998,379,108]
print("Initial array:", library_num)
bubble_sort(library_num)
print("Sorted array:", library_num)


#Insertion sort
def insertion_sort(arr):
    count = 0
    for i in range(1, len(arr)):
        key_item = arr[i]
        j = i - 1
        while j >= 0 and key_item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key_item
    print("The number of permutations is", count)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
insertion_sort(library_num)
print("Sorted array:", library_num)

#Selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
selection_sort(library_num)
print("Sorted array:", library_num)

#Heapsort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, len(arr), i)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
heap_sort(library_num)
print("Sorted array:", library_num)

#Merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mean = len(arr) // 2
        left_arr = arr[:mean]
        right_arr = arr[mean:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        i = j = k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
merge_sort(library_num)
print("Sorted array:", library_num)

#Quicksort
def partition(arr, left, right):
    i = (left - 1)  # index of smaller element
    key = arr[right]  # a key element

    for j in range(left, right):
        if arr[j] < key:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return (i + 1)


def quick_sort(arr, left, right):
    if left < right:
        key_index = partition(arr, left, right)
        quick_sort(arr, left, key_index - 1)
        quick_sort(arr, key_index + 1, right)


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
quick_sort(library_num, 0, len(library_num) - 1)
print("Sorted array:", library_num)

#Radix sort
def counting_sort(arr, place):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Determine count of elements
    for i in range(0, size):
        index = arr[i] // place
        count[index % 10] += 1

    # Determine cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in the correct place
    i = size - 1
    while i >= 0:
        index = arr[i] // place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    max_item = max(arr)
    place = 1
    while max_item // place > 0:
        counting_sort(arr, place)
        place *= 10


library_num = [124, 235, 456, 123, 756, 476, 285, 998, 379, 108]
print("Initial array:", library_num)
radix_sort(library_num)
print("Sorted array:", library_num)