def array_of_names(names_dict):
   
    full_names = []
    
    for first_name, last_name in names_dict.items():
   
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    
    return full_names

def main():
  
    names_dict = {
        "john": "doe",
        "jane": "smith",
        "alice": "cooper"
    }
    
    names = array_of_names(names_dict)
    print(names)

if __name__ == "__main__":
    main()
