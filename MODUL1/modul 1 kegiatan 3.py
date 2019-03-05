def jumlahhurufvokal(x):
    hvokal=("a","i","u","e","o","A","I","U","E","O")
    hitung = 0
    for i in x :
        if i in hvokal:
            hitung+=1
    huruf = len(x)
    return (huruf,hitung)

def jumlahhurufkonsonan(x):
    hvokal="BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    hitung = 0
    for i in x :
        if i in hvokal:
            hitung+=1
    huruf = len(x)
    return (huruf,hitung)
