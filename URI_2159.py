from math import log

n = int(input())

min = n / log(n)
max = 1.25506 * min

print("{:.1f} {:.1f}".format(min, max))
