def greetings(name="noble stranger"):
    
    if not isinstance(name, str):
        print("Error: The name must be a string.")
    else:
        print(f"Hello, {name}!")

if __name__ == "__main__":
    greetings()  
