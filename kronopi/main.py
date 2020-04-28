from datetime import datetime
import math
from decimal import Decimal as D
from decimal import getcontext

class Kronopi:
    MAX = 10000

    def __init__(self):
        """
        Setting Date and PI
        """
        self._date = datetime.now()
        self._pi = self.gen_pi()

    def gen_pi(self):
        """
        This function calculates PI to the 200th decimal number, its based on the Chudnovsky Algorithm
        https://en.wikipedia.org/wiki/Chudnovsky_algorithm
        the algorithm used is a shorter simplified version, the reason we go to 200 is because the highest
        number we can get from the users time is 144, and we add a bit of buffer space. Since the algorithm 
        is procedural and isn't accurate up to the perc number.
        """

        #Setting Decimal number to compute pi to
        getcontext().prec = 200
        pi = D(0)
        # D is Decimal!
        for k in range(self.MAX):
            pi += D(math.pow(16, -k)) * (D(4/D(8*k+1)) - D(2/D(8*k+4)) - D(1/D(8*k+5)) - D(1/D(8*k+6)))
        
        #Removin the dot, so we don't index it    
        pi = f'{pi}'.replace('.','')
        
        return pi

    def date_sum(self):
        """
        Returns the sum of the current Date of YY + DD + MM.
        """

        return int(str(self._date.year)[-2:]) + self._date.day + self._date.month 

    def time_sum(self):
        """
        Returns the sum of the current Time of HH + MM + SS.
        """

        return self._date.hour + self._date.minute + self._date.second

    def n_sum(self):
        """
        This function returns the value of the users seconds milliseconds (12.34), adding them
        and returning the value.
        """

        n = 0
        sec_mil = f'{self._date.second}{str(self._date.microsecond)[:2]}' 

        for i in sec_mil:
            n += int(i)

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

        #We reinitialize _date because 
        #self._date = datetime.now()
        n_1 = self.date_sum()
        n_2 = self.time_sum()
        n_3 = self.n_sum()
        n_4 = self.n_mod(n_1, n_2, n_3)
        n = f'{self._pi[n_1]}{self._pi[n_2]}{self._pi[n_3]}{self._pi[n_4]}'

        return n

    def get_date(self):

        return self._date

    def reset_date(self):

        self._date = datetime.now()
