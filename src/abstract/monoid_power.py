def power(b, p, op, id):
    if p == 0:
        return id
    elif p%2 == 0:  # even
        return power(op(b,b),p//2, op, id)
    else:  # odd
        return op(b, power(b, p-1, op, id))

def mult_12(x,y):
    m = (x*y) % 12
    if m == 0:
        return 12
    else:
        return m

## 7 ** 51

print(power(7, 51, mult_12, 1))

def mult_string(a,b):
    return a + b

## "hello" ** 10
print(power("hello", 10, mult_string, ""))
print(power("hello-", 3, mult_string, ""))

def mult_int(a,b):
    return a * b

## 10 ** 9
print(power(10, 9, mult_int, 1))

def add_int(a,b):
    return a + b

## 10 * 9
print(power(10, 9, add_int, 0))

valids = {"a", "b", "c", "d"}
def cayley_mult(x,y):
    assert x in valids
    assert y in valids
    if x == "a":
        return y
    elif y == "a":
        return x
    elif x == y:
        return y
    else:
        return "d"

# "c" ** 13
print(power("c", 13, cayley_mult, "a"))
print(power("c", 13, cayley_mult, "a"))

def mult_list(list1, list2):
    return list1 + list2

# [1,2,3] ** 12
print(power([1,2,3], 12, add_int, []))