# Create an empty set named showroom.
showroom = set()
# Add four of your favorite car model names to the set.
showroom.add("Aston Martin V12 Vanquish")
showroom.add("Maserati GranTurismo")
showroom.add("Lotus Elise")
showroom.add("Tesla Modal X")
# Print the length of your set.
print(len(showroom))
showroom.add("Lotus Elise")
# Pick one of the items in your show room and add it to the set again.
# Print your showroom. Notice how there's still only one instance of that model in there.
print(showroom)
# Using update(), add two more car models to your showroom with another set.
showroom.update({"Alfa Romeo Stelvio"}, ["Ford Mustang"])
print("updated showroom:", showroom)
# You've sold one of your cars. Remove it from the set with the discard() method.
showroom.remove("Lotus Elise")
print("cars left:", showroom)



# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = set()
junkyard.update({"Toyata Tacoma"}, {"Nissan Sentra"}, {"Honda Civic"}, {"Ford Mustang"})
print("junkyard:", junkyard)

# Use the intersection method to see which cars exist in both the showroom and that junkyard.
print(showroom.intersection(junkyard))

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.
showroom = showroom.union(junkyard)
print(showroom)
# Use the discard() method to remove any cars that you acquired from the junkyard that you want in your showroom.
print(junkyard.discard(junkyard))
# print(junkyard)

