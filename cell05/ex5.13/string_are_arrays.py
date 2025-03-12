import sys

def main():
    if len(sys.argv) < 2: 
        print("none")
        return

    for param in sys.argv[1:]:  
        if not param.endswith("ism"):
            print(param + "ism") 

if __name__ == "__main__":
    main()
