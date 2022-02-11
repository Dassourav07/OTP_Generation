import random
import os
import math
import smtplib

print('Generate One Time Password')

Chart = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=][.,!@#$^&*()_+:abcdefghijklmnopqrstuvwxyz'
Num = input('OTP Size')
Num = int(Num)
Char = input('Enter Number of OTP to generate')
Char = int(Char)

print = ('\nYour OTP is:')

for pwd in range(Num):
    OTP =''
    for c in range(Char):

       OTP +=random.choice(Chart)

    print(OTP)
msg= OTP
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("Your Gmail Account", "You app password")
emailid = input("Enter your email: ")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("Verified")
else:
    print("Please Check your OTP again")
