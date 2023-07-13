#username = ['admin', 'alice', 'bob', 'carera', 'danny']
username = []

if username:
    for name in username:
        if name == 'admin':
            print('Hellon ' + name + ' would you like to see a status report?')
        else:
            print('Hellon ' + name + ' thank you for logging in again.')
else:
    print('We need to find some users!')