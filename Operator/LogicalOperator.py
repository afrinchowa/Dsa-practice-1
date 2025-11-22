# Logical Operators
# Logical operators are used to combine conditional statements:

# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)	
# Examples

# Test if a number is greater than 0 and less than 10:

x = 5

print(x > 0 and x < 10)
# Example
# Test if a number is less than 5 or 
# greater than 10:

x = 5

print(x < 5 or x > 10)
# Example
# Reverse the result with not:

x = 5

print(not(x > 3 and x < 10))