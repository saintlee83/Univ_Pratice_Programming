a = input("enter mutiple int : ")
tmp = a.split()

result = 0
for i in tmp:
	print(i)
	result += int(i)

print("sum is", result)