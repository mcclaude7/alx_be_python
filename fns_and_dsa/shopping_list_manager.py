def display_menu():
    print("Shopping list manager:")
    print("1. Add item:")
    print("2. remove item:")
    print("3. View item:")
    print("4. Exit")

def add_item():
    shopping_list.append(item)

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter an item: ")
            shopping_list.append(item)
            pass
        elif choice == "2":
            item = input("Enter an item you want to remove: ")
            shopping_list.remove(item)
            pass
        elif choice == "3":
            if not shopping_list:
                print("The shopping list is empty")
            else:
                for item in shopping_list:
                    print(item)
            pass
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__== "__main__":
    main()



