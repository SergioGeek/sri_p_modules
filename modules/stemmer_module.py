from nltk.stem.snowball import SnowballStemmer

class Stemmer:

	def __init__( self, stm = "spanish" ):

		self.stemmer = SnowballStemmer("spanish")
		self.stmDic = {}


	def stemming( self, stopperWords ):


		for stw in stopperWords:

			stmw = self.stemmer.stem( stw )


			if stmw in self.stmDic:

				self.stmDic[stmw] += 1

			else:

				self.stmDic[stmw] = 1
