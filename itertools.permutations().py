from itertools import permutations
s, r = input().split()
res = permutations(sorted(s), int(r))
for i in res:
    print("".join(i))
