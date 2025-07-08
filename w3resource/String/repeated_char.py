import collections

str1 = 'the quick brown fox jumps over the lazy dog'
d = collections.defaultdict(int)
for c in str1:
    d[c] += 1

for c in sorted (d, key=d.get, reverse=True):
    if d[c] > 1:
        print(f'{c} : {d[c]}')