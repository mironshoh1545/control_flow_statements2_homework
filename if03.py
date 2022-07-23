def mx(a,b):
    if a > b:
        return a
    return b
def mn(a,b):
    if a < b:
        return a
    return b
def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mx1 = mx(a, b)
    mx1 = mx(mx1, c)
    mn1 = mn(a, b)
    mn1 = mn(mn1, c)
    return a + b + c - mx1 - mn1