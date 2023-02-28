# Zusammenarbeit mit folgenden Teilnehmern:
def cross_sum(n, b):
    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b

    crosssum = 0
    for digit in digits:
        crosssum += digit

    return crosssum

print(cross_sum(212, 16))
