from math import sqrt

a_fac = 1000
b_fac = 100
tx1 = 0.412
tx2 = 1.711

closest = 10

for a in range(1900, 2900):
    print(a)
    a /= a_fac

    for b in range(-600, -400):
        b /= b_fac

        for c in range(130, 200):
            c /= b_fac

            p = b / a
            q = c / a

            p2 = p / 2
            ppow2 = p2 ** 2
            if ppow2 <= q:
                continue

            discr = sqrt(ppow2 - q)
            x1 = -p2 + discr
            x2 = -p2 - discr

            diff = abs(tx1 - x1) + abs(tx2 - x2)
            if diff < closest:
                closest = diff
                print(diff, a, b, c, x1, x2)