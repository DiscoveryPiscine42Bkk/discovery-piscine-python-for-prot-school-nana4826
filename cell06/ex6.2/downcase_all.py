import sys

def downcase_it(input_string):
    return input_string.lower()

if len(sys.argv) == 2:
   
    result = downcase_it(sys.argv[1])
    print(result)
else:
  
    print("none")
