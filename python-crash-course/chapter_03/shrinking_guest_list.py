guests = ['Alex', 'Charles', 'Lando']
print("Sorry, " + guests[2] + " I can not invite you to dinner.")
guests.pop()

for guest in guests:
    print("Reminder to " + guest + " We are still invited.")

del guests[1]
del guests[0]

print(guests)