#exercise 1
#sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

len(it_companies)

it_companies.add('Twitter')

it_companies.update(['Flutterwave', 'Paystack'])

it_companies.remove('Facebook')

# Remove raises a KeyError if the element is not found, discard does not
it_companies.discard('Facebook')
# it_companies.remove('Facebook')

#exercise 2

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B) == B.union(A))
del A, B


#exercise 3
age_set = set(age)
print(age_set)
print(len(age_set))
print(len(age))
#age is a list of 8 elements, age_set is a set of 5 elements

#Explain the difference between the following data types: string, list, tuple and set

#string is a sequence of characters, 
#list is a sequence of elements,
#tuple is a sequence of elements that cannot be changed, 
#set is a sequence of elements that cannot contain duplicates and is unordered



sentence = "I am a teacher and I love to inspire and teach people."

sentences = sentence.split(' ')

sentence_set = set(sentences)

print(sentence_set)
print(len(sentence_set))