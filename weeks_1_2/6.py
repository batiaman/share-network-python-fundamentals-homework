"""
Project: Getting Ready for Physics Class
You are a physics teacher preparing for the upcoming semester. 
You want to provide your students with some functions that will help them 
calculate some fundamental physical properties.
"""

# Initial Data
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1

# --- Turn up the Temperature ---

# 1. Write a function called f_to_c that takes an input f_temp, a temperature 
# in Fahrenheit, and converts it to c_temp, that temperature in Celsius.
# It should then return c_temp.
# The equation you should use is: Temp (C) = (Temp (F) - 32) * 5/9
f_to_c = float(input("Enter a temprature in Fahrenheit:"))
c_temp = (f_to_c - 32) * 5/9
print(f"Temperature in Celsius: {c_temp}")

# 2. Let’s test your function with a value of 100 Fahrenheit.
# Define a variable f100_in_celsius and set it equal to the value of 
# f_to_c with 100 as an input.
f100_in_celsius = (100 - 32) * 5/9
print(f"100 Fahrenheit in Celsius: {f100_in_celsius}")

# 3. Write a function called c_to_f that takes an input c_temp, a temperature 
# in Celsius, and converts it to f_temp, that temperature in Fahrenheit.
# It should then return f_temp.
# The equation you should use is: Temp (F) = Temp (C) * (9/5) + 32
c_to_f = float(input("Enter a temprature in Celsius: "))
f_temp = c_to_f * (9/5) + 32
print(f"Temperature in Fahrenheit: {f_temp}")

# 4. Let’s test your function with a value of 0 Celsius.
# Define a variable c0_in_fahrenheit and set it equal to the value of 
# c_to_f with 0 as an input.
c0_in_fahrenheit = 0 * (9/5) + 32
print(f"0 Celsius in Fahrenheit: {c0_in_fahrenheit}")


# --- Use the Force ---

# 5. Define a function called get_force that takes in mass and acceleration. 
# It should return mass multiplied by acceleration.
get_force = train_mass * train_acceleration

# 6. Test get_force by calling it with the variables train_mass and 
# train_acceleration. Save the result to a variable called train_force 
# and print it out. train_mass and train_acceleration have been defined 
# for you at the top of the file. 
print(f"Train Force: {get_force}")

# 7. Print the string “The GE train supplies X Newtons of force.”, 
# with X replaced by train_force.

print(f"The GE train supplies {get_force} Newtons of force.")


# 8. Define a function called get_energy that takes in mass and c.
# c is a constant that is usually set to the speed of light, which is 
# roughly 3 x 10^8. Set c to have a default value of 3*10**8.
# get_energy should return mass multiplied by c squared.
def get_energy(mass, c=3*10**8):
    return mass * c**2

# 9. Test get_energy by using it on bomb_mass, with the default value of c. 
# Save the result to a variable called bomb_energy. bomb_mass has 
# been defined for you at the top of the file.
bomb_energy = get_energy(bomb_mass)

# 10. Print the string “A 1kg bomb supplies X Joules
print(f"A 1kg bomb supplies {bomb_energy} Joules.")