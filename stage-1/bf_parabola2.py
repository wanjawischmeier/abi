import numpy as np

def find_factors():
    x1 = 0.412
    x2 = 1.711

    min_decimal_places = float('inf')
    best_factors = None

    for a in range(-100, 101):
        print(a, min_decimal_places, best_factors)
        for b in range(-100, 101):
            for c in range(-100, 101):
                if a != 0:
                    discriminant = b**2 - 4*a*c
                    if discriminant > 0:
                        x1_actual = (-b + np.sqrt(discriminant)) / (2*a)
                        x2_actual = (-b - np.sqrt(discriminant)) / (2*a)

                        if round(x1_actual, 3) == x1 and round(x2_actual, 3) == x2:
                            decimal_places_a = len(str(abs(a)).split('.')[1])
                            decimal_places_b = len(str(abs(b)).split('.')[1])
                            decimal_places_c = len(str(abs(c)).split('.')[1])

                            total_decimal_places = decimal_places_a + decimal_places_b + decimal_places_c

                            if total_decimal_places < min_decimal_places:
                                min_decimal_places = total_decimal_places
                                best_factors = (a, b, c)

    return best_factors

factors = find_factors()
print("Factors with the least decimal places:", factors)
