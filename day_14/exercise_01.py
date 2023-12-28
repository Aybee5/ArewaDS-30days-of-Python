#Diff between map, filter and reduce

#map is a function that takes a function and a list and runs the function for each value, then return a new array with that effect
#filter takes a function and a list and return a a boolean for the values that satisfied the condition in the function, we can then use list to convert it to a list
#reduce fucntion takes a function and a list and run the function on the list to yield a signle value, important where we for eg are calculating sum in cart

#higher order function is a function that takes a function as an argument or return a function as a result
#closure is an inner function that access a variable from the outer function scope
#decorator is a function that takes another function as an argument, add some functionality and return another function

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
upper_case_names = list(map(lambda x: x.upper(), names))
print(upper_case_names)

#filter
ages = [22, 25, 24, 26, 30, 32, 34]
adults = filter(lambda x: x > 25, ages)
print(list(adults))

#reduce
from functools import reduce

total_ages = reduce(lambda a, b: a + b, ages)
print(total_ages)

