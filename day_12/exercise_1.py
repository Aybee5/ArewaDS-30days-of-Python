import string
from random import choice, randint, random


# Number 1
def random_user_id():
    return ''.join(
        str(choice(string.ascii_letters + string.digits))
        for _ in range(6)
    )
print(random_user_id())

# Number 2
def user_id_gen_by_user():
    num_char = int(input("number of characters: "))
    num_id = int(input("number of id: "))
    return [
        ''.join(
            str(choice(string.ascii_letters + string.digits))
            for _ in range(num_char)
        )
        for _ in range(num_id)
    ]
print(user_id_gen_by_user())

# Number 3
def rgb_color_gen():
    return 'rgb(' + ','.join(str(randint(1, 255)) for _ in range(3)) + ')'
print(rgb_color_gen())