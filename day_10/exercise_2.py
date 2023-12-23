# Number 1
total_sum = 0
for i in range(101):
    total_sum = total_sum + i
print('The sum of all numbers is ', total_sum)


# Number 2
s_even = 0
s_odd = 0
for x in range(101):
    if x % 2 == 0:
        s_even = s_even + x
    else:
        s_odd = s_odd + x
print(f'The sum of all evens is {s_even}. And the sum of all odds is {s_odd}.')