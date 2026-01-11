import string

def pwChecker():
    while True:
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        numbers = string.digits
        symbols = string.punctuation

        has_upper = False
        has_lower = False
        has_numbers = False
        has_symbols = False

        password = input('Enter password:\n')
        if len(password)<8:
            print('Must be 8 long')
            continue
        for ch in password:
            if ch in upper:
                has_upper = True
            if ch in lower:
                has_lower = True
            if ch in numbers:
                has_numbers = True
            if ch in symbols:
                has_symbols = True

        if has_upper and has_lower and has_numbers and has_symbols and len(password)>=8:
            print(f'Your password : {password}')
            print('Strong!!')
            break
            
        elif has_upper and has_lower and has_numbers and len(password)>=8:
            print(f'Your password : {password}')
            print('Medium!!')
            break

        else:
            print('Weak\nTry Again')
            continue
        
pwChecker()