# Homework 05 - Task 4
# Console bot assistant with error handling via decorators

# Decorator to handle input errors
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    # Split input into command and arguments
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args


@input_error
def add_contact(args, contacts):
    # Add a new contact to the dictionary
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    # Change phone number for existing contact
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts):
    # Show phone number for a contact
    name = args[0]
    return f"{name}: {contacts[name]}"


def show_all(contacts):
    # Show all contacts
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip()

        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()