def fibbonacci_numbers1(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
        print(b)
         
#fibbonacci_numbers1(20)

def fibbonacci_numbers2(n):
    a, b = 0, 1
    for _ in range(n):
        yield a 
        remember_a = a
        a = b
        b = remember_a + b

for i in fibbonacci_numbers2(100):
    print(i)