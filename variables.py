# Variables
"""(Financial application: calculate interest) If you know the balance and the annual
 percentage interest rate, you can compute the interest on the next monthly payment
 using the following formula:
 interest = balance * (annualInterestRate / 1200)
 Write a program that reads the balance and the annual percentage interest rate
 and displays the interest for the next month. Here is a sample run:"""

# formula is interest = balance * (annualInterestRate / 1200)
balance = input("What is your bank balance: ")
annual_interest_rate = input("What is the annual interest rate: ")

interest = int(balance) * (int(annual_interest_rate) / 1200)
print(interest)

user_name = input("Enter you name: ")
height = input("Enter your height in metres: ")
weight = input("Enter your weight in Kilograms: ")


def bmi_calculator(height, weight):
    bmi = float(weight) / float(height) ** 2

    if bmi >= 35:
        comment = "Overweight, Please seek medical advice."
    elif bmi < 35 and bmi > 25:
        comment = "Normal, you're perfectly okay."
    elif bmi < 25:
        comment = "Underweight, Please seek medical advice."
    print(f"Hello, {user_name} Your BMI value is, {bmi}. \n"
          f"----------------------------------- \n"
          f"Depending your BMI value, your health is {comment}")

bmi_calculator(height, weight)