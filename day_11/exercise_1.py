# exercise 1
def add_two_numbers(a, b):
  return a + b

# exercise 2
def area_of_circle(r):
  return 3.14 * r ** 2

# exercise 3
def add_all_numbers(*args):
  return sum(args)

# exercise 4
def convert_celsius_to_fahrenheit(c):
  return c * 9/5 + 32

# exercise 5
def check_season(month):
  if month in [12, 1, 2]:
    return 'Winter'
  elif month in [3, 4, 5]:
    return 'Spring'
  elif month in [6, 7, 8]:
    return 'Summer'
  elif month in [9, 10, 11]:
    return 'Autumn'
  else:
    return 'Month not valid'
  
# exercise 6
def calculate_slope(x1, y1, x2, y2):
  return (y2 - y1) / (x2 - x1)

# exercise 7
def solve_quadratic_equation(a, b, c):
  x1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  x2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
  return x1, x2

# exercise 8
def print_list(*args):
  for i in args:
    print(i)
    
# exercise 9
def reverse_list(*args):
  return args[::-1]

print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]

# exercise 10
def capitalize_list(*args):
  return [i.capitalize() for i in args]

print(capitalize_list("johN", "mIKE", "gUIDO"))

# exercise 11
def add_item(arr, item):
  arr.append(item)
  return arr

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))     
#[2, 3, 7, 9, 5]

# exercise 12
def remove_item(arr, item):
  arr.remove(item)
  return arr

# exercise 13
def sum_of_numbers(num):
  return sum(range(num+1))

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# exercise 14
def sum_of_odds(num):
  return sum(range(1, num+1, 2))z

#exercise 15
def sum_of_even(num):
  return sum(range(0, num+1, 2))