#Tuples

empty = ()

brothers = ("Albert", "John", 'Muhammad')

sisters = ("Maryam", "Fatima", "Aisha")

siblings = brothers + sisters

print(siblings)

family_members = list(siblings)

family_members.append("Abdullahi")
family_members.append("Mother")

print(family_members)

#exercise 2

siblings, parents = family_members[:-2], family_members[-2:]

print(siblings)
print(parents)


fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
animal_products = ('milk', 'meat', 'butter', 'yoghurt')
food_stuff_tp = fruits + vegetables + animal_products

print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

import math

middle_item = food_stuff_lt[math.floor(len(food_stuff_lt)/2)]
print(middle_item)

first_three, last_three = food_stuff_lt[:3], food_stuff_lt[-3:]
print(first_three)
print(last_three)

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
