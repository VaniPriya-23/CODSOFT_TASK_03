import random
import string

def pwd_gen(size):
  str_ = string.ascii_letters+string.punctuation+string.digits
  pwd  = ''
  for i in range(size):
    new_pwd = random.choice(str_)
    pwd += new_pwd
  print('Your Password:',pwd)

lenght = int(input('Enter the size of password: '))
pwd_gen(lenght)
