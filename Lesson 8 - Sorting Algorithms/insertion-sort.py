def insertionSort(input_array): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(input_array)): 
  
        key = input_array[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        
        while j >= 0 and key < input_array[j] : 
                input_array[j + 1] = input_array[j] 
                j -= 1

        input_array[j + 1] = key

    for i in range(len(input_array)):
        print(input_array[i]),
  
  
array = [20, 65, 67, 45, 8, 19] 
insertionSort(array) 
 
  
