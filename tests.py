# import statistics

# print(statistics.mean([1, 2, 3, 4, 5]))
# # or better still
# from statistics import mean

# print(mean([1, 2, 3, 4, 5]))
# # or even better(I am not sure about this one)
# from statistics import *

# print(median([1, 2, 3, 4, 5]))


# #lambda expression

# # lambda_fun =lambda *args : expression

# import re

# re.match(r'(\w+) (\w+)', 'Isaac Newton, physicist', re.I).groups()


import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # we get all the content from the website
soup = BeautifulSoup(content, 'html.parser') # beautiful soup will give a chance to parse
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # gives the whole page on the website
print(response.status_code)