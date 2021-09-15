# Second Part of the Programme am Making

print ('Hello New User')
print ('My name is Vhaustro and I am your Personal Assistant,')
print ('I shall help you organize your life.')
name = input ('To get started, Kindly Enter your Name:')

print (' Hello' + name + '\n and Welcome. ')

#comment = input ('How is it going?')

#print ('Same here, am excited to show you around.')

print ('Before we proceed I have one question,')

gender = input ('Are you Male or Female?')

if gender == 'Male' or 'Female' :
    print ('Nice Sir' + name)
else:
    print ('Good Mrs.' + name)

assent = 18

age = input ('Another enquiry, \nHow old are you?')

if age >= 18: 
    assent = 18
    print('You are above the age of' + str(assent))
else: 
    assent = 18
    print ('You are below the age of' + str(assent))


