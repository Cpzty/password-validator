#password validator
special_chars = "!@#$%^&*()_+-=<>?,./?;:\\"

#at least 8 characters long

def is_valid_password(password):
    #check length
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        return False
    #at least one lowercase
    if password.upper() == password:
        print("Password must have at least one lowercase")
        return False
    #at least one uppercase
    if password.lower() == password:
        print("Password must have at least one uppercase")
        return False
    #at least one digit
    any_number = False
    for char in password:
        if char.isnumeric():
            any_number = True
            break
    if not any_number:
        print("Password must have at least one number")
        return False
    #at least one special character
    if not set(password).difference(special_chars):
        print("Password must have at least one special character")
        return False
    print("Password is valid")
    return True

if __name__ == '__main__':
    valid_pass = is_valid_password("abcdefg123!")

