"""
This runner when invoked will call code_generator.py and
get the user their current 

"""
from code_generator import Kronopi
from time import sleep
from datetime import datetime 

if __name__ == "__main__":
    kronopi = Kronopi()
    print("the 4 digit number is: ", kronopi.get_n() ," for the timestamp: ", kronopi.get_date())
    
