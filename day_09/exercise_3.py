person = {
    "first_name": "Asabeneh",
    "last_name": "Yetayeh",
    "age": 250,
    "country": "Finland",
    "is_marred": True,
    "skills": ["JavaScript", "React", "Node", "MongoDB", "Python"],
    "address": {"street": "Space street", "zipcode": "02210"},
}

skill_length = len(person["skills"])
if "skills" in person:
    mid_1 = person["skills"][skill_length // 2]
    if skill_length % 2 == 0:
        mid_2 = person["skills"][skill_length // 2 - 1]
        result = f"The middle items are {mid_1} & {mid_2}"
    else:
        result = f"The middle item is {mid_1} "
print(result)


skill = person["skills"]
if "skills" in person:
    if "Python" in skill:
        print("Person has Python skill")
    else:
        print("Person has no Python skill")

if "skills" in person:
    if (
        "JavaScript" in skill
        and "React" in skill
        and "Node" in skill
        and "MongoDB" in skill
    ):
        print("He is a fullstack developer")
    elif "JavaScript" in skill and "React" in skill:
        print("He is a front end developer")
    elif "Node" in skill and "Python" in skill and "MongoDB" in skill:
        print("He is a backend developer")
    else:
        print("unknown title")

if person["is_marred"] == True and person["country"] == "Finland":
    print(
        f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married"
    )
