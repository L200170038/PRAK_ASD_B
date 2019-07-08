def test():
    """Test test"""
    L = []
    for i in range(100):
        L.insert(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
