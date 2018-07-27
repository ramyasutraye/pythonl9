value= raw_input()
if (value >= 'a' and value <='z') or (value >='A' and value <='Z'):
	if value in ['a','e','i','o','u','A','E','I','O','U']:
		print('Vowel')
	else:
		print('Consonant')
else:
	print("invalid")
