"""
Module main call will call code_generator.py, generate the
4 digit random number from py and print it.
"""
from main import Kronopi 

if __name__ == "__main__":
    kronopi = Kronopi() # constructor sets timestamp here
    print("the 4 digit number is: ", kronopi.get_n() ," for the timestamp: ", kronopi.get_date())
    
 