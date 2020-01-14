import time,os,sys, transpositionEncrypt,transpositionDecrypt

def main():
	inputFilename = 'fran.encrypted.txt'
	
	outputFilename = 'fran.decrypted.txt'
	print('11111')
	
	myKey = 10
	myMode ='decrypt'
	
	if not os.path.exists(inputFilename):
		print('The file %s does not exists. Quiting.....'%inputFilename)
		sys.exit()
		
	if os.path.exists(outputFilename):
	
		print("This will overwrite the file %s.(C)ontinue or (Q)uit?" % (outputFilename))
		
		response = input('>>')
		print ('222222')
		if not response.lower().startswith('c'):
			print('3333333')
			sys.exit()
			
	fileObj = open(inputFilename)
	content = fileObj.read()
	fileObj.close()
	print ('444444')
	print("%sing...." %(myMode.title()))	
	
	startTime = time.time()
	
	if myMode == 'encrypt':
		
		translated = transpositionEncrypt.encryptMessage(myKey,content)		
		
	elif myMode ==	'decrypt':
		
		translated = transpositionDecrypt.decryptMessage(myKey,content)	
		
		
	totalTime = round(time.time() - startTime, 2)		
	
	print ('%sion time: %s seconds' %(myMode.title(),totalTime))
	
	outputFileObj = open(outputFilename,'w')
	outputFileObj.write(translated)
	outputFileObj.close()
	
	print ('Done %sing %s(%s character).'%(myMode,inputFilename, len(content)))
	
	print ('%sed file is %s.' %(myMode.title(),outputFilename))
	
if __name__ == '__main__':
		main()