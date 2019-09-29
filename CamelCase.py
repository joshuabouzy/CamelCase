from WordCount import camelcase

print("This function will determine how many words are in a string in CamelCase format.\n")

print("Note, should only be used with strings that do not contain an empty space.\n")

print("To determine how many words are in a string, simple input the string below.\n")

s = input()

result = camelcase(s)

print("There are " + str(result) + " words in the string.\n")


