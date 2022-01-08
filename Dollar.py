import string

x = {}
for index,item in enumerate(string.lowercase):
    x[item] = index +1

def isDollarWord(word):
    lowercase = word.lower().strip()
    total = 0
    for letter in lowercase:
        if letter in x:
            total += x[letter]
    return total == 100

words = open("alp.txt")

for line in words:
    if isDollarWord(line):
        print(line)