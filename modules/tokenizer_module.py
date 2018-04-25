import re
import unicodedata


class Tokenizer:


	def __init__( self, text = ""):

		self.text = text
		self.tokens = [] # tokens del texto




	def tokenize ( self ):

		pattern = re.compile(r'\W+') # Separa por síbolos no alfanuméricos
		
		self.tokens = pattern.split(self.deleteAccent(self.text.lower()))


	
	def deleteAccent( self, s ):
   		return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
