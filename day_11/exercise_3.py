import sys

sys.path.append(".")
from files.data import countries, countries_data


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            print(f"{number} is not a prime number.")
            return False
    print(f"{number} is a prime number.")
    return True


def are_unique(arr):
    return len(arr) == len(set(arr))


def are_same_type(arr):
    return all(type(i) == type(arr[0]) for i in arr)


# exercise 4
def is_python_variable_name(name):
    return name.isidentifier() and name[0].isalpha()


def most_spoken_languages():
    languages = {}
    for country in countries_data:
        for language in country["languages"]:
            languages[language] = languages.get(language, 0) + 1
    languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
    return languages[:10]


print(most_spoken_languages())


def most_populated_countries():
    countries = sorted(countries_data, key=lambda x: x["population"], reverse=True)
    return countries[:10]


print(most_populated_countries())
