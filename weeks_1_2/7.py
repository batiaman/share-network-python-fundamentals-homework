"""
Project: Leet code exercises
LeetCode is a popular platform used by software engineers to 
practice technical coding challenges and prepare for job 
interviews. It helps developers sharpen their logic, understand 
data structures, and improve algorithmic efficiency.

This file contains a few foundational exercises to help you 
get started with the LeetCode style of thinking.
"""

# --- Roman Nomarls ---
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right. 
# However, there are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

def roman_to_int(s):
    # 1. Create variables to store the Roman symbols and their integer values.
    roman_symbols = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # 2. Create a variable to keep track of the total sum.
    total = 0
    prev_value = 0
    
    # 3. Loop through the string 's'. 
    # Hint: You may need to look at the current character and the next character
    # to determine if subtraction should occur.
   
    for char in reversed(s):
        value = roman_symbols[char]
        if value >= prev_value:
            total += value  # Add the value if it's not a subtractive combination
        else:
            total -= value  # Subtract the value if it's a subtractive combination
        prev_value = value
    
    # 4. Return the final total sum.
    return total
# --- Test Cases ---
# Test your function with these values:
# print(roman_to_int("III"))     # Expected Output: 3
# print(roman_to_int("LVIII"))   # Expected Output: 58
# print(roman_to_int("MCMXCIV")) # Expected Output: 1994

print(roman_to_int("III"))
print(roman_to_int("LVIII")) 
print(roman_to_int("MCMXCIV"))