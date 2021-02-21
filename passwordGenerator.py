'''
RANDOM PASSWORD GENERATOR

Author: Talmage Mitchell
Create Date: 2021-02-15
'''

import random

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '0123456789'
special = '!@#$%^&*()_+'


def pass_gen(pwlength):

	password = ''

	#Start PWD generator
	for num in range(pwlength):

		#RNG determines which characters will be used, and is weighted more towards letters and numbers
		rand = random.randint(1,10)	

		#Gen Alpha character
		if 1 <= rand <= 4:
			rand = random.randint(0, 25)

			#assign random amount of lower and uppercase letters
			if random.randint(0,1) == 0:
				password += alpha[rand]
			else:
				password += alpha[rand].lower()

		#Gen numerical character
		elif 5 <= rand <= 8:
			rand = random.randint(0,9)
			password += nums[rand]

		#Gen Special character
		else:
			rand = random.randint(0,11)
			password += special[rand]

	return password

#Run if file is being run directly
if __name__ == "__main__":

	while True:
		try:
			pwlength = int(input("\nPlease enter how long you want your password to be (at least 6 characters long): "))
		except:
			print("Please enter a valid number!")
		else:
			if pwlength < 6:	#Minimum password length is 6
				print("Please enter a number greater than 6!")
			else:
				break

	mypass = pass_gen(pwlength)

	print(f"\nYour randomly generated password is: {mypass}")



