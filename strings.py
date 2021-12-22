my_string = "I love programming"
altered = my_string.replace("love", "like")
uppercase = my_string.upper()
capitalized = my_string.capitalize()
print(my_string.lower())

chars = []
count = 0
for char in my_string:
    if char == "g":
        count += 1
        chars.append(char)

chars_tupple = ()
count = 0
for char in my_string:
    if char == "g":
        count += 1
        chars.append(char)

print(chars)
print(count)
print(chars_tupple)
# print(capitalized)
