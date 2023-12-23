import sys

sys.path.append('.')
from files.data import countries, countries_data

#Number 1
for i in countries:
  if 'land' in i.lower():
    print(i)

#Number 2
lists = ['banana', 'orange', 'mango', 'lemon']
for i in lists[::-1]:
  print(i)

languages_count = sum(len(i['languages']) for i in countries_data)
print(languages_count)

#10 most spoken languages
languages = {}
for country in countries_data:
  for language in country['languages']:
    languages[language] = languages.get(language, 0) + 1
# print(languages)

#sort languages by number of spoken
languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
# get top 10
languages = languages[:10]
print(languages, end='\n\n')

#10 most populated countries
countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
countries = countries[:10]
print(countries)
  
  