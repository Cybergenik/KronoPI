from datetime import datetime
import math
from decimal import Decimal as D
from decimal import getcontext

class Kronopi():
    
    def __init__(self):
        MAX = 10000

    def date_sum(self, date):
        """
        Returns the sum of the current Date of YY + DD + MM. Using datetime library.
        """
        ddate = date.today()
        n = int(ddate.strftime("%y"))
        n += int(ddate.strftime("%d"))
        n += int(ddate.strftime("%m"))
        return n

    def time_sum(self, date):
        """
        Returns the sum of the current Time of HH + MM + SS. Using datetime library.
        """
        tdate = date.now()
        n = int(tdate.strftime("%y"))
        n += int(tdate.strftime("%d"))
        n += int(tdate.strftime("%m"))
        return n

    def calcpi(self, n):
        """
        This function calculates PI to the nth number, its based on the Chudnovsky Algorithm
        https://en.wikipedia.org/wiki/Chudnovsky_algorithm
        the algorithm used is a shorter simplified version
        """
        #Calculate PI
        if n == 0:
            return 3
        else:
            getcontext().prec = n
            MAX = 10000
            pi = D(0)

            for k in range(MAX):
                pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
            
            pi = int(str(pi)[-1:])

        return pi

    def n_sum(self, date):
        """
        This function returns the value of n_3 using seconds milliseconds, adding them
        and returning the value.
        """
        n = 0
        sec = date.now()
        secmil = sec.strftime('%S%f')
        mapped = list(map(int, secmil))
        del mapped[4:-1]
        
        for i in mapped:
            n += i

        return n

    def n_mod(self, n1, n2, n3):
        """
        Takes 3 inputs of the previous ns and returns result of mod 7 on the sum of the 3
        """
        return (n1 + n2 + n3) % 7

    def get_n(self):
        """
        Generates the 4 digit Random number based on the users current time from digits in PI
        returns 4 number string
        """
        date = datetime
        n_1 = self.date_sum(date)
        n_2 = self.time_sum(date)
        n_3 = self.n_sum(date)
        n_4 = self.n_mod(n_1, n_2, n_3)
        n = str(self.calcpi(n_1)) + str(self.calcpi(n_2)) + str(self.calcpi(n_3)) + str(self.calcpi(n_4))
        return n
    

def gencode():
    """
    Generates the 4 digit Random number based on the users current time from digits in PI
    returns 4 number string
    """
    N_1 = DateSum().ret()
    N_2 = TimeSum().ret()
    N_3 = sum()
    N_4 = mod(N_1, N_2, N_3)
    NS = str(calcpi(N_1)) + str(calcpi(N_2)) + str(calcpi(N_3)) + str(calcpi(N_4))
    
    return NS

class DateSum():
    """
    Returns the sum of the current Date of YY + DD + MM. Using datetime library.
    """
    n_1 = 0
    def __init__(self):
        ndate = datetime.today()
        self.n_1 = int(ndate.strftime("%y"))
        self.n_1 += int(ndate.strftime("%d"))
        self.n_1 += int(ndate.strftime("%m"))
    def ret(self):
        return self.n_1        

class TimeSum():
    """
    Returns the sum of the current Time of HH + MM + SS. Using datetime library.
    """
    n_2 = 0
    def __init__(self):
        nnow = datetime.now()
        self.n_2 = int(nnow.strftime("%H"))
        self.n_2 += int(nnow.strftime("%M"))
        self.n_2 += int(nnow.strftime("%S"))
    def ret(self):
        return self.n_2 

def calcpi(n: int):
    """
    This function calculates PI to the nth number, its based on the Chudnovsky Algorithm
    https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    the algorithm used is a shorter simplified version
    """
    #Calculate PI
    if n == 0:
        return 3
    else:
        getcontext().prec = n
        MAX = 10000
        pi = D(0)

        for k in range(MAX):
            pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
        
        pi = int(str(pi)[-1:])

        return pi

def sum():
    """
    This function returns the value of n_3 using seconds milliseconds, adding them
    and returning the value.
    """
    n_3 = 0
    sec = datetime.now()
    secmil = sec.strftime('%S%f')
    
    mapped = list(map(int, secmil))
    del mapped[4:-1]
    
    for i in mapped:
        n_3 += i

    return n_3


def mod(n1, n2, n3):
    """
    Takes 3 inputs of the previous ns and returns result of mod 7 on the sum of the 3
    """
    return (n1 + n2 + n3) % 7
