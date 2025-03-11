# play_with_arrays.py

def main():

    original_array = [2, 6, 8, 10, 8, 12, 14, 16]
    
    new_array = [x + 2 for x in original_array]
    
    print("Original array:", original_array)
    print("New array:", new_array)

if __name__ == "__main__":
    main()
