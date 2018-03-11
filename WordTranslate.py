class WordTranslate():
	
	wordsE = {}
	wordsT = {}

	basicListT = [['merhaba', 'selam'], ['lütfen'], ['teşekkürler'], ['nasıl'], ['nasılsın'], ['ne'], ['adın ne'], ['adın ne'], ['kim'], ['kimsin'], ['nerede'], ['neredesin']]
	
	basicListE = [['hi', 'hey', 'hello'], ['please'], ['thanks', 'thank you'], ['how'], ['how are you'], ['what'], ['what’s your name'], ['what is your name'], ['who'], ['who are you'], ['where'], ['where are you']]
	
	
	def __init__(self, word, language):
		self.word = str.lower(word.rstrip('?'))
		self.language = language
		self.setDict()
		
		
	def translate(self):
		if self.language == 'EN':
			dictionary = self.wordsE
		else:
			dictionary = self.wordsT
			
		try:
			newWord = ', '.join(dictionary.get(self.word))
		except:
			newWord = 'Not found'
		return newWord
		
		
	def setDict(self):
		for items in range(len(self.basicListT)):
			for x in self.basicListE[items]: self.wordsE[x] = self.basicListT[items]
		
		for items in range(len(self.basicListE)):
			for x in self.basicListT[items]: self.wordsT[x] = self.basicListE[items]
