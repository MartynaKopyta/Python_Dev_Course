# MRO decides which method to run
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):  # B first
    pass


print(D.num)
print(D.mro())  # a way to check the order

# Overcomplicated example, don't do this
class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())  # depth first search
