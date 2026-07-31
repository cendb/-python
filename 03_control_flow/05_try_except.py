try:
    number = int(input("Enter a number to divide 100 by: "))
    print("You entered:", number)
    result = 100 / number

except ValueError:
    print("That's not a valid number. Please enter an integer.")
except ZeroDivisionError:
    print("You cannot divide by zero. Please enter a number greater than zero.")
else:
    print("Result of 100 divided by your number is:", result)