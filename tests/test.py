import math
from decimal import Decimal as D
from decimal import getcontext
import time
from datetime import datetime

def calcpi(n):
    #Calculate PI
    getcontext().prec = n
    MAX = 10000
    pi = D(0)

    for k in range(MAX):
        pi += D(math.pow(16, -k)) * (D(4/(8*k+1)) - D(2/(8*k+4)) - D(1/(8*k+5)) - D(1/(8*k+6)))
    
    print('PI:', pi)
    pi = int(str(pi)[-1:])
    print('PI:', pi)


milliseconds = int(round(time.time() * 10))
print(milliseconds)

n_3 = 0
e = datetime.now()
newe = e.strftime('%S%f')
mapped = list(map(int, newe))
del mapped[4:-1]
for i in mapped:
    n_3 += i









