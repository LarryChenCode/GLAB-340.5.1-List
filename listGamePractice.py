import random


print("Welcome to the List Game!!!\nNow, you'll be provided a list of words that you can play with. Are you ready?")
input("Press Enter to continue...\n")

words =[
    "apple", "banana", "cherry", "date", "elephant", "fig", "grape", "honey", "ice", "jelly",
    "kiwi", "lemon", "mango", "nectarine", "orange", "pear", "quince", "raspberry", "strawberry", "tomato",
    "umbrella", "vanilla", "watermelon", "xigua", "yogurt", "zebra"
]
random_words = random.sample(words, 10)
print(random_words)

# defaultList = "".split()
# print("Here is the default list: ", defaultList)
