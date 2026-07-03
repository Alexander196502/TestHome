t1 = (3, 88, 23)
t2 = (43, 12)
tt= (t1, t2)
k = 100
"""
((3, 33 ,100), (43, 100))
"""
ls= []
for i in tt:
    print(i)
    l = list(i)
    l[-1] = ls.append(tuple(l))
print(ls)
tt = tuple(ls)
print(tt)
