import math
from decimal import Decimal as D
from decimal import getcontext
'''
This is kind of fucked, but calcpi will test correctly just need to change input to function
TODO:
fix test suite

'''

#def gen_test():
    #test = Kronopi()
    #print(pi)
    #assert(date_sum() <= 142)
    #assert(TimeSum().ret() <= 144)
    #assert(sum() <= 45)
    #assert(DateSum().ret() >= 0)
    #assert(TimeSum().ret() >= 0)
    #assert(sum() >= 0)
    #print("Tests ran successfully")

def calcpi(n):
    """
    This function calculates PI to the nth number, its based on the Chudnovsky Algorithm
    https://en.wikipedia.org/wiki/Chudnovsky_algorithm
    the algorithm used is a shorter simplified version
    """
    #Calculate PI
    MAX = 10000
    real_pi = '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912'
    real_pi = real_pi[:160]
    print(real_pi)
    if n == 0:
        return 3
    else:
        getcontext().prec = n + 5
        pi = D(0)

        for k in range(MAX):
            pi += D(math.pow(16, -k)) * (D(4/D(8*k+1)) - D( 2/D(8*k+4)) - D(1/D(8*k+5)) - D(1/D(8*k+6)))
    i = 0 
    while i != n:
        if real_pi[i:i+1] != str(pi)[i:i+1]:
            print(i ,real_pi[i:i+1], 'false')
        i = i + 1

    pi_num = int(str(pi)[-5])
    return pi_num

n = calcpi(140)
print(n)