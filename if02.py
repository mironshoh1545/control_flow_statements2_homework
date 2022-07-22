def mx(a,b):
    if a < b:
        return a
    return b
def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    mn = mx(a, b)
    mn = mx(mn, c)
    return mn