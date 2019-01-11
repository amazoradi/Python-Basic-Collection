# Create a tuple named zoo that contains your favorite animals.
zoo = ("Otter", "Octopus", "Elephant", "Seal", "Tiger")

# Find one of your animals using the .index(value) method on the tuple.
print(zoo[1])

# Determine if an animal is in your tuple by using value in tuple.
if "Otter" in zoo:
  print("It's there!")

# Create a variable for each of the animals in your tuple with this cool feature of Python.
(Otter, Octopus, Elephant, Seal, Tiger) = zoo
print(Otter)
print("tupple of zoo:", zoo)

# Convert your tuple into a list.
zoo = list(zoo)
print("List of zoo:", zoo)

# Use extend() to add three more animals to your zoo.

zoo.extend(["Mouse-Rat", "Monkey", "Shark"])

print("extended zoo:", zoo)

# Convert the list back into a tuple.

zoo = tuple(zoo)
print("extended zoo as a tuple:", zoo)