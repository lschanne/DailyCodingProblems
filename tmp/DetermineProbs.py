def get_counts(x=0, n=0, counts={}):
    if n==7:
        counts[x] = counts.get(x, 0) + 1
    else:
        for _ in range(5):
            x += 1
            counts = get_counts(x, n + 1, counts)
    return counts

counts = get_counts()
total = float(sum(counts.values()))
rand7_counts = {}
for key, value in sorted(counts.items()):
    prob = value / total
    print((key, value, prob))

    new_key = key / 5.0
    rand7_counts[new_key] = rand7_counts.get(new_key, 0) + 1

print('-------------------------')
print('-------------------------')

counts = rand7_counts.copy()
total = float(sum(counts.values()))
for key, value in sorted(counts.items()):
    prob = value / total
    print((key, value, prob))

counts = {}
for key, value in rand7_counts.items():
    key = round(key)
    counts[key] = counts.get(key, 0) + 1

print('-------------------------')
print('-------------------------')

total = float(sum(counts.values()))
for key, value in sorted(counts.items()):
    prob = value / total
    print((key, value, prob))


