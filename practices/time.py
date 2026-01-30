time = int(input("what time is it in military time? "))

if time < 12 and time >= 5:
    print("Good morning!")
elif time >= 12 and time < 22:
    print("Good after midday mortal")
else:
    print("go to dreamland before I make you.")