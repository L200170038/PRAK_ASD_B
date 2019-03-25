class MhsTifUMS(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku

c0 = MhsTifUMS("Alfian", 10, "Sukoharjo", 240000)
c1 = MhsTifUMS("Eko", 51, "Boyolali", 230000)
c2 = MhsTifUMS("Mira", 2, "Mojokerto", 250000)
c3 = MhsTifUMS("Yoga", 18, "Palur", 235000)
c4 = MhsTifUMS("Susi", 4, "Bojonegoro", 240000)
c5 = MhsTifUMS("Rima", 31, "Ngruki", 250000)
c6 = MhsTifUMS("Fajar", 13, "Klaten", 245000)
c7 = MhsTifUMS("Riza", 5, "Wonogiri", 245000)
c8 = MhsTifUMS("Sidiq", 23, "Klaten", 245000)
c9 = MhsTifUMS("Jaenudin", 64, "SoloBaru", 270000)
c10 = MhsTifUMS("Syahrani", 29, "Gentan", 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

def cariKotaTinggal(list, target):
    x = []
    for i in list :
        if i.kotaTinggal == target:
            x.append(list.index(i))
    return x

x = cariKotaTinggal(Daftar, "Klaten")
print(x)
