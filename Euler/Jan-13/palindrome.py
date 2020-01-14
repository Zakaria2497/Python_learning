temp = []
def palindrome():
	for i in range(10,100):
		for j in range(10,100):
			x = i*j
			if x == int(str(x)[::-1]):
				temp.append(x)
palindrome()
print(max(temp))