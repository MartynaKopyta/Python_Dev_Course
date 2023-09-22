# You can check out new features of next python versions in the documentation
# Walrus operator := assigns values to variables as a part of a larger expression
a = 'hellooooooooo'

if (n := len(a)) > 10:
    print(f'too long {n} elements')

while (n := len(a)) > 1:
    print(n)
    a = a[:-1]  # replacing the string with the same one minus the last letter

print(a)
