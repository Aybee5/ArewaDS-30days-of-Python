import math

age = 23
height = 5.6
complex_num = 1j

# triangle area
base = input("Enter base: ")
height = input("Enter height: ")
print(f"The area of the triangle is {0.5 * int(base) * int(height)}")


#perimeter of triangle
sidea = input("Enter side a: ")
sideb = input("Enter side b: ")
sidec = input("Enter side c: ")
print(f"The perimeter of the triangle is {sidea + sideb + sidec}")

length = int(input("Length: "))
width = int(input('width: '))
area = length * width
perimeter = 2 * (length + width)
print(f"area is: {area}, perimeter is: {perimeter}")

r = int(input('enter radius: '))
pi = 3.14
area = pi * r * r
c = 2 * pi * r
print(f'area is {area}, circumference is {c}')

#slope
x1, y1, x2, y2 = 2, 2, 6, 10
m = (y2 - y1) / (x2-x1)
d = math.sqrt((pow((x2-x1), 2) + pow((y2 - y1), 2)))
print(f'slope is {m}, distance is {d}')

x = 1 #if x = -3 then y = 0
y = x ** 2 + 6 * x + 9
print(f'x is {x}, y is {y}')

print(len('python'))
print(len('dragon'))

print(len('python') == len('dragon'))

# exercise 13
print("on" in "python" and "on" in "jargon")

# exercise 14
print("jargon" in "I hope this course is not full of jargon")

# exercise 15
print("on" not in "python" and "on" not in "jargon")

# exercise 16
print(str(float(len("python"))))

# exercise 17
# by using modulo and the answer is 0
num = int(input("enter a number: "))
print("even" if num % 2 == 0 else "odd")

# exercise 18
print(7 // 3 == int(2.7))

# exercise 19
print(type("10") == type(10))

# exercise 20
print(int(9.8) == 10)

# exercise 21
hours = int(input("Enter hours: "))
rate = int(input("Enter rate: "))
print(f"your weekly earning is {hours * rate}")

# exercise 22
years = int(input("Enter number of years you have lived: "))
print(f"you have lived for {years * 365 * 24 * 60 * 60} seconds")

# exercise 23
# exercise number 23
table_list = [
    [1, 1, 1, 1, 1],
    [2, 1, 2, 4, 8],
    [3, 1, 3, 9, 27],
    [4, 1, 4, 16, 64],
    [5, 1, 5, 25, 125],
]

for i in list:
    for row in i:
        print(row, end=" ")
    print()
