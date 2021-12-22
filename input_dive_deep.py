# Getting multiple values from user using the input function
# Example: Creating the quadratic function that takes in 3 inputs a, b and c and print
# the value of calculated x and y.

a, b, c = input("Enter the values of a, b, c: ").split() # a = 4, a = "4"
user_input_a = eval(a)
user_input_b = eval(b)
user_input_c = eval(c)


def quadratic(a, b, c):
    # -b +- root(b**2 - 4ac)/ 2a
    # Where root(b**2 - 4ac) is the discriminant
    # Calculate the discriminant
    disc = ((b**2) - 4 * a * c)**0.5

    # Calculate the value of x and y
    x = -b + disc / (2 * a)
    y = -b - disc / (2 * a)

    print(f"You have entered a = {a} \nYou have entered b = {b}"
          f"\nYou have entered c = {c}, \nThe values of x and y are : x = {x} and y = {y}")


quadratic(user_input_a, user_input_b, user_input_c)