from cli_handler import handle_input
from user import User

def main():
    current_user = None
    print('Welcome to TaskBot CLI!')

    while True:
        user_input = input(">>> ").strip()

        if user_input == "/exit":
            print("Goodbye!")
            break

        if user_input.startswith("/login"):
            try:
                username = user_input.split()[1]
                current_user = User(username=username)
                print(f"Logged in as: {username}")
            except IndexError:
                print("Usage: /login <username>")
            continue

        if not current_user:
            print("Please log in first using /login <username>")
            continue
        handle_input(user_input, current_user)

if __name__ == "__main__":
    main()




