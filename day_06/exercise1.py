empty = ()

brothers = ("Albert", "John", 'Muhammad')

sisters = ("Maryam", "Fatima", "Aisha")

siblings = brothers + sisters

print(siblings)

family_members = list(siblings)

family_members.append("Abdullahi")
family_members.append("Mother")

family_members = tuple(family_members)

print(family_members)
