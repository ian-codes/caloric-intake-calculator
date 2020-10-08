
# Personal  Input Values
num1 = input("Enter your weight in kg: ")
num2 = input("Enter your height in cm: ")
num3 = input("Enter your age in years: ")
result = round(66.5 + (13.75 * float(num1)) + (5 * float(num2)) - (6.76 * float(num3)))
print("\n")

# BMR
print("Your BMR (Basal Metabolic Rate) is:", result,
      "calories per day.")
print("\n")
input("Press Enter to continue.")
print("\n")

# Activity Level Selection
print("Select your activity level: \n")
print("1) Sedentary (little to no exercise)")
print("2) Light activity (light exercise 1-3 days/week)")
print("3) Moderate activity (moderate exercise 3-5 days/week)")
print("4) Heavy activity (heavy exercise 6-7 days/week)\n")

dictionary = {
    "1":1.2,
    "2":1.38,
    "3":1.55,
    "4":1.73,
}

# TDEE
while True:
    key = input("Enter a value between 1 - 4" "\n")
    if key.lower() not in dictionary:
        print("You didn't select a value between 1 - 4.")
    else:
        break

print(f"Your TDEE (Total Daily Energy Expenditure) is approximately {round(result * dictionary[str(key)])} calories per day.")
res1 = round(result * dictionary[str(key)])

# Weight goal
print("Select your  goal: \n")
print("1) I wish to gain weight.")
print("2) I wish to lose weight")
print("3) I wish to maintain my current weight \n")


def weight_gain():
    return(res1 + 500)


def weight_loss():
    return(res1 - 500)


def weight_maint():
    return(res1)


dictionary2 = {
    "1": weight_gain,
    "2": weight_loss,
    "3": weight_maint,
}

while True:
    goal = input("Choose an option from 1 - 3 \n")
    if goal not in dictionary2:
        print("You didn't select a value between 1 - 3.")
    else: break

if goal == "1":
    print("Your caloric intake should be at approximately", dictionary2[str(goal)](),
        "calories per day, in order for you to gain weight.")
elif goal == "2":
    print("Your caloric intake should be at approximately.", dictionary2[str(goal)](),
          "calories per day, in order for you to lose weight.")
elif goal == "3":
    print("Your caloric intake should be at approximately", dictionary2[str(goal)](),
          "calories per day, in order for you to maintain your current weight. This is the same value as your \n"
          "TDEE previously calculated.")

print("\n")

input("Press Enter to exit.")
