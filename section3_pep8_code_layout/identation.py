# # Bad code
# def long_function(variable_one, variable_two, variable_three, variable_four):
#     print("Hi PEP8")

# Clean code
# 1. Braking inputs line in 8 spaces (2 tabs) for the beginning of the line
# 2. Breaking inputs line only from a bracket
# 3. Every next break is from a comma
def long_function(
        variable_one, 
        variable_two, 
        variable_three, 
        variable_four):
    print("Hi PEP8")

variable_one, variable_two, variable_three, variable_four = 1, 2, 3, 4

# # Bad code
# # Too long
# person = long_function(variable_one, variable_two, variable_three, variable_four)

# Clean code
person = long_function(variable_one, variable_two, 
                       variable_three, variable_four)

# Bad code 
clean = True
available = True
if clean and available:
    print('Ready for viewing')

# Clean code
# 1. Space between variables and if statement
# 2. Alway break variable for if statement after the condition
# for example - available if broken after and
# 3. 2 identations (2 tabs) for new condition
# 4. Add a comment to describe the function

clean = True
available = True

# The If statement checks if we can sell a house, based on clean and avaliable attributes
if clean and \
        available:
    print("Ready for viewing")

# even_numbers = [2,4,6,8,10,12,14,16,18,20] - Wrong 

# Space after a comma in a list
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] 

# Multiple lines
even_numbers = [
    2, 4, 6, 8, 10, 
    12, 14, 16, 18, 
    20
    ] 

def my_func(a, b, c, d, e, f):
    print(a, b, c, d, e, f)

my_func(
    'a', 'b', 'c',
    'd', 'e', 'f'
    )