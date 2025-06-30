from cli_handler import handle_input

def main():
    print("Welcome to TaskBot CLI!\n"
          "")
    while True:
        user_input = input(">>> ").strip()
        if user_input == "/exit":
            print("Goodbye!")
            break
        handle_input(user_input)

if __name__ == "__main__":
    main()




