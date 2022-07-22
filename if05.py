def mx(a,b):
    if a > b:
        return a
    return b

def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    x1 = n // 10000
    x2 = n // 1000 % 10
    x3 = n // 100 % 10
    x4 = n // 10 % 10
    x5 = n % 10
    m = mx(x1, x2)
    m = mx(m, x3)
    m = mx(m, x4)
    m = mx(m, x5)

    return m