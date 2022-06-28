
from telnetlib import theNULL


a = "Highfive"
print("a =", a)

while True:
     try:
         N = int(input("Please enter the value of N: "))
         D = int(input("Please enter the value of D: "))
         break     
     except ValueError:
         print("Oops!  That was no valid value.  Try again...")
         

final = a[::-1]

alpha_chars = 'abcdefghijklmnopqrstuvwxyz'

# converted to uppercase
alpha_chars2 = alpha_chars.upper()

if D == -1:
    # maketrans used for lowercase translation
    lower_trans = str.maketrans(alpha_chars, alpha_chars[ -N:] + alpha_chars[ : -N])

    # maketrans used for uppercase translation
    upper_trans = str.maketrans(alpha_chars2, alpha_chars2[ -N:] + alpha_chars2[ : -N])
elif D == 1:
    # maketrans used for lowercase translation
    lower_trans = str.maketrans(alpha_chars, alpha_chars[ +N:] + alpha_chars[ : +N])

    # maketrans used for uppercase translation
    upper_trans = str.maketrans(alpha_chars2, alpha_chars2[ +N:] + alpha_chars2[ : +N])
else:
    print("Invalid value for D, Values allowed for D are -1 or 1 only.")
    exit(1)

# merge lookups
lower_trans.update(upper_trans)

# make translation from lookups
res = final.translate(lower_trans)

# printing result
print("The converted String : " + str(res))

