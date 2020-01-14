import math
def main():
	myMessage = "Cenoonommstmme oo snnio. s s c"
	myKey = 8
	
	plaintext = decryptMessage(myKey,myMessage)
	print(plaintext +'I')
	
	
def decryptMessage(key,message):	
	numOfColumns = int(math.ceil(len(message) / float(key)))
	numOfRows = key
	
	numOfShadedBox = (numOfColumns * numOfRows) - len(message)
	
	plaintext = [''] * int(numOfColumns)
	
	column = 0
	row = 0
	
	for symbol in message:
		plaintext[column] += symbol
		column += 1
	
	
		if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBox):
			column = 0
			row += 1
			
	return ''.join(plaintext)
	
if __name__ == '__main__':
	main()		
	