while True:

    name = str(input("Please enter your name : "))
    if name == "stop":
        break
    age = int((input("Please enter your brithyear : ")))

    print(f"Hello {name}, your age is {2024 - age}")