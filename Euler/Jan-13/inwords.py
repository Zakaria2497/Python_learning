num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero',100:'One Hundred',200:'Two hundred',\
            300:'Three Hundred',400:'Four Hundred',500:'Five Hundred',600:'Six Hundred',700:'Seven Hundred',\
            800:'Eight Hundred',900:'Nine Hundred',1000:'One Thousand',2000:'Two Thousand',\
            3000:'Three Thousand',4000:'Four Thousand',5000:'Five Thousand',6000:'Six Thousand',\
            7000:'Seven Thousand',8000:'Eight Thousand',9000:'Nine Thousand',10000:'Ten Thousand'
            }
def n2w(n):

	x = n%100
	y = n%1000
	try:
		print (num2words[n])
	except KeyError:
		try:
			print (num2words[n-n%10] + num2words[n%10].lower())
		except KeyError:
			try:
				# x=n%100
				print(x)
				print (num2words[n-n%100] +" and "+ num2words[x-x%10].lower()+"-" + num2words[x%10].lower())
			except KeyError:	
				try:
					print(num2words[n-y] + " " + num2words[y-x].lower() +" and "+ num2words[x-x%10].lower() +"-"+ num2words[x%10].lower())
				except KeyError:	
					print ('Number out of range')

		
x = int(input(">>"))
n2w(x)			