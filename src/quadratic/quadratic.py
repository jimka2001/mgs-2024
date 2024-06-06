from math import sqrt


def roots(a, b, c):
    desc = b*b - 4*a*c
    # refactor
    if desc < 0:
        return []
    elif desc == 0:
        return [-b/(2*a)]
    else:
        return [(-b + sqrt(desc))/(2*a),
                (-b - sqrt(desc))/(2*a)]

#print(type(2))
#print(type(4.3))
#print(4 // 3)
#print(4 / 3)
#print(4 % 3)
#print(4.0/3)
#print([3, 7, {-1, 7, 7}, 7, 43])
#print({3, 7, -1, 7, 7, 7, 43})

print(roots(1, 1, 1 ))
print(roots(-2, -2, 24))
print(roots(1,2,1))

def testRoots():
    # testing
    assert roots(1, 0, 0) == {0}
    assert roots(3, 6, 3) == {-1}
    assert roots(1, 13, 12) == {-1, -12}
    assert roots(1, -1, -12) == {4, -3}
    assert roots(-1, 1, 12) == {4, -3}
    assert roots(1, 3, -10) == {2, -5}
    assert roots(1, 2, 2) == {}


#testRoots()
