def cont_frac(p, q):
    c = []
    while p > 1 and q != 0 and len(c) < 100:
        a = p // q
        p, q = q, p - q * a
        c.append(a)
    return c

print(cont_frac(31415926535898, 10000000000000))

def nth_conv(p, q, n):
    if n == 1:
        return p // q
    c = []
    while len(c) < n and p > 1 and q != 0:
        a = p // q
        p, q = q, p - q * a
        c.append(a)
    conv = 1 / c[-1]
    for i in range(len(c) - 1, -1, -1):
        conv = c[i] + 1 / conv
    return conv
for n in range(1, 10):
    print(nth_conv(31415926535898, 10000000000000, n))