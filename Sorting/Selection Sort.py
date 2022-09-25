def selection_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array)):
        minimum_index = i
        for j in range(i + 1, len(array)):
            iterations += 1
            if array[minimum_index] > array[j]:
                minimum_index = j
        
        # Swap the found minimum element with 
        # the first element
        if minimum_index != i:
            array[i], array[minimum_index] = array[minimum_index], array[i]

# When array is already sorted
array = [i for i in range(20)]
selection_sort(array)

print(array)
print(iterations)

# when array is shuffled
import random
array = [i for i in range(20)]
random.shuffle(array)

selection_sort(array)

print(array)
print(iterations)

# when array is reverse sorted
array = [i for i in range(20)]
array = array[::-1]

selection_sort(array)
print(array)
print(iterations)