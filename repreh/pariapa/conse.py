user_input = ''
while True:
    user_input = input('Pick one: 1) Python | 2) JavaScript | 3) TypeScript [1/2/3]? ')
    if user_input == '1':
        print('You picked Python')
        break
    elif user_input == '2':
        print('You picked JavaScript')
        break
    elif user_input == '3':
        print('You picked TypeScript')
        break
    else:
        print('Type a number 1-3')
        continue
