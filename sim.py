from user import User

if __name__ == '__main__':
	alice = User('Alice')
	bob = User('Bob')

	message = "Hello, Bob!"

	print(f"Message: {message}")
	alice.generate_keys()
	bob.generate_keys()
	cipher_text = alice.encrypt(message, bob)
	print(f"Cipher text: {cipher_text}")
	plain_text = bob.decrypt(cipher_text)
	print(f"Plain text: {plain_text}")