# Day 2: 30 Days of python programming


print("Exercise 1 var declaration")

first_name = "Ibrahim"
last_name = "Abdullahi"
full_name = "Ibrahim Abdullahi"
country = "Nigeria"
city = "Kano"
age = 24
year = 2023
is_married = False
is_true = True
is_light = True
is_single = True
status = "single"
phone_no = "08012345678"

print("Exercise 2 checking var type")

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light))
print(type(is_single))
print(type(status))
print(type(phone_no))


print(len(first_name))
print(len(first_name) == len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = pow(num_one, num_two)
floor_division = num_one // num_two


radius = 30
area_of_circle = 3.143 * pow(radius, 2)
print(f"Area of Circle: {area_of_circle}")

print("\n", "Circumference of a circle", "\n")
circum_of_circle = 2 * 3.143 * radius
print(f"Circumference of a circle: {circum_of_circle}")


radius = int(input("enter radius: "))
area = 3.143 * pow(radius, 2)
print(f"Area of Circle: {area}")

print("\n", "build-in input", "\n")
first_name = str(input("enter first name: "))
last_name = str(input("enter last name: "))
country = str(input("enter country: "))
age = int(input("enter age: "))
