def isInt(num):
	try:
		int(num)
		return True
	except:
		return False

def isFloat(num):
	try:
		x = float(num)
		float(x)
	
		return True
	except:
		return False				

def printing_number(n):
	while True:	
		if isInt(n):
		
			x = int(n)
			print("This is an integer")
			break
		elif  isFloat(n):
			x = round(float(n))	
			print("converted to Integer %d"%x)
			break
		else:
			print("Please enter number")	
			break
		
x = input(">>>")		
printing_number(x)		