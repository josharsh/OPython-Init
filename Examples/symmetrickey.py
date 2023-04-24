#import fernet
from cryptography.fernet import Fernet
message = "Hello hackers"

#You can use fernet to generate a key for encryptio and decryption
key = Fernet.generate_key()
fernet = Fernet(key)

#be encoded to byte string before encryption
encMessage = fernet.encrypt(message.encode())
print("first string: ", message)
print("second decrypted string: ", encMessage)

#decrypt the encrypted string
decMessage = fernet.decrypt(encMessage).decode()
print("the decrypted string: ", decMessage)