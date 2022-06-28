# Python3 code to demonstrate working of
# Reverse Shift characters by K
# using maketrans() + upper() + list comprehension + translate() + slicing

# initializing string
test_str = 'AeeksForGeeks'

# printing original String
print("The original string is : " + str(test_str))

# initializing K
K = 2

alpha_chars = 'abcdefghijklmnopqrstuvwxyz'

# converted to uppercase
alpha_chars2 = alpha_chars.upper()

# maketrans used for lowercase translation
lower_trans = str.maketrans(alpha_chars, alpha_chars[ -K:] + alpha_chars[ : -K])

# maketrans used for uppercase translation
upper_trans = str.maketrans(alpha_chars2, alpha_chars2[ -K:] + alpha_chars2[ : -K])

# merge lookups
lower_trans.update(upper_trans)

# make translation from lookups
res = test_str.translate(lower_trans)

# printing result
print("The converted String : " + str(res))
