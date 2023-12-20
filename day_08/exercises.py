#dictionaries

#1 
dog = {}

dog.update({'name': 'Bingo', 'color': 'brown', 'breed': 'German Shepherd', 'legs': 4, 'age': 5})

print(dog)

student = {
  'first_name': "Ibrahim",
  'last_name': "Abdullahi",
  'gender': "Male",
  'age': 24,
  'marital_status': "Single",
  'skills': ["Python", "Javascript", "HTML", "CSS", "Vue", "Node"],
  'country': "Nigeria",
  'city': "Lagos",
  'address': {
    'street': "No 1, Alara street",
    'zipcode': "23401"
  }
}

print(len(student))

print(student['skills'])
print(type(student['skills']))

student['skills'].append('MongoDB')

print(student['skills'])

print(student.keys())

print(student.values())

print(student.items())

del student['address']['zipcode']

print(student)
