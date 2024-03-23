degree = int(input("Please enter your degree :"))

if degree > 100 or degree < 0:
    print("The degree is wrong , Please enter betwee 0 and 100 only !")

if degree <= 100 or degree >= 90:
    print("Your degree is 'A' ")
elif degree <= 89 or degree >= 80:
    print("Your degree is 'B' ")
elif degree <= 79 or degree >= 70:
    print("Your degree is 'C' ")
elif degree <= 69 or degree >= 60:
    print("Your degree is 'D' ")
elif degree <= 59 or degree >= 50:
    print("Your degree is 'E' ")
else:
    print("Your degree is 'F' ")