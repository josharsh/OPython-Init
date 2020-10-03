def selection_sort(A):

    for i in range(len(A)):
        min_index = i

        for j in range(i+1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
    #swap
    A[i], A[min_index] = A[min_index], A[i]

    for i in range(len(A)):
        print(A[i], end= " ")

# Driver code for above function

array = [85, 34, 18, 4, 60, 21]
selection_sort(array)
