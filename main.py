import string
import random

def get_length():
	length = input("\n	Password length: 	")
	return int(length)

ASCII = string.ascii_uppercase + string.ascii_lowercase
DIGITS = string.digits
SPECIAL_CHARACTERS = string.punctuation
PASSWORD = ''.join(random.choice(ASCII + DIGITS + SPECIAL_CHARACTERS) for _ in range(get_length()))

if __name__ == '__main__':
	print("\n	Password: 		" + PASSWORD)
