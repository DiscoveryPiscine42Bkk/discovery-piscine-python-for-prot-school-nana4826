import sys

def shrink(text):
    print(text[:8]) 

def greet(name):
    print(f"Hello, {name}!")

def main():
    if len(sys.argv) < 2:
        print("ระบุพารามิเตอร์")
        return
    
    text = sys.argv[1] 
    
    shrink(text)
    
    greet(text)

if __name__ == "__main__":
    main()
