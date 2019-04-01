def swap (A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp

def swap_dua (A, p, q):
    A[p], A[q] = A[q], A[p]

data = [22, 4, 1, 7]
print (data)
swap (data, 0, 1)
print (data)
swap_dua(data, 0, 3)
print (data)

class mhs(object) :
    """Class mahasiswa dengan berbagai metode"""
    def __init__ (self, nama, NIM, kota, us):
        self.nama = nama
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us

    def __str__ (self) :
        s = self.nama + ', NIM' + str(self.NIM)\
            +'.Tinggal di ' + self.kotaTinggal \
            +'. Uang saku Rp' + str(self.uangSaku)\
            +' tiap bulannya.'
        return s
    def ambilNama(self) :
        return self.nama
    def ambilNIM(self) :
        return self.NIM
    def ambilUangSaku(self):
        return self.uangSaku

a0 = mhs("Ika", 10, "Sukoharjo", 240000)
a1 = mhs("Budi", 51, "Sragen", 230000)
a2 = mhs("Ahmad", 2, "Surakarta", 250000)
a3 = mhs("Chandra", 18, "Surakarta", 2350000)
a4 = mhs("Eka", 4, "Boyolali", 230000)
a5 = mhs("Fandi", 31, "Salatiga", 250000)
a6 = mhs("Deni", 13, "Klaten", 245000)
a7 = mhs("Galuh", 5, "Wonogiri", 245000)
a8 = mhs("Janto", 23, "Klaten", 245000)
a9 = mhs("Hasan", 64, "Karanganyar", 270000)
a10 = mhs("Khalid", 29, "Purwodadi", 265000)

daftar = [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]

target = "Klaten"
def cari(daftar, target):
    a = []
    indeks = 0
    for i in daftar:
        if i.kotaTinggal == target:
            a.append(indeks)
        indeks += 1
    return a
print (cari(daftar, target))

kumpulan = []
for a in daftar :
    kumpulan.append(a.ambilUangSaku())
def kecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0]
    for i in range (1,n):
        if kumpulan[i] < terkecil:
            terkecil =kumpulan[i]
    return terkecil

print (kecil(kumpulan))

def kembalikanNama(kumpulan):
    li = []
    co = 1
    n = len(kumpulan)
    terkecil = kumpulan[0].ambilUangSaku()
    for i in range (1,n):
        if kumpulan[i].ambilUangSaku() < terkecil:
            li.append(co)
        co += 1
    res = []
    for i in li:
        res.append(kumpulan[i].ambilNama())
    return res

print (kembalikanNama(daftar))

##NO 1
kumpulan = []
for a in daftar :
    kumpulan.append(a.ambilNIM())
def insertionSort(kumpulan):
    n = len(kumpulan)    
    for i in range (1, n):
        nilai = kumpulan[i]
        pos = i
        while pos > 0 and nilai < kumpulan[pos - 1] :
            kumpulan[pos] = kumpulan[pos -1]
            pos = pos -1
            kumpulan[pos] = nilai

insertionSort(kumpulan)
print (kumpulan)

##NO 2
A = [1,2,3,4,5,6,7,8,9]
B = [1,3,4,5]

def gabungkanDuaList(A, B):
    pertama = len(A); kedua = len(B)
    C = list()
    i = 0; j = 0
    #Gabungkan keduanya
    while i < pertama and j < kedua:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1

        else :
            C.append(B[j])
            j += 1
    while i < pertama :
        C.append(A[i])
        i += 1
    while j < kedua :
        C.append(B[i])
        i += 1
    return C

print (gabungkanDuaList(A, B))

##NO 3
def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp
    
def cariposisiterkecil(A, darisini, sampaisini):
    posisiterkecil = darisini
    for i in range(darisini + 1, sampaisini):
        if A[1] < A[posisiterkecil]:
            posisiterkecil = 1
    return posisiterkecil

def bubblesort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
                
def selectionsort(A):
    n = len(A)
    for i in range(n - 1):
        indexkecil = cariposisiterkecil(A, i, n)
        if indexkecil != i:
            swap(A, i, indexkecil)

def insertionsort(A):
    n = len(A)
    for i in range(1 ,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos - 1]:
            A[pos] = A[pos - 1]
            pos = pos - 1
        A[pos] = nilai
        
from time import time as detak
from random import shuffle as kocok

k = [i for i in range(1 ,6001)]
kocok(k)
u_bub = k[:]
u_sel = k[:]
u_ins = k[:]

aw = detak();bubblesort(u_bub);ak=detak();print('Buble      : %g detik' %(ak-aw));
aw = detak();selectionsort(u_sel);ak=detak();print('Selection  : %g detik' %(ak-aw));
aw = detak();insertionsort(u_ins);ak=detak();print('Insertion  : %g detik' %(ak-aw));
