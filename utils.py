if __name__ == '__main__':
    print("Diese Datei enthält Code für die Notebooks, sie wird dort importiert. Sie einfach so auszuführen wird dir nicht viel bringen.")

from time import perf_counter_ns

alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
_TRIES = 100_000

from base64 import b64decode
_super_secret_password = str(b64decode(b'S2FydG9mZmVs'))

def check_password(guess):
    # Check if the length of the password is correct
    if len(guess) != len(_super_secret_password):
        return False
    
    # Check each of the characters
    i = 0
    while i < len(_super_secret_password):
        # If this character is wrong, abort
        if guess[i] != _super_secret_password[i]:
            return False
        i += 1 # Next character
    
    # Looks like all the characters were correct, so the entire password is right 
    return True

def check_password_builtin(guess):
    return guess == _super_secret_password

def time_function_call(func, *args, tries=_TRIES, **kwargs):
    total = 0
    
    for _ in range(tries):
        start = perf_counter_ns()
        func(*args, **kwargs)
        stop = perf_counter_ns()
        
        total += stop - start
    
    return total / tries

def time_password_check(guess, tries=_TRIES):
    return time_function_call(check_password, guess, tries=_TRIES)