import sys

def main():
    if len(sys.argv) != 2: 
        print("none")
        return

    text = sys.argv[1] 
    if "z" in text: 
        for char in text: 
            if char == "z":
                print("z")
    else:
        print("none")  

if __name__ == "__main__":
    main()
