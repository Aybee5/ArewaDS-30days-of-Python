# Number 1
for i in range(10):
    print(i)

count = 0
while count < 10:
    print(count)
    count += 1

# Number 2
for i in range(10, 0, -1):
    print(i)

x = 10
while x >= 0:
    print(x)
    x -= 1

# Number 3
for i in range(1, 8):
    print("#" * i)

# Number 4
for _ in range(8):
    for _ in range(7):
        print("#", end="\t")
    print("#")

for mul in range(11):
    print(f"{mul} * {mul} = {mul * mul}")
# Number 6
lst = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for i in lst:
    print(i)


# Number 7
for even in range(0, 100, 2):
    print(even)

# Number 8
for odd in range(1,100,2):
    print(odd)
