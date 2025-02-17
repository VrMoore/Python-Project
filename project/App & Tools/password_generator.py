import random
print('Welcome to My Simple Password Generator\n')

pass_number = int(input('How many passwords do you want? : '))
pass_length = int(input('Enter the length of the password : '))

def password_generator(number,length) : 
  characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@'
  for i in range(number) :
    password = ''
    for j in range(length) :
      password += random.choice(characters)
    print(password)

password_generator(pass_number, pass_length)
