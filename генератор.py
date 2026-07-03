def gen():
    i = 0
    while i <= 3:
        yield i
        i += 1

    #res = gen()
    res = (i for i in range(4))
    print(res)
    print(next(res))
    print(next(res))
    print(next(res))
    print(next(res))

    lst = [22, 33, 44]
    it = iter(lst))
    print(next(lst))
