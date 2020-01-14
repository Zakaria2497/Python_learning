#import dictionary
import time
startt = time.time()
UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + '\t\n'
print(LETTERS_AND_SPACE)
def loadDictionary():
	
	dictionaryFile = open('dictionary.txt')
	englishWords = {}
	
	for word in dictionaryFile.read().split('\n'):
		englishWords[word] = None
		
		dictionaryFile.close()
	return englishWords
	


	
ENGLISH_WORDS = loadDictionary()

def getEnglishCount(message):
	message = message.upper()
	message = removeNonLetters(message)
	possibleWords = message.split()
	#print(possibleWords)
	if possibleWords ==[]:
		return 0.0
	
	matches = 0
	for word in possibleWords:
		print(word,"jdhkjhkdsf")
		print(possibleWords)
		print('llllllllll')
		if word in ENGLISH_WORDS:
			matches += 1
			print(matches)
			print('>>>>>>')
			
	return float(matches)/len(possibleWords)					
		
def removeNonLetters(message):
	lettersOnly = []
	
	for symbol in message:
		if symbol in LETTERS_AND_SPACE:
			lettersOnly.append(symbol)
	return ''.join(lettersOnly)
	
	
def isEnglish( message, wordPercentage = 20,letterPercentage = 85):
	
	wordsMatch = getEnglishCount(message)*100 >= wordPercentage
	
	numLetters = len(removeNonLetters(message))
	
	messageLettersPercentage = float(numLetters)/len(message)*100
	
	lettersMatch = messageLettersPercentage >= letterPercentage
	
	return wordsMatch and lettersMatch
	
tiem = round(startt - time.time(),2)
print("time is %s"%tiem)	
				