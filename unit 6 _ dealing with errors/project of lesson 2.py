class Too_old_error(Exception):

    def __init__(self):
        pass
    def __str__(self):
        return "Sorry but you are too old to sign in !"
    
class Too_young_error(Exception):

    def __init__(self):
        pass
    def __str__(self):
        return "Sorry but you are too young to sign in !"
    
def Age_check(age):
    try:

        if age > 40:
            raise Too_old_error
        elif age < 15:
            raise Too_young_error
        else:
            print("You signed in succesfully")
    
    except Too_old_error as e:
        print(e)
    except Too_young_error as e:
        print(e)

Age_check(int(input("Please enter your age : ")))