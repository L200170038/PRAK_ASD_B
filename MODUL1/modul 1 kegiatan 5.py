from math import sqrt as sq
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if n in primaKecil:
        return True
    elif n in bukanPrKecil:
        return False
    else :
        if(n % 2) != 0:
            if(n % 3) != 0:
                if(n % 5) != 0:
                    if(n % 7) != 0:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
