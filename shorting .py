def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])

print ("-2, 45, 0, 11, -9")
print ("before shorted : ")
data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print("after it has been sorted : ")
print(data)

# https://www.programiz.com/dsa/selection-sort
