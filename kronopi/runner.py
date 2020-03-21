"""
This runner when invoked will call code_generator.py and
get the user their current 

"""
from code_generator import gencode

if __name__ == "__main__":
    ns = gencode()
    print("the 4 digit number is: ", ns)
