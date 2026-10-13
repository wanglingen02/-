sides = sorted(map(int, input().split()))
a, b, c = sides[0], sides[1], sides[2]
if a + b <= c:
    print("Invalid")
elif a == b and b == c:
    print("Equilateral")
elif a == b or b == c:
    print("Isosceles")
else:
    print("Scalene")