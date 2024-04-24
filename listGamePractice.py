# Import the necessary libraries
import random

# Function to generate a random target list
def generate_target_list():
    target = random.sample(words, random.randint(2, 10))
    return target

# Function to display the current list and target list to the user
def display_list(current, target):
    print("Current list: ", current)
    print("Target list: ", target)
    
# Function to allow the user to perform operations on the list
def manipulate_list(current):
    print("\n\nYou can perform the following operations on the list:")
    print("1. Append a word to the end of the list")
    print("2. Extend the list with another list")
    print("3. Concatenate two elements in the list")
    print("4. Traverse the list and view its elements")
    print("5. Modify an element in the list")
    print("6. Insert an element at a specific index in the list")
    print("7. Pop an element from the list")
    print("8. Remove a specific element from the list")
    print("9. Sort the list in ascending or descending order")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        word = input("Enter a word to append: ")
        current.append(word)
    elif choice == 2:
        extend_list = input("Enter a comma-separated list to extend with: ").split(",")
        current.extend(extend_list)
    elif choice == 3:
        index_1 = int(input("Enter the index of the first element: "))
        index_2 = int(input("Enter the index of the second element: "))
        if index_1 >= 0 and index_1 < len(current) and index_2 >= 0 and index_2 < len(current):
            current[index_1] += current[index_2]
            del current[index_2]
        else:
            print("Wrong answer. Please try again.")
    elif choice == 4:
        print("List elements:")
        for word in current:
            print(word)
    elif choice == 5:
        index = int(input("Enter the index of the element to modify: "))
        if index >= 0 and index < len(current):
            word = input("Enter the new word: ")
            current[index] = word
        else:
            print("Wrong answer. Please try again.")
    elif choice == 6:
        index = int(input("Enter the index to insert at: "))
        if index >= 0 and index <= len(current):
            word = input("Enter the new word: ")
            current.insert(index, word)
        else:
            print("Wrong answer. Please try again.")
    elif choice == 7:
        if len(current) > 0:
            word = current.pop()
            print("Popped word:", word)
        else:
            print("The list is empty. Please try again.")
    elif choice == 8:
        word = input("Enter a word to remove: ")
        if word in current:
            current.remove(word)
        else:
            print("Word is not found in the list, please try again.")
    elif choice == 9:
        ascending = input("Sort in ascending order? (y/n) ").lower() == "y"
        current.sort(reverse=not ascending)
    return

# Print a welcome message to the user
print("Welcome to the List Game!!!\nYour task is to transform the current list into the target list. Are you ready?")
input("Press Enter to continue...\n")

# Create a list of words
words =[
    "apple", "banana", "cherry", "date", "elephant", "fig", "grape", "honey", "ice", "jelly",
    "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tomato",
    "umbrella", "vanilla", "watermelon", "xigua", "yogurt", "zebra"
]

# Display the list of words that the user can use
print("Here is the list that you can use:\n", words)

# Ask the user to input the elements of the list
length_of_list = int(input("How many elements you want to add to the list?"))
current = []
for times in range(1, length_of_list + 1):
    element = input("No.{} element: ".format(times))
    current.append(element)

# Generate the target list
print("Now, let's start the game!!!")
target = generate_target_list()
print("\n\nThe target list has been generated.")
display_list(current, target)

# Allow the user to manipulate the list
while True:
    manipulate_list(current)
    print("\n\nAfter performing the operation:")
    display_list(current, target)
    if current == target:
        print("\n\nCongratulations! You have successfully transformed the current list into the target list.")
        break
