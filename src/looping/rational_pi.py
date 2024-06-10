from math import pi

def gcd(p,q):
    if q == 0:
        return p
    else:
        return gcd(q, p%q)

#print(gcd(77,22))

def best_for_denom(dem):
    triples = [[abs(pi-num/dem), num, dem] for num in range(3*dem, 4*dem)
                if gcd(num,dem) == 1]
    triples.sort()
    return triples[0]

print(best_for_denom(14))

def best_for_all_denom(n,m):
    triples = [best_for_denom(d)
                for d in range(n,m)]
    triples.sort()
    return triples

print(best_for_all_denom(7,10000)[0:10])