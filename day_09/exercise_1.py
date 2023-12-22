# Number 1
age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18 - age}, more years to learn to drive')

# Number 2
my_age = 25
your_age = int(input('enter your age: '))
if your_age > my_age:
    if your_age - my_age == 1:
        result = f"You are {your_age - my_age} year older than me."
    else:
        result = f"You are {your_age - my_age} years older than me."
else:
    result = 'We are the same age or I am older.'
print(result)

# Number 3
a = int(input('enter number one: '))
b = int(input('enter number two: '))
if a > b:
    print(f'{a} is greater than {b}')
elif a < b:
    print(f'{a} is smaller than {b}')
else:
    print(f'{a} is equal to {b}')