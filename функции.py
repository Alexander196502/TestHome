""" подпрограмма кот ждет вызова """
def proba():
    print('Ura-ura')


def summator(x, y):
    """voxvrat"""
    z = x * y / 10
    return z

proba()
n = summator(20, 15)
print(n)
print(summator(20, 15))
#print(summator.___doc___)
#print(___doc___)

def adding(x = 4, y = 15):
    return x + y

def adding(*args, **kwargs):
    print(args)
    print(kwargs, list(kwargs.values()))
    sumkw = sum(list(kwargs.values()))
    return sum(args), sumkw
    return sum(list(args)+ list(kwargs.values()))


print(adding(2, 15, 17, 33, x=12, y=33, z=18))
print(adding(2))
print(adding(2, 14))
print(adding())
print(adding(y=30))

n, m, *z = 7, 5, 12, 88, 99
print(n, type(n), m)
print(z, type(z))
print(*z)

d = {}
n = 3
for _ in range(n):
    name, *marks = input().split()
    marks = [int(m) for m in marks]
    d[name] = round(sum(marks) / len(marks), 2)
print(d)

