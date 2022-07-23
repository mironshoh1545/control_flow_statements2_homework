def mx(a,b):
    if a > b:
        return a
    return b

def main(n):
    x1 = n // 10000
    x2 = n // 1000 % 10
    x3 = n // 100 % 10
    x4 = n // 10 % 10
    x5 = n % 10
    m = mx(x1, x2)
    m = mx(m, x3)
    m = mx(m, x4)
    m = mx(m, x5)
    
    if m == x1 :
        return 5
    elif m == x2:
        return 4
    elif m == x3:
        return 3
    elif m == x4:
        return 2
    return 1