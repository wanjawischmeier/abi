import math

closest = 10

for a in range(0, 2000):
    for b in range(0, 2000):
        f = math.e * (a / 1000) + math.pi * (b / 1000)
        diff = abs(f - 6.495197)

        if diff < closest:
            closest = diff
            closest_f = (a / 1000, b / 1000, round(f * 1000000) / 1000000)
            print(closest_f, closest)

print(closest_f, closest)

"""
Result:
0.412e + 1.711pi = 6.495197...
"""