def nthUglyNumber(n, a, b, c):
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    
    def count(x):
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)
        return (x // a) + (x // b) + (x // c) - (x // ab) - (x // bc) - (x // ac) + (x // abc)
    
    left, right = 1, 2 * 10**9
    while left < right:
        mid = (left + right) // 2
        if count(mid) < n:
            left = mid + 1
        else:
            right = mid
    return left
