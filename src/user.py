from utils import RSACipher

class User:
	def __init__(self, name):
		self.name = name
		self.public_key = None
		self.__private_key = None
		self.q = None
		self.p = None
		self.N = None

	def generate_keys(self):
		print(f"Generating keys for {self.name}...")
		if self.q is None or self.p is None:
			self.p, self.q = RSACipher.generate_two_random_primes()
		self.N = self.p * self.q
		self.create_public_key()
		self.create_private_key()

	def create_public_key(self):
		self.public_key = RSACipher.find_coprime(self.p, self.q)

	def create_private_key(self):
		self.__private_key = RSACipher.find_mod_eq_one(self.p, self.q, self.public_key)

	def encrypt(self, message, recipient):
		print(f"{self.name} is encrypting the message for {recipient.name}...")
		return [pow(ord(char), recipient.public_key, recipient.N) for char in message]

	def decrypt(self, message):
		print(f"{self.name} is decrypting the message...")
		return ''.join([chr(pow(char, self.__private_key, self.N)) for char in message])
