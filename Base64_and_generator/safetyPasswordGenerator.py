# Safety password generator

import random
import string


def generate_password():
    password = ""
    for x in range(12):
        a = random.choice(['$', '*'])
        b = random.choice(string.ascii_lowercase)
        c = random.randint(0,9)
        d = random.choice(string.ascii_uppercase)
        password = password + a + b + str(c) + d
    return password


print("Generuje bezpieczne hasło ...")
print(generate_password())