name = input()
password = input()
input_password = input()
while password != input_password:
    input_password = input()
else:
    print(f'Welcome {name}!')