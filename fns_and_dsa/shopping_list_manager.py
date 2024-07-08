def display_menu():
    print("Shopping list manager:")
    print("1. Add item:")
    print("2. remove item:")
    print("3. View item:")
    print("4. Exit")


def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter an item: ")
            shopping_list.append(item)
            print(f"{item} has been added to the shopping_list.")
            pass
        elif choice == "2":
            item = input("Enter an item you want to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed to the shopping_list.")
            else:
                print(f"{item} was not found in the shopping_list")
            pass
        elif choice == "3":
            if not shopping_list:
                print("The shopping list is empty")
            else:
                print("Current shopping list:")
                for item in shopping_list:
                    print(f"{item}")
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__== "__main__":
    main()




