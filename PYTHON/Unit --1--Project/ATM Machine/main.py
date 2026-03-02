balance = 10000
pin = "1234"

print("Welcome to ATM")

user_pin = input("Enter your PIN: ")

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Amount Deposited Successfully")

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
            else:
                print("Insufficient Balance")

        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN")