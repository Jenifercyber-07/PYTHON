books = ["python", "java", "c++", "data structures"]

def check_book(book):
    if book in books:
        print("Book is available")
    else:
        print("Book is not available")

def borrow_book(book):
    if book in books:
        books.remove(book)
        print("Book borrowed successfully")
    else:
        print("Book not available")

def return_book(book):
    books.append(book)
    print("Book returned successfully")

while True:
    print("\n1. Check Book")
    print("2. Borrow Book")
    print("3. Return Book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        check_book(book)

    elif choice == 2:
        book = input("Enter book name: ")
        borrow_book(book)

    elif choice == 3:
        book = input("Enter book name: ")
        return_book(book)

    elif choice == 4:
        print("Exiting...")
        break

    else:
        print("Invalid choice")