def formatRupiah(n):
    a = str(n)
    if len(a) <= 3:
        return  "Rp " + a
    else:
        p = a[-3:]
        q = a[:-3]
        return formatRupiah(q) + "." + p
        print ("Rp " + formatRupiah(q) + "." + p)
