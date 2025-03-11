def play_with_arrays(arr):

    filtered_arr = [x for x in arr if x > 5]
    
    unique_arr = list(set(filtered_arr))
    

    print(unique_arr)

original_array = [2, 8, 9, 48, 6, 22, -12, 2]
play_with_arrays(original_array)
