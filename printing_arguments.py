def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#another comment
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#a third comment
def print_one(arg1):
    print(f"arg1: {arg1}")

#a fourth comment
def print_none():
    print("I got nothing.")


print_two("Agbere", "Dabiyyah")
print_two_again("Agbere", "Dabiyyah")
print_one("First!")
print_none()
