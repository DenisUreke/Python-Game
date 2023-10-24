import random

def getlotto():
    
    lotto_set = []
    i = 0
    
    while i < 7:
        number = random.randint(1,35)
        if number in lotto_set:
            continue
        else:
            lotto_set.append(number)
            i += 1
    
    return lotto_set

#a = getlotto()

#print(a)
        
        
        