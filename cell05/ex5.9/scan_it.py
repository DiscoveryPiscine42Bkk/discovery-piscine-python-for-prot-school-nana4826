import sys

def scan_it(keyword, text):
    count = text.count(keyword) 
    return str(count) if count > 0 else "none"  
def main():
    if len(sys.argv) != 3: 
        print("none")
    else:
        keyword = sys.argv[1]  
        text = sys.argv[2]  
        print(scan_it(keyword, text))  
if __name__ == "__main__":
    main()
