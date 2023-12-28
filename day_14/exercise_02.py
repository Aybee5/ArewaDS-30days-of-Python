import sys

sys.path.append('.')

from functools import reduce

from files.data import countries

#exercise 1
upper_country = map(lambda country: country.upper(), countries)
print(list(upper_country))

#exercise 2
numbers = [1, 2, 3, 4, 5]
sqrs = map(lambda number: number**2, numbers)
print(list(sqrs))

#exercise 3
names = ['Asabeneh', 'Brook', 'David', 'John']
upper_names = map(lambda name: name.upper(), names)

#exercise 4
countries_with_land = filter(lambda country: 'land' in country.lower(), countries)

#exercise 5
countries_with_six_char = filter(lambda country: len(country) == 6, countries)
print(list(countries_with_six_char))

#exercise 6
countries_with_six_and_more_char = filter(lambda country: len(country) >= 6, countries)
print(list(countries_with_six_and_more_char))

#exercise 7
countries_start_with_e = filter(lambda country: country[0].lower() == 'e', countries)
print(list(countries_start_with_e))

#exercise 8
names_iterators = filter(lambda name: len(name) == 5,  list(map(lambda name: name.upper(), names)))
print(list(names_iterators))

#exercise 9
def get_string_lists(arr):
  return list(filter(lambda item: isinstance(item, str), arr))
print(get_string_lists([1, 2, 3, 4, 5, 'a', 'b', 'c', 'd']))

# exercise 10
from functools import reduce

sum_of_numbers = reduce(lambda acc, cur: acc + cur, numbers)
print(sum_of_numbers)

# exercise 11
country_sentence = reduce(lambda acc, cur: f'{acc}, {cur}', countries)
# print(country_sentence)

# exercise 12
def categorize_countries(acc, cur):
  if len(cur) > 6:
    acc['long'].append(cur)
  else:
    acc['short'].append(cur)
  return acc
country_categorized = reduce(categorize_countries, countries, {'short': [], 'long': []})
print(country_categorized)

