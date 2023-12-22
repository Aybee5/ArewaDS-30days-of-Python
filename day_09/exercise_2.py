# Number 1
marks = int(input('enter marks: '))
if marks <= 49:
    grade = 'F'
elif marks <= 59:
    grade = 'D'
elif marks <= 69:
    grade = 'C'
elif marks <= 79:
    grade = 'B'
elif marks <= 100:
    grade = 'A'
else:
    grade = 'Out of range'
print(grade)

# Number 2
u_input = str(input("enter month: ")).lower()
if u_input in {'september', 'october', 'november'}:
    print('The season is Autumn.')
elif u_input in {'december', 'january', 'february'}:
    print('The season is Winter')
elif u_input in {'march', 'april', 'may'}:
    print('The season is Spring')
elif u_input in {'june', 'july', 'august'}:
    print('The season is Summer')
else:
    print('Try Again!')


# Number 3
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = str(input('fruit name: '))
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits) 