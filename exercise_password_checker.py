username = input('Username: ')
password = input('Password: ')
hidden_password = '*' * len(password)
print(f'Hi {username}! Your password {hidden_password} is {len(password)} letters long')
