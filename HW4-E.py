a, b, c = map(int, input().split())
D = b * b - 4 * a * c
if D > 0:
    print(2)
elif D == 0:
    print(1)
else:
    print(0)