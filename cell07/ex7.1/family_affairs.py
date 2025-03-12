def find_the_redheads(family_dict):
    redheads = list(filter(lambda name: family_dict[name] == "red", family_dict))
    
    return redheads

def main():
   
    family_dict = {
        "John": "blonde",
        "Jane": "red",
        "Alice": "brown",
        "Bob": "red",
        "Charlie": "black"
    }
    
    redheads = find_the_redheads(family_dict)
    
    print("Redheads in the family:", redheads)

if __name__ == "__main__":
    main()
