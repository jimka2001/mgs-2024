from math import pi


def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)

def approxpi(den):
    data = [[abs(pi - a / den) / pi * 100, a, den]
            for a in range(3 * den, 4 * den)
            if gcd(a, den) == 1]
    data.sort()
    best = data[0]
    return best

def bestfrac(den):
    data = [[abs(pi - n/den), n, den] for n in range(3*den, 4*den)
            if gcd(n, den) == 1]
    data.sort()
    return data[0]

#print(bestfrac(4))


#approximations = [bestfrac(den) for den in range(3, 10000)]
#approximations.sort()
#print(approximations[0])

def pi_approx(n):
    n2 = n*n
    return 4 * sum(1
                    for x in range(n)
                   for x2 in [x*x]
                    for y in range(n)
                    if x2 + y*y < n2)/ n2

print(pi_approx(20000))