import random

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
