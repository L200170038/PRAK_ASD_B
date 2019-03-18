def buatNol(m, n="OKE"):
    if n == "OKE":
        n = m
    return [[0 for y in range(n)] for x in range(m)]

def buatIdentitas(i):
    return [[1 if y==x else 0 for y in range(i)] for x in range(i)]

print(buatNol(2))
print(buatIdentitas(4))
