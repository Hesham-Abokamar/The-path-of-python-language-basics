for i in range(1, 6):
    print("*" * i)

print("")

for j in range(0, 5):
    if j == 2:
        print("* python3 *")
    else:
        print("*" * 11)

print("")

num = 1
for x in range(0, 4):
    for y in range(0, x + 1):
        print(num, end = ' ')
        num += 1
    print()
