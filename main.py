
letter_dict = {}
word_list = input("Please enter five words separated by comma: ").split(",")
for word in word_list:
    for letter in word:
        if letter in letter_dict:
           letter_dict[letter] += 1
        else:
           letter_dict[letter] = 1




print(word_list)

print(dict(sorted(letter_dict.items())))