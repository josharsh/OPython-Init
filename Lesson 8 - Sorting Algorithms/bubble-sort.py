def bubbleSort(input_array):
    
    n = len(input_array) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if input_array[j] > input_array[j+1] : 
                input_array[j], input_array[j+1] = input_array[j+1], input_array[j] 
  
# Driver code to test above 
array = [36, 11, 20, 21, 57, 99, 83, 46] 
  
bubbleSort(array) 
  
for i in range(len(array)): 
    print (array[i]),
