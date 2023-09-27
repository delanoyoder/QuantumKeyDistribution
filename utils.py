from functools import lru_cache
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class RSACipher:
	@staticmethod
	@lru_cache
	def phi(p, q):
		return (p - 1) * (q - 1)

	@staticmethod
	@lru_cache
	def gcd(a, b):
		while b:
			a, b = b, a % b
		return abs(a)  # Using abs() to ensure the result is non-negative

	@classmethod
	@lru_cache
	def is_coprime(cls, N, c):
		return cls.gcd(N, c) == 1

	@classmethod
	@lru_cache
	def find_coprime(cls, p, q):
		N = p * q
		for e in range(2, cls.phi(p, q)):
			if cls.is_coprime(N, e) and cls.is_coprime(cls.phi(p, q), e):
				return e
		return None

	@classmethod
	@lru_cache
	def find_mod_eq_one(cls, p, q, e):
		for d in range(1, p * q):
			if (d * e) % cls.phi(p, q) == 1:
				return d
		return None

	@staticmethod
	def is_prime(n):
		"""Check if a number is prime."""
		if n <= 1: # 1 is not prime
			return False
		if n <= 3: # 2 and 3 are prime
			return True
		if n % 2 == 0 or n % 3 == 0: # multiples of 2 and 3 are not prime
			return False
		i = 5
		while i * i <= n: # only need to check up to sqrt(n)
			if n % i == 0 or n % (i + 2) == 0: # multiples of i and i+2 are not prime
				return False
			i += 6 # all primes greater than 3 are of the form 6k +/- 1
		return True

	@classmethod
	def generate_random_prime(cls, start, end):
		"""Generate a random prime number between start and end."""
		while True:
			num = random.randint(start, end)
			if cls.is_prime(num):
				return num

	@classmethod
	def generate_two_random_primes(cls, start=1000, end=10000):
		"""Generate two random prime numbers between start and end."""
		prime1 = cls.generate_random_prime(start, end)
		prime2 = cls.generate_random_prime(start, end)
		while prime1 == prime2:
			prime2 = cls.generate_random_prime(start, end)
		return prime1, prime2

class AESCipher:
	def __init__(self, key):
		"""
		:param key: The secret key. For AES, this must be 16, 24, or 32 bytes long.
		"""
		self.key = key

	def encrypt(self, plaintext):
		"""
		Encrypts plaintext using AES.
		:param plaintext: The plaintext string to encrypt.
		:return: The encrypted message and the initialization vector (IV).
		"""
		cipher = AES.new(self.key, AES.MODE_CBC)
		ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
		return cipher.iv, ciphertext

	def decrypt(self, iv, ciphertext):
		"""
		Decrypts an AES encrypted message.
		:param iv: The initialization vector used for encryption.
		:param ciphertext: The encrypted message to decrypt.
		:return: The decrypted plaintext string.
		"""
		cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
		plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
		return plaintext.decode('utf-8')

def get_random_key(length):
	return get_random_bytes(length)
