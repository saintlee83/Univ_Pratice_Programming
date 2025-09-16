
age = int(input('How old are you? : '))

if age >= 200:
	print("You are...")
else :
	if age < 18 :
		print("You're a minor")
	elif age < 65 :
		print("You're an adult")
	else :
		print("You're a senior")
