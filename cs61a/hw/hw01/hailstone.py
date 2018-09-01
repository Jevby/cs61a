def hailstone(n):
    if n%2==0:
        n /=2;
        hailstone(n);
    else:
        n=n*3+1;
        hailstone(n);

a = hailstone(10);
print(a)