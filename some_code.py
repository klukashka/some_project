a, b, c = map(int, input().split())
if a != 0:
    d = b**2 - 4*a*c
    print((-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a))
else:
    print(-c/b)