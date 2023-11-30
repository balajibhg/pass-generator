import random
import string

def generate_password(length=60):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in
 
range(length))
    return password

print(generate_password())
