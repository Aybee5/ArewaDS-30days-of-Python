import statistics

print(statistics.mean([1, 2, 3, 4, 5]))
# or better still
from statistics import mean

print(mean([1, 2, 3, 4, 5]))
# or even better(I am not sure about this one)
from statistics import *

print(median([1, 2, 3, 4, 5]))
