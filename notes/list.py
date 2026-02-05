numbers = [1,823,109332,132984,734927643,37,0,9,83,84]
names = ["cat", "dog", "food", "computer", "people", "yes", "no"]

print(len(names))
names[0] = "Eric"
names.append("Joe") #adds to the end of the list
index = names.index("dog")
names.pop(3) #removes item from the list based on index (or the end inf no no index is given)
print(names)

for name in names:
    print(f"Hello {name}")

    for number in numbers:
        print(f"{number}- 10 = {number-10}")
 
 #iteration => repetition 
for i in range(20):
    print(f"My code has iterated {i} times")