
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
    user_id = input("Enter UserID as text : ")
    pwd = input("Enter password as text : ")

    while True:
        try:
            N = int(input("Please enter the value of N: "))
            #TODO: Improve checking D value here
            D = int(input("Please enter the value of D: "))
            break     
        except ValueError:
            print("Oops!  That was no valid value.  Try again...")

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


