import time
import itertools
import string

def bruteForce(word, length, upper, symbol, digits ):
    
    chars = string.ascii_lowercase

    if upper:
        chars += string.ascii_uppercase

    if symbol:
        chars += string.punctuation

    if digits:
        chars += string.digits

    attempt = 0
    for guess in itertools.product(chars, repeat = length):
        attempt += 1
        guess = ''.join(guess)

        if word == guess:
            return f"{word} is guessed in {attempt:,} guesses!"
        
def main():
    print("Welcome to password guess")
    password = input("Enter the password you want to guess: ")
    length = int(input("Enter the length of the password: "))

    start = time.perf_counter()

    if result := bruteForce(password, length, False, False, True):
        print(result)
    else:
        print("Password not found")

    end = time.perf_counter()    

    print(round(end - start , 2), 's')

if __name__ == '__main__':
    main()


