current_users = ['John', 'Mike', 'Sarah', 'Emma', 'David']
new_users = ['Mark', 'Lisa', 'John', 'Emily', 'Sam']

# Convert all usernames in current_users to lowercase
current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username '{user}' is not available. Please enter a new username.")
    else:
        print(f"The username '{user}' is available.")
