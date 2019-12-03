num_int = input('Enter an integer: ')

if num_int.isdigit():
    num_int = int(num_int)
    if num_int % 2 == 0:
        print(f"{num_int} it's even")
    else:
        print(f"{num_int} it's odd")
else:
    print('This is not a integer')
