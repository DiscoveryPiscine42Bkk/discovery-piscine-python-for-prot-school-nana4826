import sys

def main():
    
    param_count = len(sys.argv) - 1

    if param_count == 0:
        print("none")
    else:
        print(f"parameters: {param_count}")
        for param in sys.argv[1:]:  
            print(f"{param} {len(param)}")

if __name__ == "__main__":
    main()
