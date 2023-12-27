# exercise 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negatives = [i for i in numbers if i < 0]

print(negatives)

# exercise 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat = [single for row in list_of_lists for single_arr in row for single in single_arr]
print(flat)

# exercise 3
# big_list = [(i, i**j) for i in range(10) for j in range(7)]
# print(big_list)
list_of_tuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# exercise 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
country_list = [[(country[0].upper(), country[0][:3].upper(), country[1].upper()) for country in countries] for countries in countries]
print(country_list)

# exercise 5
county_dict = {country[0][0]: {'country': country[0][0].upper(), 'country_code': country[0][0][:3].upper(), 'capital': country[0][1].upper()} for country in countries}
print(county_dict)

# exercise 6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name_list = [f'{name[0][0]} {name[0][1]}' for name in names]
print(name_list)

#exercise 7
linear_function = lambda x, y: x + y
print(linear_function(1, 2))