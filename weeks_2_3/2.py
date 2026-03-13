"""
Project: Basta Fazoolin'
You’ve started a position as the lead programmer for the family-style Italian restaurant 
Basta Fazoolin’ with My Heart. The restaurant has been doing fantastically and seen 
a lot of growth lately. You’ve been hired to keep things organized.
"""

# --- Making the Menus ---

# 1. Create a Menu class.
from pdb import pm
from time import time 

class Menu:

# 2. Give Menu a constructor with the five parameters: 
# self, name, items, start_time, and end_time.
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

# 3. Create the brunch menu object.
# Name: 'brunch'
# Time: 11am to 4pm
# Items: {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
brunch_menu = Menu("brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}, 11, 16)
time :int(11%m - 4%m) 

# 4. Create the early_bird menu object.
# Name: 'early_bird'
# Time: 3pm to 6pm
# Items: {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}
time :int(15%m - 18%m) 
early_bird_menu = Menu("early_bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}, 15, 18)

# 5. Create the dinner menu object.
# Name: 'dinner'
# Time: 5pm to 11pm
# Items: {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}
time :int(17%m - 23%m) 
dinner_menu = Menu("dinner", {'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}, 17, 23)

# 6. Create the kids menu object.
# Name: 'kids'
# Time: 11am to 9pm
# Items: {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}
time :int(11%m - 21%m) 
kids_menu = Menu("kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 11, 21)

# 7. Give the Menu class a string representation method that returns the name 
# of the menu and its availability.
def __repr__(self):
    return f"{self.name} is available from {self.start_time}:00 to {self.end_time}:00"

Menu.__repr__ = __repr__

# 8. Test the string representation by printing the brunch menu.
print(brunch_menu)


# 9. Give Menu a method .calculate_bill() that takes self and purchased_items 
# (a list of item names) and returns the total price.
def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
        total += self.items.get(item, 0)
    return total

Menu.calculate_bill = calculate_bill


# 10. Test .calculate_bill() on the brunch menu with: 
# ['pancakes', 'home fries', 'coffee']
print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

# 11. Test .calculate_bill() on the early_bird menu with: 
# ['salumeria plate', 'mushroom ravioli (vegan)']
print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


# --- Creating the Franchises ---

# 12. Create a Franchise class.
class Franchise:

# 13. Give Franchise a constructor that takes an address and a list of menus.
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

# 14. Create the first two franchises:
# flagship_store: "1232 West End Road" (all four menus)
# new_installment: "12 East Mulberry Street" (all four menus)

flagship_store = Franchise("1232 West End Road", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise("12 East Mulberry Street", [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

# 15. Give Franchise a string representation that returns the address.
def __repr__(self):
    return f"Franchise at address: {self.address}"

Franchise.__repr__ = __repr__

# 16. Give Franchise an .available_menus() method that takes a time and 
# returns a list of Menu objects available at that hour.
def available_menus(self, time):
    available = []
    for menu in self.menus:
        if menu.start_time <= time < menu.end_time:
            available.append(menu)
    return available

Franchise.available_menus = available_menus

# 17. Test .available_menus() at 12 noon (12) and print the results.
available_menus_at_noon = flagship_store.available_menus(12)
print(available_menus_at_noon)
# 18. Test .available_menus() at 5pm (17) and print the results.
available_menus_at_five_pm = flagship_store.available_menus(17)
print(available_menus_at_five_pm)

# --- Creating Businesses ---

# 19. Define a Business class.
class Business:

# 20. Give Business a constructor that takes a name and a list of franchises.
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises


# 21. Create the first Business:
# Name: "Basta Fazoolin' with my Heart"
# Franchises: [flagship_store, new_installment]
basta_fazoolin_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])


# 22. Create the arepas_menu object.
# Name: 'take_a_arepa'
# Time: 10am to 8pm
# Items: {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}
arepas_menu = Menu("take_a_arepa", 10, 20, {
    'arepa pabellon': 7.00,
    'pernil arepa': 8.50,
    'guayanes arepa': 8.00,
    'jamon arepa': 7.50
})

# 23. Create the arepas_place franchise.
# Address: "189 Fitzgerald Avenue"
# Menus: [arepas_menu]
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# 24. Create the new Business object.
# Name: "Take a' Arepa"
# Franchises: [arepas_place]
take_a_arepa_business = Business("take_a_arepa", [arepas_place])