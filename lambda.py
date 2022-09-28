from functools import reduce

nums = [1, 4, 2, 5, 6, 8, 16, 8, 4, 10]

evens = list(filter(lambda a: a % 2 == 0, nums))

doubles = list(map(lambda n: n * 2, evens))

sums = reduce(lambda a, b: a + b, doubles)
print(evens)
print(doubles)
print(sums)
