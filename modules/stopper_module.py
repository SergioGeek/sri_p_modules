
from nltk.corpus import stopwords

class Stopper:



	def __init__( self, sW = "spanish" ):

		self.stopWords = set(stopwords.words(sW))
		self.stoppedList = []


	

	def stopping( self, tokenizedWords ):

		for tw in tokenizedWords:
			if tw not in self.stopWords:
				self.stoppedList.append(tw)

		return self.stoppedList
