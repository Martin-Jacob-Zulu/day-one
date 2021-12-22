# We need a boolean check for hit should match in the db
is_hit = 99 * [False]
end_of_input = False

# Read numbers from the user
while not end_of_input:
    user_input = input("Enter the numbers separated by a blank space: ")
    list_user_input = user_input.split() # Returned as a string
    list_of_input = [eval(x) for x in list_user_input] # Converts the user input into number values

    for number in list_of_input:
        if number == 0:
            end_of_input = True
        else:
            is_hit[number - 1] = True
# Checking
all_hit = True # Assume that all number are a hit
for i in range(99):
    if not is_hit[i]:
        all_hit = False
        break
# Display Results
if all_hit:
    print("You've won")
else:
    print("Sorry no win for you today")
