user = input('Username: ')
password = input('Password: ')
user_bd = 'luana.mello'
pass_bd = '123456'


if user_bd == user and pass_bd == password:
    print('Successfully logged in!')
else:
    print('Incorrect username or password.')
