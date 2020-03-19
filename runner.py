"""
This runner when invoked will call code_generator.py and
get the user their current 

"""
from tests.test_gen import main
from code_generator import gencode 

if __name__ == "__main__":
    ns = gencode()
    type(ns)
    print("the 4 digit number is: ", ns)

def runtests():
    main()
    print('Tests ran successfully')


