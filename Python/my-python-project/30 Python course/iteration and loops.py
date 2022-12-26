for x in range(0, 10):  #
    # range() is every number between the first var and second last, excluded the second number
    print(x)

user_1 = {"username": "Lukas Stank", "id": 1}
user_2 = {"username": "Thomas Stank", "id": 2, "email": "abc@abc.abc"}
my_users = [user_1, user_2]

for user in my_users:
    print(user["username"])

for user in my_users:  # only prints the email, if the user has one, otherwise it would be an error
    if "email" in user:
        print(user["email"])

selected_user = {}
my_user_lookup = 2
for user in my_users:
    if "id" in user:
        if user["id"] == my_user_lookup:
            selected_user = user

if selected_user == {}:
    print("Your selected User doesn't exist!")
else:
    print(selected_user)

for x in range(0, 10):
    for user in my_users:
        if user["id"] == x:
            print(user)
