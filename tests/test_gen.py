from kronopi.code_generator import DateSum, TimeSum, sum

def gen_test():
    assert(DateSum().ret() <= 142)
    assert(TimeSum().ret() <= 144)
    assert(sum() <= 45)
    assert(DateSum().ret() >= 0)
    assert(TimeSum().ret() >= 0)
    assert(sum() >= 0)
    print("Tests ran successfully")
    
    