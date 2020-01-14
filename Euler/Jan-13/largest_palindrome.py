def isProduct(num):
	arr = []
	for i in range(1,num+1):
		if num%i==0:
			arr.append(i)
		else:
			continue
	print(arr)
	
	x = round(len(arr)/2)
	print(x)
	
	for i in range(x+1):
		a=arr[i]
		b=arr[len(arr)-i-1]
		
		print(a,b,end ="\t")
number = int(input('>>'))
isProduct(number)

	
	
	
	
	
	
	
	
	
		
		
		
				