#SA
def budget(kind):
    budget_item=float(input(f" What is your monthly {kind}?"))
    return budget_item


income=budget("income")

rent=budget("rent")

utilities=budget("utilities")

groceries=budget("groceries")

transportation=budget("transportation")

save=.1*income

excess=income-transportation-utilities-groceries-rent-save



print(f"Your rent is {rent} and that is {round (rent/income*100)}% of your income")
print(f"Your utilities are {utilities} and that is {round (utilities/income*100)}% of your income")
print(f"Your groceries are {groceries} and that is {round (groceries/income*100)}% of your income")
print(f"Your transportation is {transportation} and that is {round(transportation/income*100)} of your income")
print(f"You should save {save} a month, that is {round (transportation/income*100)} of your income")
print(f"You have {excess} of spending money each month")