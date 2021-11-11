
input1 = input("Are you a cigarette addict older than 75 years old? ").lower()
input2 = input("Do you have a severe chronic disease? ").lower()
input3 = input("Is your immune system too weak? ").lower()

age = True if input1 == "yes" else False
chronic = True if input2 == "yes" else False
immune = True if input1 == "yes" else False

risk = age and (chronic or immune)

if risk:
    print("You are in risky group")
else:
    print("You are not in risky group")






