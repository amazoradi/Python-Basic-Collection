planet_list = ["Mercury", "Mars"]

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Neptune", "Uranus"])
print(planet_list)

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")

print(planet_list)

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets=slice(0, 4)
print("rocky:", planet_list[rocky_planets], "all:", planet_list)


# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print("the sad truth:", planet_list)

# Challenge: Iterating over planets
# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
spacecraft = [('Cassini', 'Saturn'), ("Zoradi", "Neptune"), ("Planet Express Delivery Ship", "Mars"), ("Love Bug", "Venus")]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
  for craft, place  in spacecraft:
    if planet == place:
      print(f"The {craft} landed on {planet}.")
