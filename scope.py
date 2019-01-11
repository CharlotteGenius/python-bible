a = 25
# global scope. a local scope can't change the global value
# the local value is destroyed when the local function is finished

def f1():
    global a
    a = 100
    # using "global" changed the value of a, it's global value
    print(a)


def f2():
    a=50
    print(a)
# without "global", "a" is a local scope that can't been seen by f1()
# local value


f1()
f2()
print(a)


# 1) Two types of scope - Global & local
# 2) Python functions create local scopes

# special case:

b = [1,2,3]

def f3():
    b[0] = 5
    print(b)

f3()
print(b)
# In this case, "global" is not used
# but still, b is changed partially
# watch out for this!
