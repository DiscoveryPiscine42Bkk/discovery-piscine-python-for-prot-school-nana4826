def add_one(number):
 
    number += 1
    return number

def main():

    my_number = 2
    
    print(f"ก่อน: {my_number}")
    
    my_number = add_one(my_number)
    
    print(f"หลัง: {my_number}")

if __name__ == "__main__":
    main()
