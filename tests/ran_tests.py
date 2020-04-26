from datetime import datetime

def sum():
    """
    This function returns the value of n_3 using seconds milliseconds, adding them
    and returning the value.
    """
    n_3 = 0
    sec = datetime.now()
    secmil = sec.strftime('%S%f')
    print(secmil)
    print(type(secmil))
    mapped = list(map(int, secmil))
    print(mapped)
    help(mapped)
    print(type(mapped))

    del mapped[4:-1]
    
    for i in mapped:
        n_3 += i

    return n_3

print(sum())