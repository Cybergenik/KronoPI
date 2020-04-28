from datetime import datetime
import math
from decimal import Decimal as D
from decimal import getcontext

class Kronopi:
    MAX = 10000

    def __init__(self):
        self._date = datetime.now()

    def date_sum(self):
        """
        Returns the sum of the current Date of YY + DD + MM.
        """
        return int(f'{int(str(self._date.year)[-2:])}{self._date.day}{self._date.month}')

    def time_sum(self):
        """
        Returns the sum of the current Time of HH + MM + SS.
        """

        return int(f'{self._date.hour}{self._date.minute}{self._date.second}')

    def calcpi(self, n):
        """
        This function calculates PI to the nth number, its based on the Chudnovsky Algorithm
        https://en.wikipedia.org/wiki/Chudnovsky_algorithm
        the algorithm used is a shorter simplified version,
        we add 5 to n because the algorithm is procedural so its sometimes not accurate to the
        exact precision number, so we add 5 for buffer space.
        """
        #Calculate PI
        if n == 0:
            return 3
        else:
            getcontext().prec = n + 5
            pi = D(0)

            for k in range(self.MAX):
                pi += D(math.pow(16, -k)) * (D(4/D(8*k+1)) - D(2/D(8*k+4)) - D(1/D(8*k+5)) - D(1/D(8*k+6)))
            
            pi = int(str(pi)[-5])
        return pi

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
        n_1 = self.date_sum()
        n_2 = self.time_sum()
        n_3 = self.n_sum()
        n_4 = self.n_mod(n_1, n_2, n_3)
        n = f'{self.calcpi(n_1)}{self.calcpi(n_2)}{self.calcpi(n_3)}{self.calcpi(n_4)}'

        return n

    def get_date(self):
        return self._date

    def reset_date(self):
        self._date = datetime.now()
