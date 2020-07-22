def arraydif(o,x):
    for a in x:
        if a in o:
            for j in range(o.count(a)):
                a.remove(i)

    return a


def ad(a,b):
    return [x for x in a if x not in b]

def ad(a,b):
    return filter(lambda i : i not in b,a)

def ad(a,b):
    for i in range(len(b)):
        while b[i] in a:
            a.remove(b[i])
    return a
