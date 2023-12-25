# exercise 1
def evens_and_odds(number):
    evens = []
    odds = []
    for i in range(number):
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    print(f"The number of odds are {len(odds)}")
    print(f"The number of evens are {len(evens)}")
    return "Done!"


print(evens_and_odds(100))


# exercise 2
def factorial(number):
    return 1 if number == 0 else number * factorial(number - 1)


print(factorial(5))


# exercise 3
def is_empty(arr):
    return len(arr) == 0


def calculate(arr):
    print(f"The mean is {sum(arr) / len(arr)}")
    print(f"The median is {arr[len(arr) // 2]}")
    print(f"The mode is {max(set(arr), key=arr.count)}")
    print(f"The range is {max(arr) - min(arr)}")
    print(
        f"The variance is {sum((i - sum(arr) / len(arr)) ** 2 for i in arr) / len(arr)}"
    )
    print(
        f"The standard deviation is {((sum((i - sum(arr) / len(arr)) ** 2 for i in arr) / len(arr))) ** 0.5}"
    )
    return "Done!"
