#exercise 1
import random


def shuffle_list(arr):
    return random.sample(arr, len(arr))
  
print(shuffle_list([1, 2, 3, 4, 5]))


#exercise 2
def seven_random_numbers():
    seven_random_numbers = set()
    for _ in range(7):
        print(random.randint(0, 9))
        

seven_random_numbers()
        