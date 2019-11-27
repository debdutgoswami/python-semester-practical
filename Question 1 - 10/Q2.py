l = [int(i) for i in input().split()]

print("largest - ", max(l))
print('smallest - ', min(l))

print('2nd largest - ', sorted(l)[-2])
print('2nd smallest - ', sorted(l)[1])