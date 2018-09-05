def hailstone(n):
    """
        Print the hailstone sequence starting at n and return its
        length.
    """
    if n == 1:
        return 1
    
    if n%2==0:
        n /= 2
        print(int(n))
        return hailstone(n) + 1
    else:
        n = n * 3 + 1
        print(int(n))
        return hailstone(n) + 1


a = hailstone(10)
print(a)

