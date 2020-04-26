"""
This runner when invoked will call code_generator.py and
get the user their current 

"""
from code_generator import gencode, Kronopi

if __name__ == "__main__":
    kronopi = Kronopi().get_n()
    print("the 4 digit number is: ", kronopi)
