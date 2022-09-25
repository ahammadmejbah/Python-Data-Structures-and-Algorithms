def bubble_sort(array):
    n=len(array)
    for i in range(0,n):
        for j in range(0,n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j] # swap

# optimized bubble sort does not increase or decrease asymtotic notations
# however number of iterations can be reduced to some extent
def optimized_bubble_sort(array):
    global iterations
    iterations = 0
    for i in range(len(array) - 1):
        swapped = False
        for j in range(len(array) - 1):
            iterations += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        # if no swapping is performed that means sorting is complete
        # hence break out of the loop
        if not swapped:          
            break

# elements are already sorted
array = [i for i in range(1, 20)]

optimized_bubble_sort(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
print(iterations)

import random
# elements are randomly shuffled
array = [i for i in range(1, 20)]
random.shuffle(array)

optimized_bubble_sort(array)
# 20 shuffled elements need 324 iterations approx = n * n
print(iterations)

# elements are reverse sorted
array = [i for i in range(1, 20)]
# reversing the array
array = array[::-1]

optimized_bubble_sort(array)
# 20 REVERSE sorted elements need 324 iterations approx = n * n

print(iterations)