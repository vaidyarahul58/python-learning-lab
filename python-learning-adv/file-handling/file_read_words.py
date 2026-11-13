# Read, count words from text file.

try:
    with open("webui.txt", "r", encoding="utf-8") as file:
        text = file.read()
except FileNotFoundError:
    print("Error : File not found.")

n = 0
search = input("Enter the word to search : ")

words = text.split()

print("\nTotal characters : ", len(text))
print("Total words : ", len(words))
for word in words:
    if word == search:
        n += 1

print("Total lines : ", len(text.splitlines()))
print(f"\nThe word {search} used {n} times in this file.")