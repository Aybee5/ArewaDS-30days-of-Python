import math

#exercise 1
empty = []

#exercise 2
days = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#exercise 3
print(len(days))

#exercise 4
print(days[0])
print(days[math.floor(len(days)/2)])
print(days[-1])

#exercise 5
mixed_data_types = ['Ibrahim', '24', '5.7', 'single', 'Kano']

#exercise 6
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#exercise 7
print(it_companies)

#exercise 8
print(len(it_companies))

#exercise 9
first_company = it_companies[0]
print(first_company)
second_company = it_companies[[math.floor(len(it_companies)/2)]]
print(second_company)
last_company = it_companies[-1]
print(last_company)

#exercise 10
it_companies[1] = 'Tesla'
print(it_companies)

#exercise 11
it_companies.append('ChatGPT')
print(it_companies)

#exercise 12
it_companies.insert([math.floor(len(it_companies)/2)], 'Kodak')
print(it_companies)

#exercise 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

#exercise 14
for company in it_companies:
    print(f'#{company}')

#exercise 15
does_exist = 'Flutterwave' in it_companies
print(does_exist)

#exercise 16
it_companies.sort()
print(it_companies)

#exercise 17
it_companies.reverse()
print(it_companies)

#exercise 18
print(it_companies[0:3])

#exercise 19
print(it_companies[-3::])

#exercise 20
print(it_companies[4:9:5])

#exercise 21
it_companies.pop(0)
print(it_companies)

#exercise 22
del it_companies[3]
print(it_companies)

#exercise 23
it_companies.pop()
print(it_companies)

#exercise 24
it_companies.clear()
print(it_companies)

#exercise 25
del it_companies

#exercise 26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

#exercise 27
full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)
