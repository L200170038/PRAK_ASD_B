print(2)
print(3)
print(5)
print(7)
for i in range(2,1000):
    if(i % 2) != 0:
        if(i % 3) != 0:
            if(i % 5) != 0:
                if(i % 7) != 0:
                    print(i)
    
