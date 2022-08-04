text = input()
total_value = 0
for vowel in text:
    if vowel == "a":
        total_value += 1
    elif vowel == "e":
        total_value += 2
    elif vowel == "i":
        total_value += 3
    elif vowel == "o":
        total_value += 4
    elif vowel == "u":
        total_value += 5
print (total_value)