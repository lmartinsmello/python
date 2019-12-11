name = input('Name: ')
hour = input('Hour: ')

if hour.isdigit():
    hour = int(hour)
    if hour < 0 and hour > 23:
        print('Enter a valid time.')
    else:
        if hour <= 11:
            print(f'{name}, good morning!')
        elif hour <= 18:
            print(f'{name}, good afternoon!')
        elif hour <= 23:
            print(f'{name}, good night!')
else:
    print('Enter the current time between 0 and 23 hours.')
