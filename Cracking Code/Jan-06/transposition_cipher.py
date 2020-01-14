
#import pyperclip

def main():
	myMessage = 'Common sense is not so common.'
	myKey = 8
	
	ciphertext = encryptMessage(myKey,myMessage)
	
	print(ciphertext + 'I')
	
	
	#pyperclip.copy(ciphertext)
	
def encryptMessage(key,message):
	ciphertext = ['']*key	
	print(ciphertext)
	
	for column in range(key):  # 0 to 7
		currentIndex = column
		
		while currentIndex < len(message):
			ciphertext[column] += message[currentIndex]
			
			currentIndex += key
			
	return ''.join(ciphertext)
	
if __name__ == '__main__':
	main()				             
				
	