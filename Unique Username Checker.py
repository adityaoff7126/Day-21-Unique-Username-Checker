USERS = ("aditya", "rohan", "kunal")
USER_SET = set(USERS)   


def register(users, user_set):
    username = input("Enter username: ").lower()

    if username in user_set:
        print("Username already taken")
        return users, user_set

    if len(username) < 4 or not username.isalnum():
        print("Invalid username (min 4 chars, only letters & numbers)")
        return users, user_set

    users = users + (username,)  
    user_set.add(username)

    print("Registered successfully")
    return users, user_set


def view(users):
    print("\nRegistered Users:")
    for u in users:
        print("-", u)


while True:
    print("\n1. Register User")
    print("2. View Users")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        USERS, USER_SET = register(USERS, USER_SET)

    elif choice == "2":
        view(USERS)

    elif choice == "3":
        print("Exiting program")
        break

    else:
        print("Invalid choice")
