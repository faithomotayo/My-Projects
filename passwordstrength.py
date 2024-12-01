"""

Author: Faith Omotayo
Date: 28/01/24
Program: This is a password strength checker.
Requirements :
- Min of 1 special char, uppercase, lowercase and num.
- Length >= 10.
- No other chars allowed.

"""

f, n, o , m = 0, 0, 0, 0

password = input("Enter password here: ")
specialchar = '#@!$^&%*()+_'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'

if (len(password) >= 10 ):
    for i in password:
        if (i in specialchar):
            f+= 1
        if (i in uppercase):
            n += 1
        if (i in lowercase):
            o += 1 
        if (i in nums):
            m += 1



if (f >= 1 and n >= 1 and o >= 1 and m >= 1 and f + n + o + m == len(password) ):
    print("Password is valid ! ")
else:
    print("Password is invalid.Please try again\n")
    password = False

while password == False:
    input("Enter password here: \n")
    print("Password is invalid.Please try again\n\n")
    





