import string
from random import randint, random


def list_of_hexa_colors():
    return ['#' + ''.join(hex(randint(0, 255))[2:]) for _ in range(3)]
print(list_of_hexa_colors())

def list_of_rgb_colors():
    return ['rgb(' + ','.join(str(randint(0, 255)) for _ in range(3)) + ')' for _ in range(3)]
  
print(list_of_rgb_colors())

def generate_colors(type):
    if type == 'hexa':
        return ['#' + ''.join(hex(randint(0, 255))[2:]) for _ in range(3)]
    elif type == 'rgb':
        return ['rgb(' + ','.join(str(randint(0, 255)) for _ in range(3)) + ')' for _ in range(3)]
    else:
        return 'Invalid type'
      
print(generate_colors('hexa'))