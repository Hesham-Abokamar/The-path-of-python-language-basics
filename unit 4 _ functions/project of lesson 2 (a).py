def user_details():

    name = input("Please enter your name : ")
    last_name = input("Please enter your last name : ")
    age = int(input("Please enter your age : "))
    weight = int(input("Please enter your weight : "))
    height = int(input("Please enter your height : "))

    print(f"Hello {name} {last_name} ! your age is {age}, your weight is {weight} and your height is {height}")

user_details()