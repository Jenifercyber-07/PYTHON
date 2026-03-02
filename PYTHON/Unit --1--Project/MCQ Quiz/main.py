score = 0

print("Welcome to Python MCQ Quiz")

print("\n1. What is the extension of Python file?")
print("a) .py")
print("b) .java")
print("c) .html")
print("d) .cpp")

ans = input("Enter your answer: ")

if ans.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n2. Which keyword is used for function in Python?")
print("a) fun")
print("b) define")
print("c) def")
print("d) function")

ans = input("Enter your answer: ")

if ans.lower() == "c":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n3. Which data type is used for numbers?")
print("a) int")
print("b) str")
print("c) list")
print("d) tuple")

ans = input("Enter your answer: ")

if ans.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour final score is:", score, "/ 3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
else:
    print("Try Again!")