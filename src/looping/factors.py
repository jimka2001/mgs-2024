from math import sqrt, ceil


def find_factors(n):
    return [f
            for f in range(1, n+1)
            if n%f == 0]

def find_factors_v2(n):
    return [1] + [f
                    for f in range(2, n//2)
                    if n%f == 0] + [n]


#print(find_factors_v2(12))


def approx_pi(n):
    n2 = n*n
    inside = [0
                for x in range(n)
                for y in range(n)
                if x*x+y*y < n2]
    return len(inside) * 4 / (n*n)

print(approx_pi(10000))