#SA
income=float(input("What is your monthly income?" ))

rent=float(input("What is your monthly rent?" ))

utilities=float(input("What is your monthly utilities? "))

groceries=float(input("What is your monthly groceries? "))

transportation=float(input("What is your monthly transportation?" ))

save=.1*income

excess=income-transportation-utilities-groceries-rent-save

print(f"Your rent is {rent} and that is {round (rent/income*100)}% of your income")
print(f"Your utilities are {utilities} and that is {round (utilities/income*100)}% of your income")
print(f"Your groceries are {groceries} and that is {round (groceries/income*100)}% of your income")
print(f"Your transportation is {transportation} and that is {round(transportation/income*100)} of your income")
print(f"You should save {save} a month, that is {round (transportation/income*100)} of your income")
print(f"You have {excess} of spending money each month")