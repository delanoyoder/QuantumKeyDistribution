from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

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

# Example usage:

key = get_random_bytes(32)  # 32 bytes = 256 bits
aes = AESCipher(key)

message = "Hello, AES Encryption!"
iv, ciphertext = aes.encrypt(message)
print("Encrypted:", ciphertext)

decrypted_message = aes.decrypt(iv, ciphertext)
print("Decrypted:", decrypted_message)
