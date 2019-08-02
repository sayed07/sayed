from itertools import permutations
b, n= map(int, input().split())
z = list(map(int, input().split()))
for r in permutations(z, 2):
    if sum(r) == n:
        print('yes')
        break
else:
    print('no')
