
from telnetlib import theNULL
import string

opp_D = 0

def customEncrypt(inputText, N, D):
    final = inputText[::-1]

    #Get all ascii values except space and !
    ascii_values = ''.join(chr(i) for i in range(34, 127))

    #Make translation based on D value
    if D == -1:
        asc_trans = str.maketrans(ascii_values, ascii_values[-N:] + ascii_values[ : -N])
    elif D == 1:
        asc_trans = str.maketrans(ascii_values, ascii_values[+N:] + ascii_values[ : +N])
    else:
        print("Invalid value for D, Values allowed for D are -1 or 1 only.")
        exit(1)
    
    # make translation from lookups
    res = final.translate(asc_trans)
    return res

def testCustomEncrypt():
    print("Testing Custom Encryption Algorithm")
    #Take input for user_id and pwd while performing checks
    while True:
        try:
            user_id = input("Enter UserID as text : ")
            if " " in user_id or "!" in user_id:
                raise Exception("userID can not contain \'!\' or \' \'. Try again")
            pwd = input("Enter password as text : ")
            if " " in pwd or "!" in pwd:
                raise Exception("Password can not contain \'!\' or \' \'. Try again")
            break
        except:
            print("userID or Pwd can not contain \'!\' or \' \'. Try again")
    

    while True:
        try:
            N = int(input("Please enter the value of N: "))
            #TODO: Improve checking D value here
            D = int(input("Please enter the value of D: "))
            break     
        except ValueError:
            print("Oops!  That was no valid value.  Try again...")
        except:
            print("Invalid value for D, Values allowed for D are -1 or 1 only")

    #Call Custom Encryption with original userID and pwd value to get encrypted values
    e_user_id = customEncrypt(user_id, N, D)
    print("encrypted userid : " + str(e_user_id))

    e_pwd = customEncrypt(pwd, N, D)
    print("encrypted password : " + str(e_pwd))
    
    #Call Custom Encryption with reverse D value and encrypted userId and pwd to get back original
    if D == -1:
        opp_D = 1
    elif D == 1:
        opp_D = -1

    o_user_id = customEncrypt(e_user_id, N, opp_D)
    final_user_id = o_user_id[::1]
    print("Original userid : " + str(final_user_id))

    o_pwd = customEncrypt(e_pwd, N, opp_D)
    final_pwd = o_pwd[::1]
    print("Original password : " + str(final_pwd))
         
#Call Test Custom Encryption function
testCustomEncrypt()


#Task
# Question 1 : Which of the userid and password combination(s) in the table above are present in the database?
"""
asamant    Temp123   -----> wqdpdvd 654sphW
skharel    Life15$   -----> ohudknv '84hilO
"""

# Question 2 : Which userid(s) is/are present in the database, but the password does not match the password(s) in the table above?    
"""
aissa        TheKing%^&     ----> dvvld )a(wkjlO
bjha          $72messenge   ----> dkme roohK5:'
"""

# Question 3 : Which userid(s) do/does not meet the requirements of a userid?
"""
Ally!        God$12 
"""
