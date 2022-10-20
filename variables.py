# Generate 1000 unique variables:
import random
import string


def randomword(length):
    rand_word = ''
    letters = string.ascii_lowercase
    for i in range(length):
        rand_word = ''.join(random.choice(letters) for i in range(length))
    return rand_word


def generate_vars():
    for i in range(1000):
        print(randomword(10))


def main():
    generate_vars()


main()
