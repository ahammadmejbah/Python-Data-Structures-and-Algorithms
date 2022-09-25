def insertion_sort(array):
    global iterations
    iterations = 0
    for i in range(1, len(array)):
        current_value = array[i]
        for j in range(i - 1, -1, -1):
            iterations += 1
            if array[j] > current_value:
                array[j], array[j + 1] = array[j + 1], array[j] # swap
            else:
                array[j + 1] = current_value
                break

# elements are already sorted
array = [i for i in range(1, 20)]

insertion_sort(array)
# 20 ALREADY sorted elements need 18 iterations approx = n
print(array)
print(iterations)

import random
# elements are randomly shuffled
array = [i for i in range(1, 20)]
random.shuffle(array)

insertion_sort(array)
# 20 shuffled elements need 324 iterations approx = n * n
print(array)
print(iterations)

# elements are reverse sorted
array = [i for i in range(1, 20)]
# reversing the array
array = array[::-1]

insertion_sort(array)
# 20 REVERSE sorted elements need 324 iterations approx = n * n

print(array)
print(iterations)